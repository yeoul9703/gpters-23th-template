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

### ☐ A1. g23-setup 처리 방식 (004)
흡수 후 **완전 삭제** vs "welcome 으로 가세요" **얇은 리다이렉트**만 남김.
- 고려: 기존 트리거 "초기 설정/셋업"으로 들어올 사람.
- 잠정 추천: 리다이렉트 3줄만 남기고 실질 내용은 welcome 으로.

### ☐ A2. welcome 이 흡수할 setup 범위 (004)
OS 확인 / k-skill 준비 점검 / CLAUDE.md 개인화 — 전부? 일부?

### ☐ A3. "몇 주차" 판단 방식 (006)
날짜 기준 자동 계산 vs 그냥 물어보기.
- 잠정 추천: **물어보기** (스터디 시작일 안 박혀 있으면 자동계산이 더 취약).

### ☐ A4. missions/week-*.md 4개 다 있나 (006)
없으면 뭘 채울지. → 파일 확인부터.

---

## 덩어리 B — thinking-partner + skill-creator (메타 도구)

### ☐ B1. skill-creator 축약 수준 (005)
Anthropic 공식 skill-creator 를 얼마나 덜어낼지. P1 에 따라 대폭 축약 전제.
- 먼저: 공식 원본 어디 있는지 확인 (docs vs 레포).

### ☐ B2. thinking-partner ↔ skill-creator 경계 (002/005)
어디까지 "범위 좁히기"(thinking-partner)고 어디부터 "실제 생성"(skill-creator)인가.
- 잠정: 흐릿함→또렷 = thinking-partner, 또렷한 스펙→SKILL.md = skill-creator. 핸드오프 지점 1개.

---

## 덩어리 C — researcher×2 + case-writer (조사→클립→사례)

### 🔄 C1. k-윤문 = 담백함 + 상투구 회피 (003) — 방향 잡힘, 목록 확정 남음
003 에서 `korean-humanizer` 정신만 차용하기로 정리됨.
- 피할 표현 짧은 목록(10개 안쪽)을 SKILL.md 인라인. → **최종 목록 확정 필요**.

### ☐ C2. k-skill 접근 방식 (007)
로컬 클론 vs 원격(GitHub) 조회. 경량 원칙상 원격 훑기 선호?

### ☐ C3. 지피터스 게시판 접근 (008)
"베스트 사례"·"ax" 게시판이 로그인 벽 뒤인가? → 그렇다면 claude-in-chrome 필요.
- 먼저: URL 과 로그인 여부 확인.

### ☐ C4. case-writer 이름/개선 범위 (003)
`g23-case-post-writer` 유지 vs `g23-case-writer` 개명. (P2 와 연동)

---

## 확정 로그

- 2026-07-03 P1 스킬 경량 원칙 확정 (Pro 전제)
