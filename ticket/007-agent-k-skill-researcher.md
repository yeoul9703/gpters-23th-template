---
id: 007
title: k-skill-researcher — k-skill 레포 조사 서브에이전트
type: agent
status: done
created: 2026-07-03
done: 2026-07-03
---

## 뭘 하려는가 (한 줄)

k-skill 레포를 뒤져 내 업무에 참고할 사례를 찾아오는 서브에이전트.

## 왜 / 언제 쓰는 일인가

신규 서브에이전트 (`.claude/agents/` 아직 없음 → 새로 만듦).
기존 스킬 `g23-k-skills-search` 는 참가자와 대화하며 고르는 쪽,
이 에이전트는 그 뒤에서 **넓게 훑고 후보만 물어오는** 조사 담당. 스킬이 에이전트를 부르는 구조.

## 할 것 (체크리스트)

- [x] 서브에이전트 정의 방식 확인 (.claude/agents/*.md frontmatter — 공식 docs: name/description 필수, tools 콤마 구분)
- [x] 입력(내 업무 키워드) → 출력(후보 사례 3~5개: 링크·요약·왜 맞는지) 스펙 정하기 → `.claude/agents/k-skill-researcher.md` 에 명시
- [x] 읽기 전용 도구만 부여 (`tools: WebFetch, WebSearch, Read, Grep, Glob`)
- [x] g23-k-skills-search 가 이 에이전트를 부르도록 연결 (SKILL.md "찾는 방법" 2번에 위임 한 줄)
- [x] 실제 키워드 1개로 돌려보기 (아래 시험 기록)

## 시험 실행 기록 (2026-07-03, task 012)

- 입력: **"회의록 정리"**. 에이전트 정의대로 시뮬레이션: README 인덱스 1회 fetch → 후보 선별 → 개별 SKILL.md 1개 fetch(경로 패턴 `{skill}/SKILL.md` 원격 접근 확인).
- 출력 형태 확인: 후보 5개 — `korean-humanizer`(AI 티 윤문), `korean-spell-check`(맞춤법 교정), `hwp`(.hwp→Markdown 변환), `rhwp-edit`(.hwp 본문 편집), `korean-character-count`(글자 수 계산). 각각 경로·한줄 요약·왜 맞는지(문서 정리 흐름과 닮음) 형태로 나옴 → 스펙 부합.
- 본문 통째 반환 없음(요약만). 레포는 최상위 스킬 폴더 ~110개 + README 마스터 표 구조라 "인덱스 먼저 → 개별 fetch 최대 5개" 방식이 잘 맞음.

## 막힌 점 / 메모

- ~~k-skill 레포를 로컬 클론할지, 원격으로 볼지 결정~~ → **C2 확정: 원격 조회** (GitHub raw·WebFetch, 클론 안 함)
- 관련: [[003-g23-case-writer]] 와 결과를 클립으로 남길 수 있음 → ticket/clips
