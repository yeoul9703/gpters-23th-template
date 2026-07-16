---
name: g23-kskill-intro
description: g23-welcome 온보딩 ②단계 — k-skill 레포를 소개하고 마켓플레이스로 설치, market-kurly-search로 실제 실행까지 체험시킨다. g23-welcome이 온보딩 흐름 중에 호출한다. 단독으로도 "k-skill 설치해줘", "k-skill 체험해보고 싶어"라고 말하면 켠다. 다음에는 트리거하지 않는다 — 내 업무에 맞는 참고 사례를 찾고 싶으면(→ g23-k-skills-search).
---

# g23-kskill-intro — k-skill 소개·설치·체험

## 진행 순서

- [k-skill 레포](https://github.com/NomaDamas/k-skill)를 한 번 둘러봤는지 확인한다.
- k-skill은 Claude Code 플러그인 마켓플레이스로 설치할 수 있다. 설치를 원하면 안내한다:
  ```text
  /plugin marketplace add NomaDamas/k-skill
  ```
  이후 개별 skill은 `/k-skill:<skill-name>` 형태로 부르고, 자격증명이 필요한 skill은 `k-skill-setup`으로 설정한다.
- **실제로 하나 실행해본다.** `/k-skill:market-kurly-search`로 오늘의 마켓컬리 가격·할인을 검색해본다. 품목은 생수 / 원두커피 / 우유 / 계란 중 하나를 예시로 주되, 참가자가 원하는 다른 품목으로 바꿔 검색해도 된다. 이 스킬은 이미 완성돼 있으니 다시 조사하거나 새로 만들지 않는다 — 설치하고 그대로 실행해 결과를 확인하는 것으로 충분하다.
- 이번 스터디는 k-skill을 **그대로 쓰는 게 아니라 참고 사례로 삼아 내 것으로 바꾸는** 게 목적임을 상기시킨다.

## 하지 말 것
- k-skill 저장소를 clone하거나 로컬에 복제하지 않는다 — 마켓플레이스 설치로 충분하다.
