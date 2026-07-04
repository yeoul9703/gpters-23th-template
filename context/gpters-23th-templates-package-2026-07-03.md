# 배포 패키지 스냅샷 — 위치·skill 이름 규칙·배포 보류 상태 (2026-07-03)

`/Users/yeojin/dev/gpters-23th-template`은 지피터스 23기 k-skill 스터디 **참가자 배포 템플릿**이다. Yeojin의 context-hub와 분리된 별도 폴더/repo이며, hub의 AGENTS.md·티켓 체계·작업 스타일에 종속되지 않게 유지한다 (참가자에게 hub 컨벤션을 노출하지 않는다).

## 정해진 것

- 스킬 이름 규칙: 스터디 전용은 `g23-{title}`, 범용 도구는 무접두. 현재 6종: `g23-welcome`(setup 흡수·삭제), `g23-missions`, `g23-thinking-partner`, `g23-k-skills-search`, `g23-case-writer`(구 case-post-writer), `skill-creator`.
- 서브에이전트 2종: `.claude/agents/k-skill-researcher`, `gpters-case-researcher` (본문 조사는 Jina Reader 경유 — `gpters-clipping-jina-reader-2026-07-03.md` 참고).
- 구조: README/CLAUDE.md + `missions/week-1~4` + `examples/` + `.claude/skills/` + `ticket/`(기획 기록 + clips 50개). hooks·settings.json·commands·Python/zsh는 넣지 않는다.
- k-skill(NomaDamas/k-skill)은 Claude Code 플러그인 마켓플레이스로 배포됨: `/plugin marketplace add NomaDamas/k-skill`, 실행 `/k-skill:<name>`, 설정 `k-skill-setup`.

## 상태 (2026-07-03)

실행 큐(`ticket/_runplan.md`) 6/6 완료 — 스킬·에이전트·클립 전부 main에 커밋됨. **GitHub 배포는 사용자 요청으로 보류.** 배포 전 결정 필요: 레포명(`gpters-23th-templates` 복수 vs `gpters-23th-template` 단수), 공개범위(public/private), `ticket/` 폴더 포함 여부(운영 기록이라 배포본에서 뺄지).

기획·티켓은 hub(`/Users/yeojin/yeojin-context-hub`)의 `work/tickets/biz-gpters-23-k-skill-*.md`와 `projects/gpters-23-k-skill/`에도 있다.

> auto-memory에서 이 저장소 context/로 옮겨온 문서 (2026-07-04). 최신 배포 상태는 이 문서가 아니라 `ticket/README.md`·git 로그를 확인할 것 — 여기는 2026-07-03 시점 스냅샷이다.
