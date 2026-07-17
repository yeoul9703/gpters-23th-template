# gpters-23th-templates

지피터스 23기 **k-skill 활용 스터디** 참가자용 템플릿입니다.

이 폴더는 4주 동안 여러분이 자기 업무에 실제로 쓰는 Claude Code skill 3개를 만들도록 돕습니다.
스터디의 목표는 "0부터 멋진 자동화를 발명"하는 게 아니라, 잘 만들어진 한국어 자동화 사례 모음인 **[k-skill](https://github.com/NomaDamas/k-skill)** 을 출발점으로 삼아 내 업무에 맞게 바꾸고, 써보고, 다시 고치는 것입니다.

---

## 시작하기 (3단계)

### 1. 이 폴더를 Claude Code로 엽니다

이 폴더를 원하는 위치에 두고, 터미널에서 폴더로 이동한 뒤 `claude` 를 실행하거나 Claude Code에서 이 폴더를 엽니다.

### 2. Claude Code에 아래 문장을 그대로 붙여넣습니다

```text
이 폴더의 README.md와 CLAUDE.md를 읽고, g23-welcome skill을 실행해서 스터디 시작을 도와줘.
```

Claude가 여러분의 OS, Claude Code 사용 경험, 업무를 몇 가지 물어보고 스터디를 시작할 준비를 함께 잡아줍니다.

### 3. 이번 주 미션을 확인합니다

```text
이번 주 미션을 알려줘.
```

`g23-missions` 스킬이 주차별 목표와 제출물을 정리해서 안내합니다.

---

## 폴더 구조

```text
.
├── README.md          ← 지금 읽는 파일
├── CLAUDE.md          ← Claude가 매 세션 참고하는 스터디 가이드
├── examples/          ← 사용 기록·사례글 작성 양식
├── clips/             ← 지피터스 사례 클립 (사례글 쓸 때 문체 참고자료)
└── .claude/skills/    ← 스터디용 도우미 skill 모음 (주차별 미션은 g23-missions/reference/ 안에 있음)
```

> `CLAUDE.local.md`는 clone 직후엔 없다가 `g23-setup` 실행 후 생깁니다 — 내 이름·업무 맥락 등 개인 정보용이라 `.gitignore` 처리돼 있고 git에는 안 실립니다.

## 포함된 skill

Claude Code에게 자연어로 말하면 아래 skill들이 알아서 켜집니다. 슬래시 명령으로 직접 부를 수도 있습니다.

| Skill | 언제 쓰나 |
|---|---|
| `g23-welcome` | 처음 시작할 때 — 셋업부터 첫 skill 실습까지 온보딩 (내부적으로 `g23-setup`·`g23-kskill-intro`를 순서대로 부릅니다) |
| `g23-missions` | 이번 주 무엇을 해야 하는지 확인할 때 |
| `g23-thinking-partner` | 내 반복 업무에서 skill 후보를 고를 때 |
| `g23-k-skills-search` | 참고할 k-skill 사례를 찾을 때 |
| `skill-creator` | 고른 후보를 실제 SKILL.md로 만들 때 |
| `g23-case-writer` | 사용 기록으로 사례글을 쓸 때 |

## 4주 후 손에 남는 것

- k-skill을 응용한 나만의 업무 skill 3개
- 각 skill의 짧은 사용 기록 (목적 / 사용 전후 / 막힌 점 / 고친 점)
- 4주 사용 경험을 담은 사례글 1개

---

## 참여 전 준비

- Claude Code 설치 완료 ([Claude Code desktop 사용법](https://youtu.be/1VLebkCcH5I?si=vFj7k-AN0GSh3Wx2))
- 터미널에서 명령을 실행해본 경험
- Claude Code로 간단한 파일 수정·문서 생성을 시도해본 경험
- skill을 직접 만들거나 수정해본 경험
- [k-skill 레포](https://github.com/NomaDamas/k-skill) 한 번 둘러보기

막히면 오픈카톡방에서 물어보세요: https://open.kakao.com/o/g1hHyaBi
