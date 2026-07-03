---
id: 008
title: gpters-case-researcher — 지피터스 사례 조사 서브에이전트
type: agent
status: todo
created: 2026-07-03
---

## 뭘 하려는가 (한 줄)

지피터스 "베스트 사례"·"ax" 게시판을 훑어 쓸모 있는 글을 찾아오는 서브에이전트.

## 왜 / 언제 쓰는 일인가

신규 서브에이전트. 결과는 `ticket/clips/` 에 클리핑으로 쌓이는 것과 짝.
넓게 훑고 **후보 게시글만 물어오면**, 참가자가 진짜 쓸 것만 골라 클립.

## 할 것 (체크리스트)

- [x] ~~지피터스 게시판 접근 방식 확인~~ (009 사전조사: 태그 목록 공개=WebFetch OK, 회원 프로필 로그인 벽 → _discuss C3)
- [ ] [[009-clip-gpters-writing-samples]] 첫 수동 실행 결과 보고 스펙 다듬기 (개별 글 접근 여부 포함)
- [ ] 입력(관심 주제) → 출력(게시글 3~5개: 링크·한줄 요약·왜 쓸모) 스펙
- [ ] 읽기 전용 도구만 부여
- [ ] 출력 형식을 clips/_template.md 에 맞춰 바로 클립 가능하게
- [ ] 주제 1개로 돌려보기

## 막힌 점 / 메모

- 진입점 URL: `https://www.gpters.org/ai-study-post?tag_id=Q1d120GLVF32yKbIgqFxE` (공개, 009 task.json 에 상세)
- 개별 글 본문이 막히면 claude-in-chrome 폴백 (사용자 Chrome 로그인 상태)
- 이 에이전트가 자동화할 일의 **첫 수동 실행 = [[009-clip-gpters-writing-samples]]**. 009 결과가 이 티켓의 스펙 근거.
- 관련: [[003-g23-case-writer]] 사례글 재료로 이어짐, ticket/clips 로 저장
