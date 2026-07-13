---
id: 029
title: gpters-case-researcher agent 보류 처리
type: fix          # skill | mission | fix
status: done       # todo | doing | done
created: 2026-07-13
done: 2026-07-13
---

## 뭘 하려는가 (한 줄)

`.claude/agents/gpters-case-researcher.md`를 삭제하지 않고 보류 상태로 표시해, 028의
목록/태그 검색 진입 경로가 활성화된 뒤에도 참가자·향후 세션이 헷갈리지 않게 한다.

## 왜 / 언제 쓰는 일인가

028에서 태그/주제 검색 기능이 `gpters-clipper` skill로 흡수되면 `gpters-case-researcher`는
더 이상 활성 플로우가 아니다. 그렇다고 지금 지우면 이 agent가 만들어진 배경(007/008/012
티켓)과 "왜 있다가 안 쓰는지" 맥락이 날아간다 — 보류로 남겨 나중에 서브에이전트 분리가
다시 필요해지면(예: 대량 백필 작업, 토큰 절약이 중요한 대규모 조사) 참고할 수 있게 한다.

## 할 것 (체크리스트)

- [x] `.claude/agents/gpters-case-researcher.md` 파일 상단에 보류 안내 추가
      ("⚠️ 보류 (2026-07-13) — 이 역할은 `gpters-clipper` skill로 흡수됨. 이 파일은
      참고용으로만 남김.")
- [x] `.claude/agents/gpters-case-researcher.md`(에이전트 파일, SKILL.md 아님) 1번 항목의
      "공개 태그 목록 페이지부터 훑는다 (WebFetch 가능 확인됨)" 문구를 정정 — 실측 결과
      목록 페이지는 WebFetch로 안 열리고 `curl+r.jina.ai`로만 열림
      ([[_gpters-clipper-listing-search]] 경위 2번 참고).
- [x] `description` frontmatter를 "⚠️ 보류 — 활성 트리거 없음. 역할은 `gpters-clipper`
      skill로 흡수됨. 참고용으로만 남김." 으로 교체해 메인 에이전트가 자동으로 이 agent를
      spawn하지 않게 한다 (트리거 예시 문구는 전부 제거, 역할 설명 한 줄만 남김).
- [x] `.claude/skills/gpters-clipper/SKILL.md`의 "관련" 섹션에서 gpters-case-researcher를
      "후보 조사 전담"으로 설명하는 줄을 갱신 — 그 역할은 이제 gpters-clipper 자신의
      목록/태그 검색 단계(028)로 흡수됐다는 점을 반영한다.
- [x] `docs/10-next-steps.md`, `ticket/README.md`의 관계 지도에서 `gpters-case-researcher`
      를 "보류"로 표시한다.
- [x] `docs/04-clips-clipping.md`의 `## 연결` 섹션 — "서브에이전트 `gpters-case-researcher`
      가 후보 글을 물어오면 → clips 로 저장" 문장은 지금 **현재형 활성 워크플로우**로
      쓰여 있어, 보류 후에도 그대로 두면 사실과 어긋난다. `gpters-clipper` 자체의 목록/태그
      검색 단계(028)로 흡수됐다는 내용으로 갱신한다. (`docs/05-skills-overview.md`의 언급은
      "008에서 신규 생성" 이력 표라 과거형 서술이므로 갱신 대상 아님 — 확인 후 미변경.)
- [x] `ticket/008-agent-gpters-case-researcher.md`(원 생성 티켓)에 이번 보류 결정 backlink를
      추가한다.

## 완료 기준

- 메인 에이전트가 태그/주제 검색 요청을 받으면 `gpters-clipper` skill을 쓰지,
  `gpters-case-researcher`를 spawn하지 않는다.
- agent 파일 자체는 삭제되지 않고 저장소에 남아 있다.

## 막힌 점 / 메모

- 관련: [[028-gpters-clipper-listing-search]] (이 agent 로직이 흡수되는 대상),
  [[008-agent-gpters-case-researcher]] (원 생성 배경)
