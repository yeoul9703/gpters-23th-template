---
id: 005
title: skill-creator — 3문 인터뷰로 SKILL.md 한 장 뽑아주기 (공식 스펙 경량화)
type: skill
status: todo
created: 2026-07-03
---

## 뭘 하려는가 (한 줄)

참가자가 "이거 skill 로 만들자" 하면, 몇 마디 묻고 SKILL.md 한 장을 만들어준다.

## 왜 / 언제 쓰는 일인가

신규 skill. Anthropic 공식 `skill-creator`(anthropics/skills 레포 + 플러그인)를 **기준으로만**
삼고, 무거운 부분은 다 덜어낸다. 대상이 **비개발자 "바쁜 실무자"(중급), "오늘 배워 내일 써먹는"**
성격이라 고급 개념은 혼란만 준다. P1(경량·Pro) 준수.

트리거: "skill 만들자", "이거 skill 로", "SKILL.md 어떻게 써", "자동화 skill 필요해"

## 확정된 설계 (덩어리)

**공식에서 지킬 것 (스펙 근거)**
- frontmatter `description`(+`when_to_use`) 합쳐 **1,536자 이내**, **가장 흔한 쓰임을 맨 앞**에 → 자동 트리거가 삼
- 트리거 표현은 **약간 넉넉하게** (undertrigger 방지)
- SKILL.md **500줄 이하**, 배치는 프로젝트 `.claude/skills/{name}/SKILL.md`

**공식에서 덜어낼 것 (혼란 요소)**
- ❌ eval/evals.json, 벤치마크 Python, 블라인드 A/B, description 최적화 루프, 서브에이전트 병렬
- ❌ 전문 용어 전반 — "인터뷰→파일 한 장" 수준으로

**흐름 (대화형, 파일 하나)**
1. **범위 확인** — 흐릿하면 만들지 말고 `g23-thinking-partner` 로 넘김 (범위 잡기는 거기 담당)
2. **3문 인터뷰** — ① 뭘 하나(입력→출력) ② 언제 켜나(자연스러운 말 3~5개) ③ 특수 도구 필요?(Bash/Read)
3. **SKILL.md 초안 생성** — frontmatter(name + description=②, 핵심 앞에) + 본문(흐름)
4. **트리거 자가확인** — "이렇게 말하면 켜질까?" 문장 3~5개 눈으로 점검 (스크립트 아님)
5. **한 주 써보고 고치기** — 보통 description/본문 한 줄 수정. 신규·기존 수정 **둘 다** 지원

**결정 (확정)**
- 범위: **신규 생성 + 기존 skill 수정 둘 다** (한 주 써보고 고치는 게 스터디 핵심)
- thinking-partner 관계: **범위는 thinking-partner, skill-creator 는 "생성"에 집중** (중복 제거)
- 공식 플러그인: **"이런 게 있다" 한 줄 포인터만**, 우리는 가벼운 한국어판 유지

## 할 것 (체크리스트)

- [ ] `.claude/skills/skill-creator/SKILL.md` 작성 (위 5단계 흐름)
- [ ] description 을 "핵심 쓰임 맨 앞 + 넉넉한 트리거" 규칙대로 작성
- [ ] g23-thinking-partner → skill-creator 핸드오프 문구 맞추기 (양쪽)
- [ ] 견본 skill 1개 실제로 만들어보며 검증 (비개발자 눈높이 확인)
- [ ] 공식 플러그인 한 줄 포인터 넣기 (`skill-creator@claude-plugins-official`)

## 막힌 점 / 메모

- 근거: Claude Code Skills 공식 docs (frontmatter cap·트리거·배치), anthropics/skills 레포
- 관련: [[002-g23-thinking-partner]] 에서 넘어옴, [[004-g23-welcome]] 미니 실습이 이 스킬을 부름
