---
id: 033
title: missions/ 폴더를 g23-missions/reference/로 이동
type: skill
status: done
created: 2026-07-14
---

## 뭘 하려는가 (한 줄)

루트의 `missions/week-1~4.md`를 `.claude/skills/g23-missions/reference/week-1~4.md`로 옮기고,
README/CLAUDE.md의 관련 문구를 g23-missions 스킬 경유 안내로 정리한다.

## 왜 / 언제 쓰는 일인가

세션 중 질문("왜 missions/를 g23-missions 하위 reference로 안 두고 루트에 뒀나")에서 시작.
1차로 "사람이 직접 열어볼 수도 있는 콘텐츠라 루트가 맞다"는 근거를 냈으나, 사용자가 반박:

- `missions/`는 g23-missions 스킬 외에 관여되는 곳이 없다 — 다른 스킬이 참조하지 않는다
  (`examples/`는 g23-missions·g23-case-writer 양쪽이 참조해 공유 폴더로 남을 근거가 있지만, missions/는 다름).
- 온보딩 설계 자체가 "`/g23-missions`를 통해 미션을 확인하라"는 흐름이라, 참가자가 `missions/` 폴더를
  직접 열어보는 경로를 애초에 유도하지 않는다. "사람이 직접 본다"는 근거가 실제 UX와 안 맞음.

→ 루트에 남아 있을 이유가 빈약하다고 판단, 이동 확정.

## 참고: reference/ 관례와의 차이

이 레포에서 `reference/`는 지금까지 "평소엔 안 읽는 온디맨드 문서"라는 뜻으로 써왔다
(`g23-welcome/reference/setup-guide.md`, `g23-missions/reference/official-curriculum.md` 모두
"평소 안내에는 읽지 않는다"는 문구가 붙어 있음, [[025-welcome-setup-reference]]).

`week-N.md`는 반대로 g23-missions가 켜질 때마다 **매번** 읽는 본체 콘텐츠라 이 관례와 결이 다르다.
같은 `reference/` 폴더 안에 두되, SKILL.md에 "이 둘은 다르다"는 것을 명시적으로 구분해 적어
"reference = 안 읽는 것"이라는 다른 스킬들의 관례가 헷갈리지 않게 한다.

## 할 것 (체크리스트)

- [x] `missions/week-{1,2,3,4}.md` → `.claude/skills/g23-missions/reference/week-{1,2,3,4}.md` (git mv)
- [x] `g23-missions/SKILL.md`: 경로 갱신 + week-N.md(매번 읽음) vs official-curriculum.md(온디맨드) 구분 명시
- [x] `README.md`: "폴더 구조" 트리에서 `missions/` 제거, "시작하기 3단계"의 `missions/` 언급을 스킬 경유 문구로 수정
- [x] `CLAUDE.md`: "폴더 구조" 목록에서 `missions/week-*.md` 항목 갱신
- [x] 빈 `missions/` 폴더 정리
- [x] `ticket/README.md` 인덱스에 반영

## 막힌 점 / 메모

- 과거 티켓(004/006/016~020)들이 `missions/week-N.md` 경로를 언급하지만, 이건 완료된 히스토리 기록이라
  건드리지 않는다 — 새 경로는 이 티켓과 그 이후 문서에만 반영.
- 관련: [[025-welcome-setup-reference]] (동일 패턴의 선례 — reference/ 온디맨드 문서 분리).
