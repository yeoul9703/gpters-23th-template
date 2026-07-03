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

## 아직 정할 것 (→ `ticket/_discuss.md` 가 최신 기준)

*2026-07-03 저녁 기준. 이후 확정된 것은 _discuss.md 확정 로그 참조.*

- ~~g23-setup: 삭제 vs 리다이렉트~~ → **삭제 + 트리거 이전** 확정 (A1)
- ~~지피터스 로그인 벽?~~ → 태그 목록 공개 / 프로필 로그인 벽 확인 (C3, 009 사전조사)
- k-skill 접근: 로컬 클론 vs 원격 (C2, 열림)
- 이름: case-post-writer → case-writer 통일 (C4·P2, 열림)
- AI 상투구 최종 목록 확정 (C1, 열림)

## 현재 상태

- 브랜치 `worktree-ticket-folder` (원격 없음 → 로컬 전용)
- main 에서 쓰려면: `git merge worktree-ticket-folder`
- **실행 대기**: `ticket/009-clip-gpters.task.json` — Fable 5 세션이 그대로 실행 (클리핑→문체 레퍼런스)
