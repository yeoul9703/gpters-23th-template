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

### ☐ P2. 이름 규칙
- 스킬: `g23-*` 접두 유지 (예외: `skill-creator` 는 범용이라 접두 없이?) ← **결정 필요**
- 서브에이전트: 접두 없이 역할명 (`k-skill-researcher`, `gpters-case-researcher`)
- `g23-case-post-writer` → `g23-case-writer` 로 통일? ← **결정 필요 (003)**

---

## 덩어리 A — welcome + missions + setup (온보딩)

### ✅ A1. g23-setup 처리 → 삭제 + 트리거 이전 + 참조 갱신
setup **삭제**, 트리거("초기 설정/셋업/처음인데")를 welcome description 으로 이전.
리다이렉트 파일 안 만듦(P1: 빈 껍데기 금지). 참조 3곳 갱신 필요:
- 루트 `README.md` L19, L51
- `missions/week-1.md` L11
> 2026-07-03 확정.

### ✅ A2. welcome 흡수 범위 → setup §1~4 통째 + 실습 + 핸드오프
welcome 흐름: ①환경확인 ②k-skill준비 ③업무파악 ④CLAUDE.md개인화(§1~4 흡수)
→ ⑤**1주차 첫 실습**(신규) → ⑥missions 핸드오프(§5).
> 2026-07-03 확정. 단 ⑤의 성격은 A5 참조.

### ✅ A5. welcome "1주차 첫 실습" → 미니 실습 후 실제 skill 호출 (하이브리드)
(a)+(b) 순서: **작은 작업으로 즉시 성공 경험** → 거기서 멈추지 말고 **실제 skill 호출**로 이어감.
- 미니 실습은 self-contained(의존 없이 성공) → 그 다음 진짜 도구(thinking-partner→skill-creator) 호출.
- skill-creator 미완성이어도 미니 실습은 동작; 호출부는 "다음은 이 스킬로" 포인터로 degrade.
> 2026-07-03 확정.

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

### 🔄 C1. k-윤문 = 담백함 + 상투구 회피 (003) — 방향 잡힘, 목록 확정 남음
003 에서 `korean-humanizer` 정신만 차용하기로 정리됨.
- 피할 표현 짧은 목록(10개 안쪽)을 SKILL.md 인라인. → **최종 목록 확정 필요**.

### ☐ C2. k-skill 접근 방식 (007)
로컬 클론 vs 원격(GitHub) 조회. 경량 원칙상 원격 훑기 선호?

### 🔄 C3. 지피터스 게시판 접근 (008) — 절반 확인됨 (009 사전조사, 2026-07-03)
- **태그 목록 페이지 = 공개.** WebFetch 로 제목·작성자·링크 열거 가능 확인.
  (`https://www.gpters.org/ai-study-post?tag_id=...`)
- **회원 프로필 = 로그인 벽.** (`gpters.org/member/...`) → claude-in-chrome 폴백 (사용자 Chrome 로그인 상태).
- 남은 것: **개별 글 본문**이 WebFetch 로 열리는지 → [[009-clip-gpters-writing-samples]] 실행 중 확인.

### ☐ C4. case-writer 이름/개선 범위 (003)
`g23-case-post-writer` 유지 vs `g23-case-writer` 개명. (P2 와 연동)

---

## 확정 로그

- 2026-07-03 P1 스킬 경량 원칙 확정 (Pro 전제)
- 2026-07-03 C3 절반 확인 — 태그 목록 공개 / 회원 프로필 로그인 벽 (009 사전조사)
