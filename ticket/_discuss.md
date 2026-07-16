# 논의 허브 — 결정할 것들

티켓 전반에 걸친 **열린 결정**을 여기 모은다. 정해지면 → 해당 티켓에 반영하고 여기선 ✅ 로 옮긴다.
(티켓 하나 안에서만 끝나는 사소한 건 그 티켓 "막힌 점"에 두고, 여기엔 **여러 티켓에 걸리거나 방향을 가르는 것**만.)

---

## 공통 원칙 (전 티켓 적용)

### ✅ P1. 스킬은 가볍게 (Pro 요금제 전제)
참가자 대부분 Claude **Pro** → 토큰·복잡도 최소화.
- SKILL.md **한 장**으로 끝낸다. 별도 리소스 파일·스크립트 지양.
- ❌ 큰 파일 통독, ❌ 다에이전트 게이트, ❌ Python 검증, ❌ 무거운 코퍼스/채점
- 서브에이전트도 "넓게 훑고 후보만 물어오기" 수준으로 얇게.
> 출처: 003 티켓 정리 중 확정. CLAUDE.md "큰 파일 통째로 읽지 말 것"과 같은 결.

### ✅ P2. 이름 규칙
- 스킬: `g23-*` 접두 유지. 예외: `skill-creator` 는 범용이라 **접두 없이** 확정.
- 서브에이전트: 접두 없이 역할명 (`k-skill-researcher`, `gpters-case-researcher`)
- `g23-case-post-writer` → **`g23-case-writer` 개명 확정** (C4 와 함께).
> 2026-07-03 확정.

---

## 덩어리 A — welcome + missions + setup (온보딩)

### ⚠️ A1. g23-setup 처리 → 삭제 + 트리거 이전 + 참조 갱신 (2026-07-14 부분 뒤집힘)
setup **삭제**, 트리거("초기 설정/셋업/처음인데")를 welcome description 으로 이전.
리다이렉트 파일 안 만듦(P1: 빈 껍데기 금지). 참조 3곳 갱신 필요:
- 루트 `README.md` L19, L51
- `missions/week-1.md` L11
> 2026-07-03 확정.
> **2026-07-14 재검토(031) — g23-setup을 독립 스킬로 재신설.** 025에서 한 번 더 기각됐던
> "빈 껍데기" 안이지만, 이번엔 **역할이 다름**(OS/Python 안내 문서가 아니라 로컬 git
> 재초기화·CLAUDE.md 최소 정체성 기록이라는 실행 작업)이라 사용자가 재확정. 재발 방지 조건:
> description 트리거를 action-phrased("프로젝트 초기화", "초기 스캐폴드 실행")로 한정해
> welcome의 세션 시작 트리거와 절대 안 겹치게 함 — A1이 지운 중복은 유지. 상세: [[031-g23-setup-scaffold]].

### ✅ A2. welcome 흡수 범위 → setup §1~4 통째 + 실습 + 핸드오프
welcome 흐름: ①환경확인 ②k-skill준비 ③업무파악 ④CLAUDE.md개인화(§1~4 흡수)
→ ⑤**1주차 첫 실습**(신규) → ⑥missions 핸드오프(§5).
> 2026-07-03 확정. 단 ⑤의 성격은 A5 참조.

### ✅ A5. welcome "1주차 첫 실습" → 미니 실습 후 실제 skill 호출 (하이브리드)
(a)+(b) 순서: **작은 작업으로 즉시 성공 경험** → 거기서 멈추지 말고 **실제 skill 호출**로 이어감.
- 미니 실습은 self-contained(의존 없이 성공) → 그 다음 진짜 도구(thinking-partner→skill-creator) 호출.
- skill-creator 미완성이어도 미니 실습은 동작; 호출부는 "다음은 이 스킬로" 포인터로 degrade.
> 2026-07-03 확정.

### ✅ A6. welcome ⑤ 미니 실습 재정비 → 교체 아닌 추가, ② k-skill 체험 신설
07-04 안(027 최초 결정: 커스텀 예시를 실제 k-skill로 **교체**)을 재검토해 뒤집음.
전체 흐름 재확인: `invoke → 스킬 선언 → (구 setup 흡수) → 1주차 OT용 k-skill 체험 + 만든 skill 체험 → g23-case-writer 발간 안내`.
k-skill 체험과 만든 skill 체험이 **둘 다** 있어야 완성 — 교체하면 후자가 사라져 흐름과 어긋남.
- ⑤ 커스텀 미니 실습(021, 하루 세 시점 예시)은 **유지**. 대신 **②** k-skill 준비에 "실제 k-skill 하나 실행해보기" task 신설.
- 전체 온보딩 예산 **~50분** (① 셋업부터 ⑤ 실습까지 포함).
- "하루 세 시점"은 필수 구조 아님 — 스터디장 예시·팁 수준. 본질은 실무자 반복 업무 자동화 경험.
- `k-skill-researcher`는 지금 그대로 충분(README 기반 가벼운 조사) — 호출 시 역할 한 줄 설명만 곁들임.
> 2026-07-14 확정 (welcome 스킬 점검 브랜치). 상세 체크리스트는 [[027-welcome-mini-practice-clear-output]].

### ✅ A7. welcome 오케스트레이터 재설계 → ②~⑥ 전부 분리 (032)
032에서 검토하던 "welcome을 절차대로 스킬 호출하는 오케스트레이터로 바꿀지"를 확정.
동기는 **구조 정리**(재사용/독립 호출 목적 아님) — welcome SKILL.md 한 장이 길어져 유지보수하기 부담스러움.
- ①은 인라인 유지(환경 확인 + 조건부 g23-setup 호출), ②~⑥은 각각 `g23-kskill-intro`·`g23-work-discovery`·`g23-personalize`·`g23-mini-practice`·`g23-missions-handoff`로 분리.
- advisor가 짚은 두 위험을 사용자가 인지한 채로 감수: **⑥은 사실상 한 문장짜리 빈 껍데기**(025가 두 번 반려한 패턴), **③은 g23-thinking-partner와 트리거 충돌 소지**(description에 "온보딩 밖에서는 트리거하지 않는다" 배제 문구로 완화).
- P1("스킬은 가볍게")보다 "구조 정리" 동기를 우선한 명시적 예외 — 향후 유사 분리 요청의 선례.
> 2026-07-14 확정. 상세: [[032-welcome-orchestrator-reconsider]].

### ✅ A3. "몇 주차" 판단 → 물어보기 (이미 구현됨)
missions 가 이미 "몇 주차인가요? 처음이면 1주차부터" 물음. 날짜 자동계산 안 씀. 변경 없음.

### ✅ A4. week-*.md → 4개 다 있음
week-1~4.md 존재. missions 는 한 주차만 읽음(P1 부합). 가벼운 점검만.

---

## 덩어리 B — thinking-partner + skill-creator (메타 도구)

### ✅ B1. skill-creator 축약 → 대폭 경량 (평가·loop 제외)
다른 세션에서 진행 중. 공식 `skill-creator` 를 기준으로만 삼고
평가(eval)·description 최적화 루프·서브에이전트 병렬 등 고급은 전부 제외,
"3문 인터뷰 → SKILL.md 한 장" 수준. 상세는 [[005-skill-creator]].
> 2026-07-03 확정.

### ✅ B2. thinking-partner ↔ skill-creator 경계 → 명확화 vs 생성
- **thinking-partner**: 흐릿함 → 또렷한 미니 스펙(뭘·트리거·15분 범위). 명확화·범위 담당.
- **skill-creator**: 또렷한 스펙 → SKILL.md 한 장. 생성 담당. (005 step1 = 흐릿하면 thinking-partner 로)
- 핸드오프 지점 1개. 양쪽 문구 맞추기 남음.
- thinking-partner 레퍼런스: vmc `grilling`(한질문+추천답), Rhim80 `thinking-partner`(가정 짚기·요약).
  노트 워크스페이스 탐색·무한 grilling 은 P1 로 덜어냄.
> 2026-07-03 확정. 상세 [[002-g23-thinking-partner]].

---

## 덩어리 C — researcher×2 + case-writer (조사→클립→사례)

### ✅ C1. k-윤문 = 담백함 + 상투구 회피 (003) → 목록 9개 확정
003 에서 `korean-humanizer` 정신만 차용하기로 정리됨.
- 상투구 최종 목록 **9개 확정** (003 예시 + `_style-reference.md` §3 병합) — SKILL.md 인라인, 전문은 [[003-g23-case-writer]] 'C1 확정' 절.
> 2026-07-03 확정 (task 013).

### ✅ C2. k-skill 접근 방식 (007) → 원격 조회
GitHub API·WebFetch 로 필요한 파일만 원격에서 훑는다. 클론 관리 부담 없음, P1 부합.
> 2026-07-03 확정.

### ✅ C3. 지피터스 게시판 접근 (008) → 전부 확인됨
- **태그 목록 페이지 = 공개.** ~~WebFetch 로 제목·작성자·링크 열거 가능 확인.~~ (009 사전조사)
  (`https://www.gpters.org/ai-study-post?tag_id=...`)
  > **2026-07-13 재검증(gpters-clipper 목록 검색 결정 gate) — WebFetch 직접 호출은 실패로
  > 재현됨**(다른 섹션 네비 셸만 반환). 대신 `curl -sL "https://r.jina.ai/<목록URL>"` 경유는
  > 게시물 31개까지 정상 enumerate됨. 사이트가 그 사이 바뀌었는지, 009 당시 다른 조건이었는지는
  > 불명 — **지금 기준으로는 목록 페이지 fetch에 WebFetch 대신 jina reader를 쓴다.**
  > 자세한 내용: [`_gpters-clipper-listing-search.md`](_gpters-clipper-listing-search.md) 경위 2.
- **개별 글 본문 = 공개.** WebFetch 로 본문 열람·요약 가능 확인 (`/nocode/post/...` 샘플 1건, task 012 시험 실행).
- **회원 프로필 = 로그인 벽.** (`gpters.org/member/...`) → claude-in-chrome 폴백 (사용자 Chrome 로그인 상태, 메인 세션에서).
> 2026-07-03 확인 완료 (사전조사 009 + 시험 012). 009 본 실행에서 예외 글 나오면 008 티켓 메모로.
> 태그 목록 페이지의 WebFetch 가능 여부는 2026-07-13 재검증으로 정정됨(위 참고).

### ✅ C4. case-writer 이름 → `g23-case-writer` 개명 확정
(P2 와 함께 확정. 실행은 [[013-case-writer.task.json|task 013]] 에서.)
> 2026-07-03 확정. task 013 에서 반영 완료 — 디렉터리 개명 + README/week-4/g23-missions 참조 갱신.

---

## 확정 로그

- 2026-07-03 P1 스킬 경량 원칙 확정 (Pro 전제)
- 2026-07-03 C3 절반 확인 — 태그 목록 공개 / 회원 프로필 로그인 벽 (009 사전조사)
- 2026-07-03 P2 이름 규칙 확정 — skill-creator 무접두, g23-case-writer 개명 (C4 포함)
- 2026-07-03 C2 확정 — k-skill 원격 조회
- 2026-07-03 실행 위임 체계 문서화 — task 010~013 + `_runplan.md` (남은 열린 결정: C1 상투구 목록 → task 013 에서 확정, C3 나머지 → 009/012 에서 확인)
- 2026-07-03 C3 완결 — 개별 글 본문도 WebFetch 공개 확인 (task 012 시험 실행)
- 2026-07-03 C1 완결 — 상투구 목록 9개 확정 + C4 개명 반영 (task 013). 덩어리 C 열린 결정 전부 소진.
- 2026-07-14 A6 확정 — welcome ⑤ 미니 실습 재정비: 07-04 "교체" 안 뒤집고 "추가"로 정리, ② k-skill 체험 신설 + 전체 온보딩 50분 예산 명시 (027 재검토, welcome 스킬 점검 브랜치)
- 2026-07-14 027 완료 + 023 삭제 — welcome ⑤ 성공 정의를 산출물 확인까지 강화, ② `market-kurly-search` 실행 체험 신설. 이 ② 후보 조건(자격증명/API 키 불필요 등)이 023이 요구하던 "1주차 k-skill 환경 무관 필터"를 사실상 충족해 023 티켓은 삭제(사용자 결정) — 근거는 027, 삭제 기록만 README에 남김.
- 2026-07-14 A7 확정 — welcome을 오케스트레이터로 재설계, ②~⑥ skill 5개 분리(032). 동기는 구조 정리, ⑥ 빈 껍데기·③ 트리거 충돌 위험은 사용자가 인지하고 감수.
