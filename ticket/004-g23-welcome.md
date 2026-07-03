---
id: 004
title: g23-welcome — 첫날 셋업 + 미니 실습 + 온보딩 (setup 흡수)
type: skill
status: todo
created: 2026-07-03
---

## 뭘 하려는가 (한 줄)

처음 온 참가자가 켜면, 셋업부터 "첫 성공 경험"까지 손잡고 끌어주는 온보딩 skill.

## 왜 / 언제 쓰는 일인가

신규 skill. 기존 `g23-setup` 을 **흡수·대체**하고, 매주 반복인 missions 로 **핸드오프**.
P1(경량) 준수: SKILL.md 한 장, 대화형, 파일 통독 없음.

트리거(= setup 트리거 이전): "스터디 시작", "초기 설정", "셋업", "처음인데 뭐부터", "온보딩"

## 확정된 설계 (덩어리 A)

welcome 흐름 — setup §1~4 흡수 + 미니 실습 + 핸드오프:
1. **환경 확인** — OS(macOS/Win), Claude Code 실행, 경험 수준 (setup §1)
2. **k-skill 준비** — 마켓플레이스 안내, "참고 사례로 삼는다" 상기 (setup §2)
3. **업무 파악 3문** — 직무 / 반복작업 3 / 해보고 싶은 것 1 (setup §3)
4. **CLAUDE.md 개인화 초안 제안** — 자동수정 금지, 제안만 (setup §4)
5. **미니 실습 (A5, 신규)** — 작은 작업으로 그 자리서 즉시 성공 경험 →
   멈추지 말고 **실제 skill 호출**(thinking-partner→skill-creator)로 이어감.
   · skill-creator 미완이면 "다음은 이 스킬로" 포인터로 degrade.
6. **missions 핸드오프** — "이번 주 미션 알려줘" → g23-missions 1주차 (setup §5)

## 할 것 (체크리스트)

- [ ] `.claude/skills/g23-welcome/SKILL.md` 작성 (위 6단계, setup §1~4 재사용)
- [ ] 미니 실습(5단계) 구체화: "5줄 skill 하나 같이 만들기" 같은 최소 작업 1개 정하기
- [ ] setup 삭제: `.claude/skills/g23-setup/` 제거
- [ ] 참조 3곳 welcome 으로 갱신: 루트 README.md(L19,L51), missions/week-1.md(L11)
- [ ] "처음 온 척" 한 번 돌려보기 (셋업→미니실습→missions 안내까지)

## 막힌 점 / 메모

- 미니 실습이 skill-creator 를 부르므로 순서상 [[005-skill-creator]] 와 맞물림 (없어도 degrade)
- 관련: [[006-g23-missions]] 로 핸드오프
