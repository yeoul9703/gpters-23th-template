---
id: 031
title: g23-setup 신설 — 참가자 작업 공간 스캐폴드 (독립 스킬로 부활)
type: skill
status: done
created: 2026-07-14
---

## 뭘 하려는가 (한 줄)

clone 직후 템플릿 폴더를 참가자 개인 작업 공간으로 만드는 일회성 초기화(로컬 git 재초기화·CLAUDE.md 최소 정체성 기록·환경 점검)를 `g23-setup` 독립 스킬로 신설하고, `g23-welcome` 초반에서 자동으로 이어지게 한다.

## 왜 / 언제 쓰는 일인가

스터디 실습시간(50분)에 참가자가 템플릿을 clone한 뒤 `g23-welcome`을 호출하면, 그 흐름 안에서 자연스럽게 초기 스캐폴드(git 재초기화·정체성 기록·환경 설정)가 실행되길 기대함 (사용자 요청, 2026-07-14).

**과거 결정과의 관계 — 이번엔 새 근거로 뒤집음:**
- A1(`_discuss.md`, 2026-07-03): g23-setup 삭제 + welcome으로 트리거 흡수, 리다이렉트 파일 안 만듦.
- 025(`025-welcome-setup-reference.md`, 2026-07-04): g23-setup 부활 검토했으나 기각 — description이 매 세션 로드되는데 실사용 빈도 낮아 "빈 껍데기" 문제 재발.
- 이번엔 **역할 자체가 다름**(OS/Python 안내 문서 ≠ git 초기화·정체성 기록이라는 실행 작업)이라 사용자가 재검토 후 독립 스킬로 재확정. `_discuss.md`에 A1 뒤집힘 기록 필요.

## 결정된 설계 (2026-07-14, 세션 내 확정)

- **등록 방식**: 독립 스킬(`g23-setup`)로 등록. 단 description 트리거는 action-phrased("프로젝트 초기화", "초기 스캐폴드 실행")로 한정 — `g23-welcome`의 세션 시작 트리거("스터디 시작"/"셋업"/"처음인데")와 절대 겹치지 않게 해서 A1이 지운 중복이 재발하지 않게 함.
- **저장소 분리 범위**: 로컬 git만 재초기화(`git init` + 첫 커밋). GitHub 원격 저장소 생성(`gh repo create`)은 이번 스코프 제외 — gh 인증 필요해 50분 실습 예산에 위험.
- **진행 순서(사용자 지정)**: ① 감지 → ② CLAUDE.md 최소 정체성(성함·목적) 채팅으로 질문 후 기록 → ③ 시스템 감지+설정(OS 확인, `setup-guide.md` 참고, 설정은 `/update-config`로 위임) → ④ git init + 첫 커밋(동의 필수 게이트).
- **welcome ③④와의 역할 분리**: g23-setup은 성함·목적이라는 최소 정체성만 **직접 기록**. welcome ③업무파악·④CLAUDE.md개인화(직무·반복업무·해보고 싶은 것)는 그대로 welcome이 맡아 **제안만** — 질문이 겹치지 않음.
- **되돌리기 어려운 작업 원칙**: git 재초기화는 감지→제안→동의 확인→실행 순서 필수, 자동 실행 금지.
- **설정 파일 원칙 유지**: `.claude/settings.json`/hooks 직접 수정 안 함(프로젝트 CLAUDE.md 원칙) — 필요하면 `/update-config` 안내만.
- **재사용**: OS별 터미널/uv 안내는 새로 안 만들고 `g23-welcome/reference/setup-guide.md` 포인터.

## 할 것 (체크리스트)

- [x] `.claude/skills/g23-setup/SKILL.md` 작성
- [x] `g23-welcome/SKILL.md`에 g23-setup 핸드오프 한 줄 추가 (① 앞)
- [x] `ticket/_discuss.md` A1 뒤집힘 기록 (✅ 로그에 반영)
- [x] `ticket/README.md` 인덱스 갱신 (열린 티켓 + 관계 지도)
- [x] 트리거 자가확인: 두 description 문구 비교 결과 겹치는 문자열 없음 — setup은 "프로젝트 초기화"/"초기 스캐폴드 실행"/"스캐폴드 돌려줘"/"이 폴더 내 걸로 만들어줘"(action-phrased), welcome은 "스터디 시작"/"초기 설정"/"셋업"/"처음인데 뭐부터"/"온보딩"(세션 시작형). "초기"라는 어근은 공유하지만 문구 자체는 분리돼 있어 설계 의도대로 확인됨.
- [스킵] (선택) 서브에이전트 드라이런 — 선택 항목이고 실제 clone 직후 미초기화 상태를 안전하게 재현하기 어려워 생략. 실사용 중 문제 생기면 재검토.

## 막힌 점 / 메모

- 세션 중 사용자가 "welcome은 만들어진 스킬들을 절차대로 실행하는 오케스트레이터로 바뀔 것 같다"는 방향성을 언급함 — 지금은 반영 안 하고 핸드오프 한 줄만 추가하기로 결정(범위 통제). 별도 티켓 [[032-welcome-orchestrator-reconsider]] 로 분리.
- 관련: `ticket/_discuss.md` A1, `ticket/025-welcome-setup-reference.md`, `.claude/skills/g23-welcome/SKILL.md`.
