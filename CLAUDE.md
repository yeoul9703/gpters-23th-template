# 지피터스 23기 k-skill 활용 스터디 — 작업 가이드

## 스터디 목표

참가자가 4주 동안 **자기 업무에 실제로 쓰는 Claude Code skill 3개**를 만든다.
0부터 발명하지 않는다. 잘 만들어진 한국어 자동화 사례 모음인 **[k-skill](https://github.com/NomaDamas/k-skill)** 을 출발점으로 삼아, 내 업무에 맞게 바꾸고 → 일주일 써보고 → 다시 고친다.

## 최종 결과물 (4주)

skill 3개 + 사례글 1개, 그리고 skill마다 짧은 사용 기록(목적 / 사용 전·후 / 막힌 점 / 고친 점).

## 폴더 구조

- `CLAUDE.local.md` — 내 이름·업무 맥락 등 개인 정보. clone 직후엔 없다가 온보딩(`g23-setup`) 중에 생긴다. `.gitignore` 처리돼 있어 git에는 안 실린다 — 이 파일(`CLAUDE.md`)은 스터디 공용 가이드라 개인 정보를 안 담는다.
- `data/gpters/` — 지피터스 사례 클립 모음 (사례글 쓸 때 문체 참고자료, 이미 채워져 있음). "작업 지침"의 "로컬 자료"가 가리키는 게 이 폴더다.
- `.claude/skills/g23-missions/reference/week-*.md` — 주차별 목표·제출물·체크리스트 (g23-missions 스킬이 매번 읽는 미션 원문)
- `.claude/skills/` — 스터디용 도우미 skill 모음. 첫날 온보딩은 두 단계다: `g23-setup`이 작업 공간 초기화와 k-skill 설치·체험을, 이어서 `g23-welcome`이 업무 파악·지피터스 사례·4주 로드맵 HTML·OT 초안을 진행한다.
- 참가자가 만드는 skill도 `.claude/skills/{skill-name}/SKILL.md` 에 둔다

## 작업 지침

- **최우선: 모든 안내는 비개발자·Claude Code 첫 사용자 눈높이의 쉬운 한국어로.** 참가자는 개발자가 아니고 Claude Code도 처음이다. 전문용어(터미널, git, 리포지토리, 커밋 등)를 꼭 써야 하면 바로 옆에 한 줄 풀이를 붙인다. 영어 용어를 번역 없이 그대로 두지 않는다. 설명은 짧고 간략하게 — 길게 나열하지 말고 지금 필요한 것 하나만.
- **큰 파일을 통째로 읽지 말 것.** 지금 필요한 미션 파일이나 템플릿 하나만 확인한다. (특히 Pro 요금제 토큰 절약)
- skill은 작게 시작한다. "15분 안에 끝낼 수 있는 범위"로 자른 뒤 만들고, 써보며 고친다.
- 참가자 대신 결정을 내리지 말고, 선택지를 주고 고르게 한다.
- 참가자 로컬 설정(`.claude/settings.json`, hooks 등)을 자동으로 수정하지 않는다. 필요하면 무엇을 왜 바꾸는지 설명하고 참가자가 직접 하게 한다.
- OS(macOS/Windows)에 따라 명령이 다르면 분리해서 안내한다. bash를 전제하지 않는다.
- **참고 사례가 필요한데 로컬 자료로 안 풀리면 subagent에 위임한다.** 자동화 사례(k-skill)가 필요하면 `k-skill-researcher`, 지피터스 사례가 필요하면 `gpters-case-researcher`에게 넓게 훑어 후보만 받아온다. 참가자에게 별도 skill 이름을 알려줄 필요 없다 — 필요한 순간 자동으로 위임한다.

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
