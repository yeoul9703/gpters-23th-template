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

## 지금 열린 티켓

<!-- 새 티켓을 만들면 여기 한 줄씩 추가. done 은 지우거나 아래로 내린다. -->

**만들/고칠 skill**
- `002-g23-thinking-partner.md` — 모호한 의도 명확화 (개선)
- `003-g23-case-writer.md` — k-윤문 톤 사례글, AI slop 제거 (개선)
- `004-g23-welcome.md` — 첫날 셋업+온보딩, g23-setup 흡수 (신규)
- `005-skill-creator.md` — Anthropic 공식 참고 skill 제작 도우미 (신규)
- `006-g23-missions.md` — 1~4주차 미션 제공, welcome 과 분리 (점검)

**서브에이전트**
- `007-agent-k-skill-researcher.md` — k-skill 레포 조사 (신규)
- `008-agent-gpters-case-researcher.md` — 지피터스 사례 조사 (신규)

**참고**
- `001-example.md` — 견본 티켓 (감 잡으면 삭제)

### 관계 지도

```
g23-welcome ──안내──▶ g23-missions        (온보딩→매주 미션)
   └ g23-setup 흡수
g23-thinking-partner ──▶ skill-creator     (범위 좁히기→실제 생성)
k-skill-researcher ─┐
gpters-case-researcher ─┴─▶ ticket/clips + g23-case-writer  (조사→클립→사례글)
```

## done

<!-- 끝난 티켓을 여기로 -->
