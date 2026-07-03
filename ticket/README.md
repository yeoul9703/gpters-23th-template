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
- `003-g23-case-writer.md` — 담백한 사례글, AI 티 없이 · 경량 (개선) — task 013, 009 대기


**실행 태스크 (Fable 5)**
- `009-clip-gpters-writing-samples.md` (+`009-clip-gpters.task.json`) — 지피터스 사례글 클립 → case-writer 문체 레퍼런스

**참고**
- `001-example.md` — 견본 티켓 (감 잡으면 삭제)

### 관계 지도

```
g23-welcome ──안내──▶ g23-missions        (온보딩→매주 미션)
   └ g23-setup 흡수
g23-thinking-partner ──▶ skill-creator     (범위 좁히기→실제 생성)
k-skill-researcher ─┐
gpters-case-researcher ─┴─▶ ticket/clips + g23-case-writer  (조사→클립→사례글)
   └ 첫 수동 실행 = 009 (Fable 5, task.json) → clips/_style-reference.md
```

## done

<!-- 끝난 티켓을 여기로 -->

- `004-g23-welcome.md` — welcome 신규(6단계) + setup 삭제 (task 010, 2026-07-03)
- `006-g23-missions.md` — 4주치 점검·핸드오프 정합 (task 010, 2026-07-03)
- `005-skill-creator.md` — 3문 인터뷰→SKILL.md 한 장 (task 011, 2026-07-03)
- `002-g23-thinking-partner.md` — 미니 스펙 + skill-creator 핸드오프 (task 011, 2026-07-03)
- `007-agent-k-skill-researcher.md` — .claude/agents/ 읽기 전용 조사 에이전트 (task 012, 2026-07-03)
- `008-agent-gpters-case-researcher.md` — 동상, C3 완결 확인 (task 012, 2026-07-03)
