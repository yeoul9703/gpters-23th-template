# 지피터스 23기 k-skill 활용 스터디 — 작업 가이드

이 파일은 매 세션 시작 시 참고하는 짧은 프로젝트 가이드입니다.

## 스터디 목표

참가자가 4주 동안 **자기 업무에 실제로 쓰는 Claude Code skill 3개**를 만든다.
0부터 발명하지 않는다. 잘 만들어진 한국어 자동화 사례 모음인 **[k-skill](https://github.com/NomaDamas/k-skill)** 을 출발점으로 삼아, 내 업무에 맞게 바꾸고 → 일주일 써보고 → 다시 고친다.

## 최종 결과물 (4주)

1. 자기 업무에 실제로 쓰는 skill 3개
2. 4주 사용 경험 기반 사례글 1개
3. 각 skill마다 짧은 사용 기록: 목적 / 사용 전·후 / 막힌 점 / 고친 점

## 폴더 구조

- `.claude/skills/g23-missions/reference/week-*.md` — 주차별 목표·제출물·체크리스트 (g23-missions 스킬이 매번 읽는 미션 원문)
- `examples/skill-log-template.md` — skill별 사용 기록 양식
- `examples/case-post-notes-template.md` — 사례글 작성용 메모 양식
- `.claude/skills/` — 스터디용 도우미 skill 모음 (`g23-welcome`이 온보딩 중 `g23-setup`·`g23-kskill-intro`를 내부적으로 부름)
- 참가자가 만드는 skill도 `.claude/skills/{skill-name}/SKILL.md` 에 둔다

## 작업 지침

- **큰 파일을 통째로 읽지 말 것.** 지금 필요한 미션 파일이나 템플릿 하나만 확인한다. (특히 Pro 요금제 토큰 절약)
- skill은 작게 시작한다. "15분 안에 끝낼 수 있는 범위"로 자른 뒤 만들고, 써보며 고친다.
- 참가자 대신 결정을 내리지 말고, 선택지를 주고 고르게 한다.
- 참가자 로컬 설정(`.claude/settings.json`, hooks 등)을 자동으로 수정하지 않는다. 필요하면 무엇을 왜 바꾸는지 설명하고 참가자가 직접 하게 한다.
- OS(macOS/Windows)에 따라 명령이 다르면 분리해서 안내한다. bash를 전제하지 않는다.

## skill 만드는 법 (요약)

`.claude/skills/{skill-name}/SKILL.md` 파일 하나가 skill 하나다. 앞부분에 frontmatter를 둔다.

```markdown
---
name: my-morning-routine
description: 아침에 하루를 시작할 때 오늘 할 일과 우선순위를 정리한다. "하루 시작", "오늘 뭐부터", "아침 정리"라고 말하면 켠다.
---

# 아침 루틴 정리

(무엇을 어떤 순서로 하는지, 입력·출력·사용 흐름을 적는다)
```

`description` 에 **언제 켜지는지(트리거 표현)** 를 적어야 Claude가 알아서 실행한다.

## 참고 (공식 문서)

- Skills: https://docs.anthropic.com/en/docs/claude-code/skills
- Memory(CLAUDE.md): https://docs.anthropic.com/en/docs/claude-code/memory
