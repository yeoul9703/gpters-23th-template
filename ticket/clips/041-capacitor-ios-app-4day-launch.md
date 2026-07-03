---
title: Claude Code로 웹앱을 iOS 앱으로 — Capacitor + App Store 심사 4일 출시기
source: https://www.gpters.org/dev/post/web-app-ios-app-jxEFcC59zQYbtyK
category: best
clipped: 2026-07-03
tags: [claude-code, capacitor, ios, app-store, nextjs]
---

## 왜 클립했나 (한 줄)

웹앱→네이티브 앱 전환을 "4일"이라는 짧은 타임라인으로 끝낸 실전 기록 — 스터디 참가자에게 "작게 빨리"의 좋은 예시.

## 핵심 요약

- Next.js 웹앱 '모닝카페'(서울 카페 9,514개 지도)를 Capacitor 7로 감싸 iOS 앱으로 전환, Claude Code로 코드 작성부터 App Store 출시까지 4일 완료.
- 로컬 알림 추가, 네이티브/웹 분기 처리, Safe Area 대응을 진행했고 Privacy Manifest·위치 권한으로 2번 리젝 후 통과.
- WebView 빈 화면(CSP/캐시), Safe Area 겹침, 스플래시 타이밍 이슈는 증상을 Claude Code에 전달해 해결.

## 내 업무에 어떻게 쓸까

기존 결과물(웹앱)을 다른 플랫폼으로 확장할 때 "증상을 그대로 AI에 전달 → 해결책 받기" 루프를 따라 하기. 리젝 사유까지 기록하는 방식도 skill 사용 기록 양식에 반영할 만함.

## 글쓰기에서 훔칠 점

- "2주 전에 공유했는데 반응이 좋아서 앱까지 만들었습니다" — 이전 글과 연결하는 연재형 도입.
- "리젝 2번 받았습니다" 같은 실패를 숫자로 담백하게 노출해 신뢰를 얻는 방식.
- 9,514개, 4일 등 정확한 수치로 문장에 무게를 싣는 습관.
