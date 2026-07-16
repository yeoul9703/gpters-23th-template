# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""fetch_list.py <listing-or-tag-url> — 지피터스 목록/태그 페이지에서 게시글 열거.

실행:  uv run .claude/skills/gpters-clipper/scripts/fetch_list.py "<목록 URL>"
출력:  게시글마다 "제목<TAB>URL" 한 줄 (stdout).

- 목록 페이지도 JS SPA라 Jina Reader를 경유한다. 목록은 본문 셀렉터가 없어
  기본 응답을 받되, /post/ 링크만 정규식으로 추출하므로 사이트 헤더가 섞여
  있어도 결과는 오염되지 않는다.
- 무한스크롤 첫 배치(~30개)만 잡힌다 — 더 긁어오려 하지 말고 "더 있을 수
  있다"고 안내하는 것이 이 스킬의 스코프다.
- 실패 시 stderr에 FETCH_FAILED, exit 1. 후보를 지어내지 않는다.
"""
import re
import sys
import time

import requests

MAX_TRIES = 3
TIMEOUT = 60
POST_LINK = re.compile(
    r"\[([^\]]+)\]\((https://www\.gpters\.org/[a-zA-Z0-9_-]+/post/[a-zA-Z0-9_-]+)\)"
)


def fail(url: str, reason: str) -> None:
    print(f"FETCH_FAILED: {url} ({reason})", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("(no url)", "usage: uv run fetch_list.py <listing-or-tag-url>")
    url = sys.argv[1]
    if "gpters.org" not in url:
        fail(url, "not a gpters.org URL")

    last_reason = "unknown"
    for attempt in range(1, MAX_TRIES + 1):
        backoff = 2 * attempt  # 간헐 렌더링 실패 대비, 간격을 점점 늘린다
        try:
            resp = requests.get(f"https://r.jina.ai/{url}", timeout=TIMEOUT)
        except requests.RequestException as e:
            last_reason = f"request error: {e}"
            time.sleep(backoff)
            continue
        if resp.status_code != 200 or not resp.text.strip():
            last_reason = f"HTTP {resp.status_code}, {len(resp.text)} bytes"
            time.sleep(backoff)
            continue

        seen: set[str] = set()
        lines: list[str] = []
        for title, link in POST_LINK.findall(resp.text):
            if link in seen:
                continue
            seen.add(link)
            lines.append(f"{title.strip()}\t{link}")
        if not lines:
            last_reason = "response had no post links"
            time.sleep(backoff)
            continue

        print("\n".join(lines))
        return

    fail(url, f"retried {MAX_TRIES}x, last: {last_reason}")


if __name__ == "__main__":
    main()
