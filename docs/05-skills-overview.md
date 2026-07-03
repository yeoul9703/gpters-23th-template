# 05 · 만들 스킬 · 에이전트 한눈에

참가자가 필요하다고 꼽은 것들을 티켓으로 만들었다. 이미 있는 건 개선/점검, 없는 건 신규.

## 스킬 (type: skill)

| 티켓 | 스킬 | 현재 | 성격 |
|---|---|---|---|
| 002 | g23-thinking-partner | 있음 | 개선 — 모호한 의도 명확화 강화 |
| 003 | g23-case-writer | `case-post-writer` 로 있음 | 개선 — 담백한 사례글 (경량) |
| 004 | g23-welcome | 없음 | 신규 — 셋업+온보딩, setup 흡수 |
| 005 | skill-creator | 없음 | 신규 — Anthropic 공식 참고 |
| 006 | g23-missions | 있음 | 점검 — 1~4주차 제공 |

## 서브에이전트 (type: agent)

| 티켓 | 에이전트 | 성격 |
|---|---|---|
| 007 | k-skill-researcher | 신규 — k-skill 레포 조사 |
| 008 | gpters-case-researcher | 신규 — 지피터스 사례 조사 |

`.claude/agents/` 는 아직 없어서 새로 만든다. 스킬이 에이전트를 부르는 구조.

## 아직 안 정한 것

- g23-setup 폐기 방식 (삭제 vs 리다이렉트)
- 조사 에이전트의 접근 방식 (로컬 클론? 로그인 벽?)
- case-post-writer → case-writer 이름 통일

→ `ticket/_discuss.md` 에 모음.
