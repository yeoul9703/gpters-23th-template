# 10 · 관계 지도 · 다음 할 일

## 스킬·에이전트 관계 지도

```
g23-welcome ──안내──▶ g23-missions           (온보딩 → 매주 미션)
   └ g23-setup 흡수
g23-thinking-partner ──▶ skill-creator        (범위 좁히기 → 실제 생성)
k-skill-researcher ─┐
gpters-case-researcher ─┴─▶ ticket/clips + g23-case-writer   (조사 → 클립 → 사례글)
```

## 추천 작업 순서

1. **g23-missions** — 제일 가벼움(점검). week 파일만 확인
2. **g23-welcome** — setup 흡수, missions 로 핸드오프
3. **skill-creator** — 이후 스킬 제작을 빠르게
4. **g23-thinking-partner** — skill-creator 와 짝
5. **조사 에이전트 2개** — 사례 재료 공급
6. **g23-case-writer** — 쌓인 재료로 사례글

## 아직 정할 것 (→ `ticket/_discuss.md`)

- g23-setup: 삭제 vs 얇은 리다이렉트
- 조사 에이전트: k-skill 로컬 클론? 지피터스 로그인 벽?
- 이름: case-post-writer → case-writer 통일

## 현재 상태

- 브랜치 `worktree-ticket-folder` (원격 없음 → 로컬 전용)
- main 에서 쓰려면: `git merge worktree-ticket-folder`
