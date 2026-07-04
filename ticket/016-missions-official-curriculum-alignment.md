---
id: 016
title: missions/week-*.md를 gpters.org 공식 커리큘럼에 맞춘다 (인덱스)
type: mission      # skill | mission | fix
status: done       # todo | doing | done
created: 2026-07-04
---

## 뭘 하려는가 (한 줄)

`missions/week-1~4.md`가 gpters.org에 이미 공개된 "23기 K스킬자동화" 스터디 페이지의 주차별 목표·과제와 어긋나지 않게 맞춘다.
이 티켓은 실제 체크리스트를 들고 있지 않는 **인덱스**다 — 작업은 아래 자식 티켓 4개로 쪼갰다 (여러 세션이 주제 하나씩 논의할 수 있도록).

## 왜 / 언제 쓰는 일인가

스터디 공식 소개 페이지([링크](https://www.gpters.org/ai-study-list/post/babbeun-silmujareul-wihan-oneul-baeweo-naeil-sseomeogneun-k-seukil-4HGbQhiSgpP2S2E))가 이미 참가자에게 노출되는 약속이다.
`missions/week-*.md`는 Claude Code 세션 안에서 그 약속을 실제로 이행하는 실행 스크립트 역할 — 두 문서가 다른 말을 하면 참가자가 헷갈린다.

## 자식 티켓 (실행 큐)

| 순서 | 티켓 | 내용 | 상태 |
|---|---|---|---|
| 1 | [[017-week2-curriculum-alignment]] | week-2.md 목표 톤 + 사례 게시글 발행 단계 | done |
| 2 | [[018-week3-curriculum-alignment]] | week-3.md 과제 보강 | done |
| 3 | [[019-week4-curriculum-alignment]] | week-4.md 스터디장 세션 안내 | done |
| 4 | [[020-cross-week-examples-and-tags]] | 4주 전체 예시 다양화 + 태그 스윕 (017~019 끝난 뒤 마지막) | done (예시 다양화는 사용자 반려로 스킵, 태그 스윕만 확인) |

017~019는 서로 파일이 겹치지 않아 순서 무관하게 병렬로 논의 가능. 020은 나머지가 정리된 뒤 마지막에.

## 완료 기준

017~020이 전부 `done`이면 이 인덱스 티켓도 `done`으로 바꾼다.

## 이미 끝난 것 (분리 전 진행분)

- [x] 공식 페이지 원문 확보 (Jina Reader 경유 — WebFetch 직접 호출은 렌더링된 본문을 못 가져옴)
- [x] `.claude/skills/g23-missions/reference/official-curriculum.md`에 스냅샷 저장 (원문 요지 + 표) — 자식 티켓들이 여기를 근거로 참조
- [x] week-1.md: 순서에 `skill-creator`·`g23-case-writer` 명시, 사례 게시글 발행 단계 반영
- [x] 태그 표기: `23기 [스터디]` 같은 대괄호 placeholder 대신 실제 이름을 예시로 보여주는 형식(`23기 K스킬자동화`(예시))으로 확정 (2026-07-04) — week-1.md·g23-case-writer에 반영 완료. 나머지 파일 스윕은 020에서.

## 막힌 점 / 메모

- reference 폴더 위치는 `.claude/skills/g23-missions/reference/` — g23-missions SKILL.md는 이걸 매 세션 읽지 않는다(P1 경량 원칙). 주차 내용을 고치거나 근거를 재확인할 때만 참고하는 포인터로 연결.
- 참고: [[015-clip-blank-body-diagnosis]] 때처럼 gpters.org 본문은 WebFetch 직접 호출로는 제대로 안 나오고 `https://r.jina.ai/<url>` 경유가 안정적이었다.
