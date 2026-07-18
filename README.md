# gpters-23th-templates

지피터스 23기 **k-skill 활용 스터디** 참가자용 템플릿입니다.

이 폴더는 4주 동안 여러분이 자기 업무에 실제로 쓰는 Claude Code skill 3개를 만들도록 돕습니다.
스터디의 목표는 "0부터 멋진 자동화를 발명"하는 게 아니라, 잘 만들어진 한국어 자동화 사례 모음인 **[k-skill](https://github.com/NomaDamas/k-skill)** 을 출발점으로 삼아 내 업무에 맞게 바꾸고, 써보고, 다시 고치는 것입니다.

---

## 시작하기 (3단계)

### 1. GitHub에서 이 저장소를 clone하고 Claude Code로 엽니다

clone한 폴더에서 `claude`를 실행하거나 Claude Code로 폴더를 엽니다.

### 2. Claude Code에 아래 문장을 그대로 붙여넣습니다

```text
스터디 시작 도와줘
```

`g23-welcome`이 초기 설정, 실제 마켓컬리 검색, 첫 장보기 skill, 4주 자동화 로드맵,
OT 사례 초안까지 50분 흐름으로 안내합니다.

### 3. 실제 상품 URL을 확인한 뒤 2주차 미션으로 넘어갑니다

`kully-result-{닉네임}.html`에 실제 마켓컬리 상품 URL이 담긴 표가 있고, 장보기 skill 실행·
`gpters-k-skill-report-{닉네임}.html`·OT 사례 초안까지 마쳤다면 아래처럼 말해보세요.

```text
2주차 미션 알려줘
```

첫날 장보기 skill을 1주차 첫 skill로 인정하고, `g23-missions`가 2주차 목표와 제출물을 안내합니다.
만약 결과 표의 URL 칸이 비어 있다면(라이브 검색을 못 한 상태) 아직 1주차를 마친 것은 아닙니다. Node 18과
인터넷을 확인한 뒤 **“장보기 실습 다시 이어줘”**라고 말하면 실제 검색부터 이어갑니다.

---

## 폴더 구조

```text
.
├── README.md          ← 지금 읽는 파일
├── CLAUDE.md          ← Claude가 매 세션 참고하는 스터디 가이드
├── data/              ← 지피터스 사례 클립 (사례글 쓸 때 문체 참고자료)
└── .claude/skills/    ← 스터디용 도우미 skill 모음 (주차별 미션은 g23-missions/reference/ 안에 있음)
```

> `CLAUDE.local.md`는 clone 직후엔 없다가 온보딩(`g23-welcome`) 중에 생깁니다 — 내 이름·업무 맥락 등 개인 정보용이라 `.gitignore` 처리돼 있고 git에는 안 실립니다.

## 포함된 skill

Claude Code에게 자연어로 말하면 아래 skill들이 알아서 켜집니다. 슬래시 명령으로 직접 부를 수도 있습니다.

| Skill | 언제 쓰나 |
|---|---|
| `g23-welcome` | 처음 시작할 때 — 초기화, 실제 장보기 skill, GPTERS 스타일 4주 로드맵 HTML, OT 초안까지 진행합니다 |
| `g23-missions` | 이번 주 무엇을 해야 하는지 확인할 때 |
| `g23-thinking-partner` | 내 반복 업무에서 skill 후보를 고를 때 (막히면 비슷한 k-skill 사례를 자동으로 찾아 보여줍니다) |
| `skill-creator` | 고른 후보를 실제 SKILL.md로 만들 때 |
| `g23-case-writer` | 사용 기록으로 사례글을 쓸 때 |

## 4주 후 손에 남는 것

- k-skill을 응용한 나만의 업무 skill 3개
- 각 skill의 짧은 사용 기록 (목적 / 사용 전후 / 막힌 점 / 고친 점)
- 4주 사용 경험을 담은 사례글 1개

첫날에는 장보기 skill 1개, 실제 상품 URL이 담긴 `kully-result-{닉네임}.html`, `gpters-k-skill-report-{닉네임}.html`,
OT 사례 게시글 초안이 먼저 남습니다. 장보기 skill을 이후에도 쓸지는 자유입니다.

---

## 참여 전 준비

- Claude Code 설치 완료 ([Claude Code desktop 사용법](https://youtu.be/1VLebkCcH5I?si=vFj7k-AN0GSh3Wx2))
- Node.js 18 이상
- 인터넷 연결 (마켓컬리 실제 상품 검색에 사용)
- 터미널에서 명령을 실행해본 경험
- Claude Code로 간단한 파일 수정·문서 생성을 시도해본 경험
- skill을 직접 만들거나 수정해본 경험
- [k-skill 레포](https://github.com/NomaDamas/k-skill) 한 번 둘러보기

막히면 오픈카톡방에서 물어보세요: https://open.kakao.com/o/g1hHyaBi
