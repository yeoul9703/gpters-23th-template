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

- 서브에이전트 `gpters-case-researcher` 가 후보 글을 물어오면 → clips 로 저장 ([08](08-case-writer-research.md), [10](10-next-steps.md))
- 클립이 사례글 재료가 됨 → `g23-case-writer` ([09](09-case-writer-intent.md))
