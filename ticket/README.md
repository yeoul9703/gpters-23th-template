# ticket — 내가 할 일 모음

작업 하나 = 파일 하나. `001-무엇.md` 처럼 번호를 붙여 쌓는다.
0부터 발명하지 않고, 지금 손대야 할 것만 카드처럼 얇게 적는다.

## 두 종류가 있다

- **티켓** (`ticket/*.md`) — 내가 **할 일**. 만들 skill 작업, 스터디 미션 to-do, 막힌 점.
- **클리핑** (`ticket/clips/*.md`) — 나중에 볼 **자료**. 지피터스 "베스트 사례"·"ax" 사례 중 진짜 쓸모 있는 글.

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
- `021-welcome-daily-moments-detail.md` — g23-welcome 미니 실습 하루 세 시점 디테일 논의 (todo, 추가 세션에서)
- `022-clip-office-worker-skill-examples.md` — 사무직 보편 업무 스킬 예시 클리핑 점검·보강 (gpters + k-skill) (todo)
- `023-week1-kskill-environment-independent-wow.md` — 1주차 k-skill 예시 환경 무관 실행 + 와우 포인트 기준 (todo, 우선순위 낮아 보류)

**참고**
- `001-example.md` — 견본 티켓 (감 잡으면 삭제)

### 관계 지도

```
g23-welcome ──안내──▶ g23-missions        (온보딩→매주 미션)
   └ g23-setup 흡수
g23-thinking-partner ──▶ skill-creator     (범위 좁히기→실제 생성)
k-skill-researcher ─┐
gpters-case-researcher ─┴─▶ gpters-clipper ─▶ ticket/clips + g23-case-writer  (조사→클립(원문 발췌 필수)→사례글)
   └ 첫 수동 실행 = 009 (Fable 5, task.json) → clips/_style-reference.md
   └ 클립 형식 결함(원문 발췌 누락) 발견·수정 = 024 → gpters-clipper 스킬 신설
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
