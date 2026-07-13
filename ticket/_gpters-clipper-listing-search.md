# gpters-clipper 확장 — 목적/범위 결정 허브

참가자가 "지피터스 ~ 관련 사례 찾아줘"처럼 주제만 던지든, URL을 직접 주든 — 태그 목록 진입부터
개별 게시물 클리핑까지 스킬 하나로 끝내는 걸 다룬다. 여러 턴에 걸친 결정 gate 논의 결과를
여기 모으고, 실제 구현은 하위 티켓으로 위임한다.

> 스킬명은 `gpters-clipper`(p 두 개, 기존 표준 철자)로 확정. 개명하지 않고 **기존 스킬을
> 그 자리에서 확장**한다 — 논의 초반 "gpters-cliper"(p 하나)로 부른 건 오타였음, 정정.

## 왜 (Intent)

- 참가자가 URL을 이미 아는 경우도 있지만, 주제만 던지는 경우도 많을 것으로 예상된다.
- 지금은 후자를 처리하려면 `gpters-case-researcher` 서브에이전트를 거쳐야 하는데, 입문자
  입장에선 서브에이전트 홉이 "무슨 일이 벌어지는지" 안 보이게 만든다.
- 목표: 메인 에이전트 하나가 (a) 주제/태그 검색 (b) URL 직접 클립 두 경로를 모두 처리한다.

## 경위 — 결정 gate에서 확인한 것 (2026-07-13)

1. **이미 있는 것 확인.** `gpters-clipper` skill(발췌+전문 로직, 클립 50개 실적, 이미 검증됨),
   `gpters-case-researcher` agent(`.claude/agents/`, 태그 목록 훑어 후보 3~5개 보고, 읽기 전용).
   "gpters-cliper"라는 신규 요청이 이 둘과 겹치는지 모른 채 들어와서, 결정 gate로 먼저 짚었다.
2. **목록 페이지 fetch 검증.** `curl -sL "https://r.jina.ai/<목록URL>"`로 태그 필터 목록
   페이지가 실제로 enumerate됨(게시물 31개, URL+제목+본문 요약까지 나옴). 반면 WebFetch
   도구로 직접 열면 다른 섹션 네비 셸만 반환됨 — `gpters-case-researcher` SKILL 설명서의
   "목록 페이지 WebFetch 가능 확인됨" 문구는 지금 기준으로 틀렸다(029에서 갱신).
3. **페이지네이션 한계.** 위 fetch는 무한스크롤 첫 배치(~31개)만 잡힌다. "더보기" 마커
   없이 로그인 전용 사이드바("내 AI스터디")로 끝남 — 태그당 게시물 전체를 확보하려면
   별도 조사(숨은 API/스크롤 시뮬레이션)가 필요하나, 이번 스코프에서는 제외한다.
4. **개별 게시물 DOM.** 실측 HTML 기준 본문은 `<article class="prose">...</article>` 안에만
   있고, 하단 태그는 태그 페이지 링크가 아니라 `/search?query=...&type=post` 검색 링크
   (badge)다. 게시물 URL 패턴은 board별로 다르다 (`/ax-lab/post/`, `/dev/post/`,
   `/nocode/post/`, `/marketing/post/`, `/media/post/`, `/wealth/post/` 등 확인됨).
5. **P1 원칙과의 충돌 확인·해소.** `_discuss.md`의 확정 원칙 P1("스킬은 가볍게, 별도
   스크립트·리소스 지양")과 처음 논의한 "scripts/+references/ 번들" 구성이 충돌했다.
   재논의 결과 P1을 그대로 따르기로 함 — 진짜 목적은 서브에이전트 spawn·무거운 절차를
   안 만드는 것이었지, 스크립트 자체가 목적이 아니었다. curl 명령은 기존 `gpters-clipper`
   처럼 SKILL.md 절차 안에 인라인으로 쓴다. 별도 scripts/references 폴더는 만들지 않는다.
6. **이름 오타 발견·정정 (cold-read 검토 1사이클).** 결정 gate 대화 내내 "gpters-cliper"
   (p 하나)로 불렀는데, 실제 기존 스킬은 `gpters-clipper`(p 두 개)다. 개명이 아니라
   오타였음을 확인 — **스킬명은 그대로 `gpters-clipper` 유지, 디렉터리/개명 작업 불필요.**

## 결정 (Architecture)

- **단일 skill, 서브에이전트 spawn 없음.** `gpters-case-researcher` agent는 **보류** —
  삭제하지 않되 활성 플로우에서 제외한다.
- **`gpters-clipper`를 그 자리에서 확장.** 개명하지 않는다. 기존 발췌+전문 로직은 그대로
  유지, 앞단에 "목록/태그 검색" 진입 경로를 추가한다.
- **두 가지 트리거 흐름을 한 SKILL.md가 처리:**
  - (a) 주제/태그만 줌("~ 관련 사례 찾아줘") → 목록 페이지 curl+jina로 enumerate →
    후보 나열 → 사람 확인 → 확정된 것만 클립
  - (b) URL을 이미 앎("이 글 클립해줘") → 목록 단계 생략, 바로 기존 클립 절차
- **인라인 curl, 별도 scripts/references 폴더 없음** (P1 준수).

## 스코프 밖 (보류)

- 태그당 게시물 전체(무한스크롤 첫 배치 이상) 확보 — 별도 조사 필요, 이번엔 안 함.
- 사람 확인 생략하는 자동 대량 클립 모드 — 1차는 항상 확인 거침.

## 하위 티켓 — 둘 다 done (task 030, 2026-07-13, worktree 구현)

- [`028-gpters-clipper-listing-search.md`](028-gpters-clipper-listing-search.md) —
  `gpters-clipper`에 목록/태그 검색 진입 경로 추가 (개명 없음)
- [`029-case-researcher-hold.md`](029-case-researcher-hold.md) — gpters-case-researcher
  agent 보류 처리 + 참조 문서 갱신

## 막힌 점 / 메모

- 관련: [[008-agent-gpters-case-researcher]], [[024-clip-verbatim-excerpts]],
  [[026-clip-full-body-text]] (흡수·보류 대상들의 원 배경)
