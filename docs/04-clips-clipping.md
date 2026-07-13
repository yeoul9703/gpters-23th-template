# 04 · clips — 지피터스 사례 클리핑

## 아이디어

지피터스 **"베스트 사례"·"ax" 사례** 중 진짜 쓸모 있는 게시글을 모아두고 싶다는 요청에서 출발.
많이 모으는 게 목적이 아니라, 나중에 내 스킬·업무에 써먹을 것만.

## 위치

`ticket/clips/` — 티켓(할 일)과 구분되는 "나중에 볼 자료".

## 클립 양식 (`clips/_template.md`)

```yaml
---
title: <게시글 제목>
source: <지피터스 링크>
category: best      # best | ax
clipped: 2026-07-03
tags: []
---
```

세 줄만 있어도 충분: **왜 클립했나 / 핵심 요약 / 내 업무에 어떻게.**

## 연결

- `gpters-clipper` 스킬이 목록/태그 검색(주제만 줘도 후보를 찾아줌)부터 발췌+전문 클립까지 한 번에 처리 → clips 로 저장 ([10](10-next-steps.md)). 서브에이전트 `gpters-case-researcher` 가 후보를 물어오던 방식은 보류됨(2026-07-13, [08](08-case-writer-research.md)).
- 클립이 사례글 재료가 됨 → `g23-case-writer` ([09](09-case-writer-intent.md))
