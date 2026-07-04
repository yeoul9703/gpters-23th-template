---
id: 025
title: g23-welcome — OS/Python 셋업 가이드를 reference 문서로 분리
type: skill
status: done
created: 2026-07-04
---

## 뭘 하려는가 (한 줄)

Windows/Mac 터미널 차이 + Python이 필요해질 때 uv 쓰는 법을, 새 스킬이 아니라
`g23-welcome/reference/setup-guide.md` 온디맨드 문서로 담고, welcome·skill-creator
양쪽에 포인터 한 줄씩만 연결한다.

## 왜 / 언제 쓰는 일인가

세션 논의(`context/python-setup-uv-consistency-2026-07-04.md`)에서:
- 참가자가 만드는 skill은 SKILL.md 한 장짜리 자연어 지시문이라 대부분 Python이 필요 없음(P1).
- 하지만 드물게 필요해지는 참가자마다 설치 방식(conda/pip --user/brew python 등)이 제각각이면
  트러블슈팅 비용이 매번 새로 든다 → uv로 통일하는 컨벤션만 문서화해두기로 함.
- `g23-setup`을 스킬로 되살리는 안도 검토했으나 기각: 스킬 `description`은 매 세션 상시 로드되는데,
  실제로 쓰이는 빈도가 낮아 "빈 껍데기"(과거 g23-setup 삭제 사유, task 010/A1)가 재발함.
- advisor 확인: welcome은 자체적으로 셸 명령을 내리지 않으므로(②는 슬래시 커맨드, ⑤는 Claude
  툴로 파일 생성) ①에 "터미널 종류" 질문을 미리 추가해도 welcome 안에서 쓰일 데가 없음 →
  질문 추가 대신 `g23-missions`가 `reference/official-curriculum.md`를 참조하는 것과 같은
  포인터 방식으로 처리.

## 확정된 설계

- `g23-welcome/reference/setup-guide.md` (완료) — §1 Windows/Mac 터미널 차이, §2 Python 필요시 uv 컨벤션.
- `g23-welcome/SKILL.md`에 포인터 1줄 추가 (①에 새 질문 추가 안 함).
- `skill-creator/SKILL.md`에 포인터 1줄 추가 — §2(Python/uv)가 이번 배치 후 아무 데서도
  연결 안 되는 고아 섹션이 되지 않도록.

## 할 것 (체크리스트)

- [x] `.claude/skills/g23-welcome/reference/setup-guide.md` 작성
- [x] `g23-welcome/SKILL.md`에 reference 포인터 1줄 추가 (① 끝, 새 질문은 추가 안 함)
- [x] `skill-creator/SKILL.md`에 reference 포인터 1줄 추가 (3문 인터뷰 질문3 아래)
- [x] 검증: 서브에이전트에게 "처음 온 Windows 참가자" 시나리오 위임 — 5개 체크(흐름 어색함/링크 정합/포맷 일관성/P1·A1 정합) 전부 pass
- [x] `ticket/README.md` 인덱스 갱신

## 막힌 점 / 메모

- 스킬 승격(가칭 `g23-setup` 부활)은 명시적으로 기각 — 근거는 위 "왜" 항목.
- 관련: `context/python-setup-uv-consistency-2026-07-04.md` (전체 논의 스냅샷), `004-g23-welcome.md`, `005-skill-creator.md`, `ticket/_discuss.md` P1/A1.
