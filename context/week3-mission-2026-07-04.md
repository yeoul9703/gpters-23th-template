# 3주차 미션 논의 — compact 전 맥락 스냅샷 (2026-07-04)

> **후속 처리 완료 (2026-07-04, "스터디 미션 점검" 세션)**: 아래 "핵심 미완료" 항목(domino-skill 구체 예시 부재)은 정적 예시 대신 `g23-thinking-partner` 되묻기 흐름으로 `week-3.md` "이번 주 순서"를 재작성해 해결했다. 근거는 [[018-week3-curriculum-alignment]] 막힌 점 메모 참고. 이 문서는 참고용으로만 남겨둔다.

> 세션 브랜치명: "3주차"(부모 브랜치 "missions 아이데이션"에서 분기). 형제 브랜치 "1주차 미션"·"2주차 미션"·"4주차 미션"이 같은 저장소를 동시에 편집 중이므로,
> 티켓 상태가 이 문서 작성 시점과 다를 수 있다 — 최신 상태는 항상 `ticket/README.md`를 확인한다.
> 실제로 이 세션 도중 병렬 세션이 `ticket/018-week3-curriculum-alignment.md`·`ticket/README.md`·`.claude/skills/g23-missions/SKILL.md`를 todo 상태로 되돌린 적이 있어, 편집 전 재확인 후 다시 반영했다.

## 이 세션에서 있었던 일 (순서대로)

1. `missions/week-3.md`, `.claude/skills/g23-missions/reference/official-curriculum.md`(3주차 행), `week-1.md`·`week-2.md`(발행 패턴 참고용)를 확인.
2. [[018-week3-curriculum-alignment]] 티켓의 "결정할 것" 2개를 처리:
   - 목표 문구 → **일반화**. "아침 동작" 같은 고정 예시를 빼고 공식 표현("여러 스킬을 통합해 한 번에 처리")에 맞춤. "아침 루틴" 예시는 [[020-cross-week-examples-and-tags]]에서 스터디장 사례글 줄에만 남기기로 함 — 018에서는 그 줄을 건드리지 않았다.
   - 사례 게시글 발행 단계 → week-1·2와 동일 패턴으로 "이번 주 순서" 5번·"손에 남는 것"·"멤버 과제"에 추가.
3. **세션 중 새로 나온 결정 — 여러 skill을 한 번에 실행하는 구성 skill을 뭐라고 부를지.**
   여러 라운드의 이름 브레인스토밍이 있었다: 통합/매크로/루틴/오케스트레이터/올인원 → 묶음/올인원/한번에 → 콤보/합체/필살기 → 원런(One-Run)/멀티런(Multi-Run)/올런/토탈런 → 채팅창에 10개 추천 요청(이어달리기·도미노·세트메뉴·원클릭·줄줄이·파이프라인·오토플로우·스킬체인·번들·N-in-1) → **"도미노" 채택**.
   - **최종 형식**: 본문 전체에서 이 개념을 강제 용어로 반복하지 않고 평서문("순서대로 이어서 도는 skill")으로 설명. 실제 `skill-creator`로 만드는 "이번 주 순서" 3번 단계에서만 이름 예시로 `domino-skill` **(추천)**을 제시하고 "다른 이름을 붙여도 됩니다"라고 명시 — `skill-creator` SKILL.md가 이미 쓰던 관행(`name: 영문 소문자와 하이픈. 예: meeting-note-cleaner`, "이름·트리거·범위 모두 후보를 주고 고르게 한다")을 그대로 따른 것.
   - 반영 파일: `missions/week-3.md`, `.claude/skills/g23-missions/SKILL.md`(4주 요약표 3주차 행), `ticket/018-week3-curriculum-alignment.md`(결정 근거 기록).
4. 티켓 018 → `status: done`, 결정할 것·할 것 체크리스트 전부 체크. `ticket/README.md` 018 라인도 done으로 갱신 (022·023 등 다른 세션이 추가한 라인은 보존).

## 아직 안 끝난 것 — 다음 세션이 이어갈 질문

- **핵심 미완료**: 사용자가 원래 던진 질문 "3주차 미션을 바탕으로 어떤 것들을 미션으로 제시해야 하지?"에 대해 방향(구체적 domino-skill 예시를 문서에 제시)까지는 합의됐지만, **실제 예시 2~3개(예: 아침 브리핑/회의 준비/주간보고 같은 조합)는 아직 week-3.md에 추가되지 않았다.** 이름 브레인스토밍(3번 항목)에 논의가 쏠리면서 여기로 돌아오지 못했다 — 다음 세션은 여기부터 이어가면 된다.
- 사용자가 명시한 교육 목적: "만든 skill을 절차적으로 실행하는 경험을 제공 → 단기적으로 여러 skill을 하나의 파이프라인으로 실행·설계할 필요성을 경험하고 효과를 얻는 것." 예시를 만들 때 이 목적(파이프라인 설계 필요성 체감)을 기준으로 골라야 한다.
- [ ] domino-skill 구체 예시 2~3개를 어떤 기준으로 고를지 (직군 무관 범용 예시 vs [[021-welcome-daily-moments-detail]]의 "하루 세 시점" 프레임과 연결할지)
- [ ] 예시를 week-3.md 어디에 넣을지 (현재 "이번 주 순서" 3번은 이름 제안만 있고 구체 조합 예시는 없음 — 새 섹션을 만들지, 3번 안에 붙일지)
- [ ] [[020-cross-week-examples-and-tags]]의 "스터디장 사례글" 예시 교체(공식 3예시 배분)와 이 domino-skill 예시가 서로 다른 것인지 — 스터디장 사례글은 "완성된 결과물 사례"이고, 이번 항목은 "참가자가 시도해볼 조합 후보"라 성격이 다르다는 점을 다음 세션에 명확히 인지시킬 것.

## 살아있는 티켓 지도 (이 문서 작성 시점 기준)

| 티켓 | 상태 | 비고 |
|---|---|---|
| 016 (인덱스) | doing | 017~020 전부 done되면 done |
| 017 week-2 정합 | done | "2주차 미션" 세션이 처리 |
| 018 week-3 정합 | done | 이 세션에서 처리 — 단, domino-skill 구체 예시는 미완 (위 참고) |
| 019 week-4 정합 | todo | "4주차 미션" 세션 추정 |
| 020 예시 다양화 + 태그 스윕 | todo | 017~019 끝난 뒤 실행 |
| 021 welcome 하루 세 시점 디테일 | todo | 별도 세션에서 추가 논의 예정 |
| 022 사무직 보편 업무 예시 클리핑 | todo | week-2 논의에서 파생(추정) |
| 023 1주차 k-skill 환경무관 기준 | todo | "1주차 미션" 세션에서 생성, 진행 중 |

> 여러 세션이 같은 저장소를 동시에 건드리고 있다 — 파일을 다시 쓰기 전 항상 재확인할 것(`ticket/README.md`, 해당 티켓 파일). Edit 충돌 나면 재-Read 후 재시도.

## 참고 자료

- 공식 커리큘럼 스냅샷: `.claude/skills/g23-missions/reference/official-curriculum.md` (3주차 행)
- `skill-creator` SKILL.md의 이름 제안 관행: `.claude/skills/skill-creator/SKILL.md` ("name: 영문 소문자와 하이픈만. 예: `meeting-note-cleaner`", "참가자 대신 결정하지 않는다 — 이름·트리거·범위 모두 후보를 주고 고르게 한다")
- 원본 스터디 페이지: https://www.gpters.org/ai-study-list/post/babbeun-silmujareul-wihan-oneul-baeweo-naeil-sseomeogneun-k-seukil-4HGbQhiSgpP2S2E
