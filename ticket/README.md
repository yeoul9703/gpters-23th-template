# ticket — 내가 할 일 모음

작업 하나 = 파일 하나. `001-무엇.md` 처럼 번호를 붙여 쌓는다.
0부터 발명하지 않고, 지금 손대야 할 것만 카드처럼 얇게 적는다.

## 두 종류가 있다

- **티켓** (`ticket/*.md`) — 내가 **할 일**. 만들 skill 작업, 스터디 미션 to-do, 막힌 점.
- **클리핑** (`clips/*.md`) — 나중에 볼 **자료**. 지피터스 "베스트 사례"·"ax" 사례 중 진짜 쓸모 있는 글.

할 일이면 티켓, 언젠가 볼 자료면 클리핑. 헷갈리면 티켓.

## 티켓 만드는 법

1. `_template.md` 를 복사해 `002-무엇.md` 로 저장 (번호는 다음 순번).
2. 앞부분 frontmatter만 채우고, 나머지는 쓰면서 채운다.
3. 상태가 바뀌면 `status:` 만 고친다 (`todo → doing → done`).

작게 자른다. "15분 안에 끝낼 수 있는 범위"가 티켓 하나의 크기.

> 여러 티켓에 걸린 **결정할 것들**은 [`_discuss.md`](_discuss.md) 에 모아둔다. 정해지면 각 티켓에 반영.

## 지금 열린 티켓

<!-- 새 티켓을 만들면 여기 한 줄씩 추가. done 은 지우거나 아래로 내린다. -->

**만들/고칠 skill**
- `022-clip-office-worker-skill-examples.md` — 사무직 보편 업무 스킬 예시 클리핑 점검·보강 (gpters + k-skill) (doing — gpters 신규 12개 클립(052~063) + 기존 13개 office-general 재태깅 완료, task 022; k-skill 정적 클립 여부·참조 위치는 미정)

**참고**
- `001-example.md` — 견본 티켓 (감 잡으면 삭제)

### 관계 지도

```
g23-welcome (오케스트레이터, ①만 인라인) ──▶ g23-missions   (온보딩→매주 미션)
   └ ① 초반에 g23-setup 먼저 호출(clone 직후 미초기화 상태일 때만) — 031, 독립 스킬로 재신설
   └ ②~⑥ 순서대로 호출 — 032, A7. g23-kskill-intro → g23-work-discovery →
     g23-personalize → g23-mini-practice → g23-missions-handoff
g23-thinking-partner ──▶ skill-creator     (범위 좁히기→실제 생성)
k-skill-researcher (읽기 전용 조사, 활성)

gpters-clipper ──▶ clips + g23-case-writer   (목록/태그 검색→클립(원문 발췌+원문 전문 필수)→사례글)
   └ 첫 수동 실행 = 009 (Fable 5, task.json) → clips/_style-reference.md
   └ 클립 형식 결함(원문 발췌 누락) 발견·수정 = 024 → gpters-clipper 스킬 신설
   └ 발췌만으론 글 구조가 안 보임 → 원문 전문 추가 = 026 (done — 프롬프트만 0/50 미실행 → bash 백필은 셸 오염 → uv Python + selector로 재백필, 51/51 전수 검증 clean)
   └ 입문자 단일 흐름을 위해 목록/태그 검색 진입 경로(A·B 단계) 추가(개명 없음) = 028 (done, task 030)
   └ fetch·정제를 scripts/(fetch_post.py·fetch_list.py, uv run)로 이동, P1 예외 (026, 2026-07-14)

gpters-case-researcher — ⚠️ 보류 (029, done, task 030). 목록/태그 훑기 역할은
gpters-clipper의 A·B 단계로 흡수됨. agent 파일은 참고용으로 남아 있음(삭제 안 함).
```

## done

<!-- 끝난 티켓을 여기로 -->

- `004-g23-welcome.md` — welcome 신규(6단계) + setup 삭제 (task 010, 2026-07-03)
- `006-g23-missions.md` — 4주치 점검·핸드오프 정합 (task 010, 2026-07-03)
- `005-skill-creator.md` — 3문 인터뷰→SKILL.md 한 장 (task 011, 2026-07-03)
- `002-g23-thinking-partner.md` — 미니 스펙 + skill-creator 핸드오프 (task 011, 2026-07-03)
- `007-agent-k-skill-researcher.md` — .claude/agents/ 읽기 전용 조사 에이전트 (task 012, 2026-07-03)
- `008-agent-gpters-case-researcher.md` — 동상, C3 완결 확인 (task 012, 2026-07-03)
- `009-clip-gpters-writing-samples.md` — 014 에 병합·초과 달성 (2026-07-03)
- `014-clip-gpters-50.md` — 지피터스 사례 50개 클립 + `clips/_style-reference.md` (task 014, 2026-07-03)
- `003-g23-case-writer.md` — g23-case-writer 개명 + 경량 재작성, C1 상투구 9개 확정 (task 013, 2026-07-03)
- `015-clip-blank-body-diagnosis.md` — 빈 본문 원인 = Jina 동시요청 502 + 실패 오표기·재시도 부재. researcher 규칙 수정 (Fable 브랜치, 2026-07-03)
- `025-welcome-setup-reference.md` — OS/Python 셋업 가이드를 `g23-welcome/reference/setup-guide.md` 온디맨드 문서로 분리, welcome·skill-creator에 포인터 1줄씩 연결 (스킬 승격 안 함, task 025, 2026-07-04)
- `016~020` (스터디 미션, 인덱스+자식 4개) — `missions/week-1~4.md`를 gpters.org 공식 커리큘럼에 맞춤. week-4 스터디장 세션 한 줄 반영(019), week-3 domino-skill을 예시 대신 thinking-partner 되묻기 흐름으로 보강(018), week-2~4 사례글 예시 다양화는 사용자 반려로 스킵·태그 스윕만 확인(020) ("스터디 미션 점검" 세션, 2026-07-04)
- `024-clip-verbatim-excerpts.md` — clips/ 50개 전부에 `## 원문 발췌`(verbatim) 섹션 추가 + 사실오류 3건(007/009/038) 수정 + `gpters-clipper` 스킬 신설로 재발 방지 (task 024, 2026-07-04)
- `021-welcome-daily-moments-detail.md` — 1차("현재 상태 유지") 결정을 별도 세션에서 재검토해 뒤집음 → 세 시점 질문에 예시 구체화, 미니 실습 예시 코드 3개(아침/점심/퇴근) 전부 반영, ⑤-4 죽은 분기(skill-creator 부재 체크) 삭제. thinking-partner 확산은 안 함 유지 (2026-07-04)
- `_gpters-clipper-listing-search.md`, `028-gpters-clipper-listing-search.md`, `029-case-researcher-hold.md` — gpters-clipper에 목록/태그 검색 진입 경로(A·B 단계) 추가 + gpters-case-researcher agent 보류 처리(삭제 안 함) + docs/04·docs/10 관계 서술 정정 (결정 gate + 3사이클 cold-read 리뷰, task 030, 2026-07-13)
- `026-clip-full-body-text.md` — clips/ 전체에 `## 원문 전문` 확보. 3단 경위: ① 프롬프트 지시만으론 0/50 미실행 ② bash+curl 백필은 사이트 헤더 오염·오판(013 손상, 016/021/043 오표기) ③ uv Python(`scripts/fetch_post.py`·`fetch_list.py`) + Jina `x-target-selector`로 재백필, 51/51 전수 검증 clean. 4-backtick 펜스·429 대기·죽은 링크 판정 포함, SKILL.md도 lean 재작성 (gpters-clippers 브랜치 세션, 2026-07-14)
- `027-welcome-mini-practice-clear-output.md` — welcome ⑤ 성공 정의를 "트리거 발동"→"산출물 확인"으로 강화 + ②에 `market-kurly-search` 실행 체험(자격증명 불필요 조건) 신설 (2026-07-14)
- `023-week1-kskill-environment-independent-wow.md` — 삭제(2026-07-14). "1주차 k-skill 예시 환경 무관 필터" 문제의식은 027에서 확정한 ② 후보 조건("자격증명/API 키 불필요")으로 이미 충족돼 별도 티켓 불필요 → 파일 삭제, 결정 근거는 `_discuss.md` 확정 로그에 남김.
- `031-g23-setup-scaffold.md` — g23-setup을 독립 스킬로 재신설(A1 뒤집음). 로컬 git 재초기화·CLAUDE.md 최소 정체성 기록 담당, welcome 초반에서 미초기화 상태일 때만 핸드오프. 트리거 문구를 action-phrased로 한정해 welcome 세션 시작 트리거와 겹치지 않게 확인 (2026-07-14, welcome 오케스트레이터화 여부는 032로 분리)
- `033-missions-folder-relocate.md` — 루트 `missions/week-*.md`를 `.claude/skills/g23-missions/reference/`로 이동. missions/는 g23-missions 외에 관여되는 곳이 없고, 온보딩이 `/g23-missions` 경유로만 미션을 안내하도록 설계돼 있어 루트에 남을 근거가 빈약하다는 판단(025와 동일 패턴). README/CLAUDE.md 폴더 구조 갱신, SKILL.md에 week-N.md(매번 읽음)와 official-curriculum.md(온디맨드) 구분 명시 (2026-07-14)
- `032-welcome-orchestrator-reconsider.md` — g23-welcome을 오케스트레이터로 재설계. ②~⑥을 `g23-kskill-intro`·`g23-work-discovery`·`g23-personalize`·`g23-mini-practice`·`g23-missions-handoff` 5개 skill로 분리, welcome은 ①만 인라인 + 나머지는 순서 호출만. 동기는 구조 정리(재사용 아님) — ⑥ 빈 껍데기·③ thinking-partner 트리거 충돌 위험은 사용자가 인지하고 감수 (A7, 2026-07-14)
