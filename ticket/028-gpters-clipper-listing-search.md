---
id: 028
title: gpters-clipper에 목록/태그 검색 진입 경로 추가
type: skill        # skill | mission | fix
status: done       # todo | doing | done
created: 2026-07-13
done: 2026-07-13
---

## 뭘 하려는가 (한 줄)

`gpters-clipper` skill(개명 없음, 그 자리에서 확장)에 목록/태그 검색 진입 경로를 추가해서,
URL을 이미 아는 경우뿐 아니라 "~ 관련 사례 찾아줘"처럼 주제/태그만 주는 경우도 같은 스킬
하나로 처리한다.

## 왜 / 언제 쓰는 일인가

참가자가 URL을 직접 아는 경우도 있지만, 주제만 던지는 경우가 더 많을 것으로 예상된다.
지금은 후자를 처리하려면 `gpters-case-researcher` 서브에이전트를 거쳐야 하는데, 입문자
입장에선 서브에이전트 홉이 안 보여서 "무슨 일이 일어나는지" 따라오기 어렵다. 배경·검증
내역은 [`_gpters-clipper-listing-search.md`](_gpters-clipper-listing-search.md) 참고.

## 할 것 (체크리스트)

- [x] SKILL.md description에 두 트리거 모두 반영: "URL 클립해줘" 계열 +
      "~ 사례 찾아줘"/"~ 관련 글 찾아줘" 계열. `name`·디렉터리명은 그대로 `gpters-clipper`
      유지(개명 안 함).
- [x] 절차 맨 앞에 신규 단계 A·B를 추가하고, **기존 1~6단계(본문 열기→핵심 추출→원문
      발췌→원문 전문→저장→인덱스 갱신)는 그대로 보존한다.**
  - **A. 목록 진입 (신규, 주제/태그만 왔을 때만)**: 목록 페이지를
    `curl -sL "https://r.jina.ai/<목록 또는 태그 URL>"`로 열어 게시물 URL+제목+요약을
    enumerate한다.
  - **B. 후보 확인 (신규, 주제/태그만 왔을 때만)**: 후보를 사람에게 나열해 확인받는다
    (case-researcher의 "요약만 보고, 저장은 사람 확인 후" 원칙 유지 — 자동 대량 클립은
    이번 스코프 밖).
  - **기존 1단계부터 그대로 진행**: URL이 이미 주어졌으면 A·B를 생략하고 바로 기존
    1단계(`curl` + jina로 본문 열기)부터 시작한다. A·B를 거쳤다면 확정된 URL마다
    기존 1~6단계를 그대로 반복한다.
- [x] "하지 않는 것" 섹션에 추가: 페이지네이션 이상(무한스크롤 첫 배치 이후)의 게시물은
      다루지 않는다 — 더 있을 수 있다는 안내만 남긴다.
- [x] 별도 scripts/references 폴더를 만들지 않는다 (P1 준수, curl은 절차 텍스트에 인라인).
- [x] `docs/04-clips-clipping.md`, `docs/10-next-steps.md`는 확인 결과 실제로
      `gpters-clipper`를 전혀 언급하지 않았다 — 029에서 두 문서의 관계도/연결 문장을
      `gpters-clipper` 중심으로 갱신(현재형 case-researcher 활성 서술도 함께 정정)했다.
- [x] `ticket/README.md` 관계 지도는 이미 이 작업(028/029) 반영해 갱신됨 — 완료 상태로 이동.
- [x] `g23-case-writer` 등 다른 skill이 `gpters-clipper`를 이름으로 참조하는 곳이 있는지
      `grep -rln "gpters-clipper"`로 확인 — SKILL.md 자기 자신 외 참조 없음(개명이 없어
      깨질 참조도 없음).

## 완료 기준

- 주제만 주는 트리거와 URL을 주는 트리거 둘 다 같은 skill(`gpters-clipper`, 개명 없음)이
  처리한다.
- 기존 발췌+전문 로직(클립 50개로 검증된 부분, 1~6단계)은 그대로 보존된다.
- SKILL.md가 여전히 한 장 분량이고, 별도 스크립트/리소스 파일이 없다.

## 막힌 점 / 메모

- 관련: [[024-clip-verbatim-excerpts]], [[026-clip-full-body-text]] (흡수 대상 로직의 배경)
- `gpters-case-researcher`와의 관계는 별도 티켓([[029-case-researcher-hold]]) 참고 —
  이 티켓은 로직 흡수만 다루고, agent 파일 처리는 건드리지 않는다.
- 이름은 `gpters-clipper`(p 두 개)로 확정. 초기 논의에서 "gpters-cliper"(p 하나)로 부른
  건 오타였음 — cold-read 검토 1사이클에서 발견·정정(2026-07-13).
