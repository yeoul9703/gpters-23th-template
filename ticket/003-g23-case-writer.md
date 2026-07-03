---
id: 003
title: g23-case-writer — k-윤문 톤 사례글, AI slop 제거
type: skill
status: todo
created: 2026-07-03
---

## 뭘 하려는가 (한 줄)

사례 게시글을 쓰되, k-윤문 스타일을 반영해 "AI가 지어낸 티" 안 나는 글로.

## 왜 / 언제 쓰는 일인가

이미 `.claude/skills/g23-case-post-writer/` 존재 → **개선 티켓** (이름은 case-writer 로 정리 여부 결정).
핵심은 톤: 뻔한 도입부·과장·불릿 남발 같은 AI slop 을 걷어내고
실제 사용 기록(전·후, 막힌 점, 고친 점)에 붙은 담백한 글.

트리거: "사례글 써줘", "후기", "경험 정리"

## 할 것 (체크리스트)

- [ ] 기존 SKILL.md 흐름 확인
- [ ] "k-윤문" 이 구체적으로 뭘 뜻하는지 규칙화 (금지 표현·문장 길이·구조)
- [ ] AI slop 체크리스트 추가 (도입 상투구, 억지 정리, 과장 형용사 등)
- [ ] examples/case-post-notes-template.md 실제 기록으로 초안 1개 써보기
- [ ] 이름 case-post-writer → case-writer 통일할지 결정

## 막힌 점 / 메모

- "k-윤문" 정의를 참가자와 한 번 맞춰야 함 (샘플 문단 1~2개 필요)
