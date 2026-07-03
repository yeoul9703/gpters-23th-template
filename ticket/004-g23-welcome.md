---
id: 004
title: g23-welcome — 첫날 셋업 + 1주차 온보딩 실습 (setup 흡수)
type: skill
status: todo
created: 2026-07-03
---

## 뭘 하려는가 (한 줄)

처음 온 참가자가 켜면, 셋업부터 1주차 실습까지 손잡고 끌어주는 온보딩 skill.

## 왜 / 언제 쓰는 일인가

신규 skill. 기존 `g23-setup`(OS 확인·k-skill 준비·CLAUDE.md 개인화)을 **흡수**하고,
바로 1주차 온보딩 실습으로 이어짐. 매주 반복인 missions 와는 분리 —
welcome 은 1주차에서 missions 를 **안내(핸드오프)** 만 함.

트리거: "스터디 시작", "처음인데", "셋업", "온보딩"

## 할 것 (체크리스트)

- [ ] 기존 g23-setup SKILL.md 읽고 재사용할 부분 추림
- [ ] welcome 흐름 설계: ① 셋업 점검 → ② CLAUDE.md 개인화 → ③ 1주차 실습 1개 → ④ missions 안내
- [ ] `.claude/skills/g23-welcome/SKILL.md` 작성
- [ ] g23-setup 폐기: SKILL.md 에 "g23-welcome 으로 이동" 안내만 남기거나 삭제
- [ ] 처음 온 척 한 번 돌려보기

## 막힌 점 / 메모

- setup 삭제 vs 얇은 리다이렉트 남기기 — 참가자와 결정 (기존 트리거 "초기 설정" 유입 고려)
- 관련: [[006-g23-missions]] 로 핸드오프
