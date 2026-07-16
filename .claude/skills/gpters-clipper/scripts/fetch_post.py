# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""fetch_post.py <post-url> — 지피터스 게시글 본문만 verbatim 마크다운으로 출력.

실행:  uv run .claude/skills/gpters-clipper/scripts/fetch_post.py "<게시글 URL>"
(uv가 PEP 723 헤더를 읽어 격리 환경에 requests를 자동 설치한다 —
 setup-guide.md §2 uv 컨벤션. venv를 직접 만들 필요 없음.)

왜 이렇게 가져오나:
- gpters.org는 JS SPA라 원본 URL을 그냥 받으면 본문이 없다(실측 2026-07-14,
  1.1MB HTML에 본문 텍스트 0건). 그래서 Jina Reader(r.jina.ai)를 경유한다.
- Jina 기본 응답은 게시글에 따라 사이트 헤더/네비/추천글/뉴스레터 위젯이
  통째로 섞여 온다(글마다 다름). `x-target-selector: article.prose` 헤더로
  글 콘텐츠 요소만 지정하면 그 셸이 애초에 안 들어온다(실측 확인).
- 셀렉터를 `div.basis-full > article.prose`처럼 좁히면 안 된다 — BetterMode
  에디터가 헤딩·이미지·링크를 article.prose 밖 형제 블록으로 렌더링하는 글이
  있어서(035 실측: `## 진행 방법`/`## 도움 받은 글`이 조용히 유실됨), 좁은
  셀렉터는 본문 일부를 소리 없이 빠뜨린다. 대신 넓은 `article.prose`는 댓글
  텍스트가 본문 뒤에 이어질 수 있다 — **조용한 유실보다 여분 포함이 낫다**는
  판단으로 넓은 쪽을 쓴다. 클립할 때 끝부분이 댓글인지 한 번 보면 된다.
- 이전 bash 버전은 응답 마크다운의 문자열 패턴("가입/로그인" 등)으로 셸을
  걸러내려다 정상 글을 오판했다. 셀렉터 방식은 그 추측 자체가 필요 없다.
- 알려진 한계: Jina의 SPA 렌더 스냅샷이 비결정적이라, 같은 요청이 시점에 따라
  헤딩·이미지·링크 블록이 빠진 부분판을 줄 때가 있다(035 실측 — x-timeout,
  x-wait-for-selector, x-no-cache 모두 무효). 클라이언트는 "완전한지"를 알 수
  없으므로 코드로 못 막는다. 출력이 원문 대비 의심스럽게 짧으면 시간을 두고
  재실행해 더 긴 쪽을 쓴다.

출력: 정제된 본문 마크다운(stdout). 이미지 참조 줄은 제거(alt 텍스트는 저자
글이 아님). 실패 시 stderr에 FETCH_FAILED + 사유, exit 1 — 실패했으면
클립을 만들지 않는 것이 규칙이다(제목만으로 지어내는 것이 최악의 결과).
"""
import json
import re
import sys
import time

import requests

SELECTOR = "article.prose"
MAX_TRIES = 5          # 015 티켓: Jina 간헐 502 + 무료 티어 429(rate limit) 재시도 여유
TIMEOUT = 60
IMAGE_LINE = re.compile(r"^!\[Image \d+.*$", re.MULTILINE)


def fail(url: str, reason: str) -> None:
    print(f"FETCH_FAILED: {url} ({reason})", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("(no url)", "usage: uv run fetch_post.py <post-url>")
    url = sys.argv[1]

    # 게시글 URL만 받는다. member 프로필 같은 페이지도 article.prose를 갖고
    # 있어서(프로필에 최근 글이 렌더링됨) 셀렉터만으로는 못 거른다.
    if "gpters.org" not in url or "/post/" not in url:
        fail(url, "not a gpters.org post URL — expected .../{section}/post/{slug}")

    last_reason = "unknown"
    for attempt in range(1, MAX_TRIES + 1):
        # Jina는 간헐적으로 렌더링에 실패한 응답을 준다. 너무 촘촘히 재시도하면
        # 같은 상태를 반복해서 맞으므로 간격을 점점 늘린다(실측: 목록 fetch가
        # 1초 간격 3연속 실패 후 수십 초 뒤 정상).
        backoff = 2 * attempt
        try:
            resp = requests.get(
                f"https://r.jina.ai/{url}",
                headers={"x-target-selector": SELECTOR},
                timeout=TIMEOUT,
            )
        except requests.RequestException as e:
            last_reason = f"request error: {e}"
            time.sleep(backoff)
            continue

        text = resp.text
        # Jina의 JSON 에러 응답은 두 부류다:
        # - 429 rate limit: 일시적. retryAfter(초)를 알려주니 그만큼 기다렸다 재시도.
        # - 422 등 no-content: 셀렉터가 페이지에 없음(삭제된 글 등). 확정 실패.
        if text.lstrip().startswith("{") and '"code"' in text[:300]:
            try:
                err = json.loads(text)
            except json.JSONDecodeError:
                err = {}
            if err.get("code") == 429:
                wait = max(float(err.get("retryAfter", 5)), backoff)
                last_reason = f"rate limited (429), waited {wait:.0f}s"
                time.sleep(wait)
                continue
            fail(url, f"jina error response (dead link or no article body): {text[:200]}")
        if resp.status_code != 200 or not text.strip():
            last_reason = f"HTTP {resp.status_code}, {len(text)} bytes"
            time.sleep(backoff)
            continue

        # 메타 헤더(Title:/URL Source:/... ) 이후의 본문만 남긴다.
        marker = "Markdown Content:"
        idx = text.find(marker)
        if idx == -1:
            last_reason = "malformed response (no 'Markdown Content:' header)"
            time.sleep(backoff)
            continue
        body = text[idx + len(marker):].strip()
        if len(body) < 200:
            last_reason = f"body too short ({len(body)} chars) — suspicious"
            time.sleep(backoff)
            continue

        body = IMAGE_LINE.sub("", body)
        body = re.sub(r"\n{3,}", "\n\n", body).strip()
        print(body)
        return

    fail(url, f"retried {MAX_TRIES}x, last: {last_reason}")


if __name__ == "__main__":
    main()
