# 실행 계획 (run plan) — task.json 위임 루프

티켓 논의는 끝났고, 실제 구현은 **task.json 단위로 위임**한다.
task.json 하나 = 세션(에이전트) 하나가 끝낼 분량. 이 문서가 큐의 기준.

## 실행 큐

| 순서 | task | 내용 | 의존 | 상태 |
|---|---|---|---|---|
| 0 | `009-clip-gpters.task.json` | 지피터스 클리핑 → `_style-reference.md` | — | ⏳ 대기 (Fable 5 세션용) |
| 1 | `010-onboarding.task.json` | welcome 신규 + setup 삭제 + missions 점검 | — | ✅ 완료 (2026-07-03, acceptance 4/4) |
| 2 | `011-meta-tools.task.json` | skill-creator 신규 + thinking-partner 개선 | — | ✅ 완료 (2026-07-03, acceptance 4/4) |
| 3 | `012-researchers.task.json` | 서브에이전트 2개 (.claude/agents/) | — | ✅ 완료 (2026-07-03, acceptance 4/4 · C3 완결 확인) |
| 4 | `013-case-writer.task.json` | case-writer 개명+재작성 | **009 산출물 필수** | 🚫 blocked |

010·011·012 는 서로 독립(파일 겹침 없음) → **병렬 가능**.
013 만 009 뒤. 009 는 runner 가 Fable 로 지정돼 있으니 별도 세션에서.

## 실행 규칙 (runner 가 지킬 것)

1. **task.json 만 읽고 시작한다.** 필요한 결정은 전부 `decisions_already_made` 에 있다. 없는 결정을 새로 내리지 말 것 — 그건 `on_block` 감.
2. `constraints` 는 전부 P1(경량) 파생이다. 어기면 acceptance 를 통과해도 실패.
3. **`ticket/README.md` 인덱스는 건드리지 않는다** (병렬 충돌 방지 — 오케스트레이터가 일괄 갱신).
4. 커밋은 태스크당 1개, 메시지에 `task NNN` 명시. 병렬 실행 시엔 커밋하지 말고 파일 변경까지만 (오케스트레이터가 커밋).
5. 막히면 `on_block` 대로: 억지로 완성하지 말고 티켓 '막힌 점'에 기록 후 보고.

## 완료 판정

각 task.json 의 `acceptance` 를 그대로 검사한다. 통과 →
해당 티켓 frontmatter `status: done` + `_runplan.md` 이 표의 상태 갱신.

## 사용자 개입 포인트

- **009**: Fable 5 세션에서 직접 실행 ("ticket/009-clip-gpters.task.json 읽고 실행해").
- 010~013 결과물 중 **SKILL.md 톤**은 사용자가 한 번 훑어보는 걸 권장 (비개발자 눈높이 확인).
- 열린 결정 없음 — P2·C2·C4 확정 완료 (2026-07-03, `_discuss.md` 확정 로그).
