---
id: 008
title: gpters-case-researcher — 지피터스 사례 조사 서브에이전트
type: agent
status: done
created: 2026-07-03
done: 2026-07-03
---

## 뭘 하려는가 (한 줄)

지피터스 "베스트 사례"·"ax" 게시판을 훑어 쓸모 있는 글을 찾아오는 서브에이전트.

## 왜 / 언제 쓰는 일인가

신규 서브에이전트. 결과는 `ticket/clips/` 에 클리핑으로 쌓이는 것과 짝.
넓게 훑고 **후보 게시글만 물어오면**, 참가자가 진짜 쓸 것만 골라 클립.

## 할 것 (체크리스트)

- [x] ~~지피터스 게시판 접근 방식 확인~~ (009 사전조사: 태그 목록 공개=WebFetch OK, 회원 프로필 로그인 벽 → _discuss C3)
- [x] [[009-clip-gpters-writing-samples]] 첫 수동 실행 결과 보고 스펙 다듬기 (개별 글 접근 여부는 012 시험에서 확인: 본문도 WebFetch 로 열림 → C3 ✅. 009 본 실행에서 예외 글 나오면 그때 스펙 보강)
- [x] 입력(관심 주제) → 출력(게시글 3~5개: 링크·한줄 요약·왜 쓸모) 스펙 → `.claude/agents/gpters-case-researcher.md` 에 명시
- [x] 읽기 전용 도구만 부여 (`tools: WebFetch, WebSearch, Read, Grep, Glob` — 로그인 벽 우회 없음, chrome 폴백은 메인 세션 몫)
- [x] 출력 형식을 clips/_template.md 에 맞춰 바로 클립 가능하게 (title/source/category/tags 필드 그대로)
- [x] 주제 1개로 돌려보기 (아래 시험 기록)

## 시험 실행 기록 (2026-07-03, task 012)

- 입력: **"자동화 후기"**. 에이전트 정의대로 시뮬레이션: 공개 태그 페이지 fetch → 글 8개 열거(제목·작성자·URL) → 후보 본문 1개 WebFetch 시도.
- **개별 글 본문 = 로그인 없이 열림** 확인 ("나는 검토만 했는데, AI가 재무 자동화를 끝냈다" `/nocode/post/just-reviewed-ai-has-qTGBvmRtrWmriEb` — 본문 전체 공개, 요약 추출 성공). → C3 나머지 해소.
- 출력 형태 확인: title/source/category/tags + 한줄 요약 + 클립 가치 + 본문 접근 표시 → clips/_template.md 에 바로 옮길 수 있는 형태. 본문 통째 반환 없음.

## 막힌 점 / 메모

- 진입점 URL: `https://www.gpters.org/ai-study-post?tag_id=Q1d120GLVF32yKbIgqFxE` (공개, 009 task.json 에 상세)
- 개별 글 본문도 WebFetch 로 열림 (012 시험 확인). 회원 프로필(`gpters.org/member/...`)만 로그인 벽 → 그 경우 claude-in-chrome 폴백 (메인 세션에서)
- 이 에이전트가 자동화할 일의 **첫 수동 실행 = [[009-clip-gpters-writing-samples]]**. 009 본 실행 결과로 스펙 추가 보강 가능.
- 관련: [[003-g23-case-writer]] 사례글 재료로 이어짐, ticket/clips 로 저장
