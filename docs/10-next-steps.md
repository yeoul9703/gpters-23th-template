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
- ~~지피터스 로그인 벽?~~ → 태그 목록·본문 공개 / 프로필만 로그인 벽 (C3, 완결)
- ~~k-skill 접근: 로컬 클론 vs 원격~~ → **원격 조회** 확정 (C2)
- ~~이름: case-post-writer → case-writer 통일~~ → **개명 완료** (C4·P2, task 013)
- ~~AI 상투구 최종 목록 확정~~ → **9개 확정, SKILL.md 인라인** (C1, task 013)

## 현재 상태 (2026-07-03 밤 갱신)

- `main` 단일 브랜치, 실행 큐(`ticket/_runplan.md`) **6/6 완료** — 스킬 5종·에이전트 2종·클립 50개 전부 반영
- 열린 결정 없음. 티켓 논의(_discuss.md) 전부 ✅
- 남은 것:
  - 사용자가 SKILL.md 5종 톤 훑어보기 (비개발자 눈높이 확인, _runplan '사용자 개입 포인트')
  - GitHub 배포 (사용자 보류 중 — 레포명 단수/복수, 공개범위 결정 필요)
