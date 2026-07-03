---
title: Claude Code 훅으로 옵시디언 업무 일지 자동화하기
source: https://www.gpters.org/marketing/post/automating-obsidian-journal-claude-i9e2rmnCGFxrVlt
category: best
clipped: 2026-07-03
tags: [claude-code, hooks, obsidian, 업무일지, 자동화]
---

## 왜 클립했나 (한 줄)

세션 종료 훅으로 "오늘 뭐 했지"를 자동 기록하는 구성 — 스터디의 skill 사용 기록 자동화에 바로 이식 가능한 아이디어.

## 핵심 요약

- Claude Code 세션이 끝날 때 훅이 돌아 당일 작업을 옵시디언에 자동 분류·저장, 터미널·파일에 흩어진 기록을 한 곳으로 통합.
- Marketing/Product 범주 자동 분류 + 재사용 가치 있는 것만 별도 '메모리'에 저장하는 고도화까지.
- 시행착오: 매 응답 훅→세션 종료 훅으로 변경, Linear 데이터 처리량 초과→파일 분할, 폴더 제약→절대경로로 해결.

## 내 업무에 어떻게 쓸까

참가자의 skill-log 작성 부담을 줄이는 "세션 종료 시 자동 기록" 패턴으로 응용. 단, 로컬 설정(hooks)은 참가자가 직접 넣게 안내하는 원칙 유지.

## 글쓰기에서 훔칠 점

- "to-do는 Linear에 있고, 정작 '오늘 뭐 했지'는 흩어져 있었어요" — 도구 이름을 박은 구체적 문제 제시 도입.
- 1단계→2단계→3단계 개선 서사로 시행착오를 성장기처럼 배치.
- "손으로 적는 게 거의 없어졌습니다!" 한 문장으로 성과를 체감시키는 마무리.
