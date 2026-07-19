# GPTERS HTML 디자인 가이드

> welcome이 렌더링하는 `gpters-k-skill-report-{닉네임}.html`(4주 자동화 로드맵)에서
> 일관된 GPTERS 스타일을 쓰기 위한 참조 문서다.
> **필요할 때만 열어본다. 매 세션 자동으로 읽지 않는다.**

## 단일 출처

브랜드 값의 **원본은 `reference/gpters-k-skill-report-template.html`의 `:root` 블록**이다.
새 HTML을 만들 땐 그 파일의 `:root` CSS 변수를 그대로 복사해 `<style>`에 넣는 것이
기본이다. 아래 표는 빠른 참고용 요약일 뿐, 값이 어긋나면 **template html이 맞다**
(여기 요약이 아니라). 팔레트를 바꿔야 하면 template html을 먼저 고치고 여기 요약을 맞춘다.

## 색상 (gpters-k-skill-report-template.html `:root`에서)

| 변수 | 값 | 용도 |
|---|---|---|
| `--gpters-primary` | `#eb5a10` | 주 강조색 (주황) — 링크 hover, 포인트 |
| `--gpters-primary-hover` | `#d34600` | 링크 기본색, 강조 텍스트 |
| `--gpters-primary-soft` | `#fff5f1` | 옅은 배경 (hero 그라데이션, goal 박스) |
| `--gpters-primary-soft-strong` | `#ffe0d1` | 테두리·번호 배경 |
| `--gpters-text` | `#060607` | 본문 텍스트 |
| `--gpters-text-subdued` | `#525458` | 보조 텍스트 (설명·캡션) |
| `--gpters-background` | `#f6f6f6` | 페이지 배경 |
| `--gpters-surface` | `#ffffff` | 카드·표면 |
| `--gpters-surface-subdued` | `#f3f3f3` | 옅은 카드 배경 |
| `--gpters-line` | `#e9e9e9` | 테두리·구분선 |
| `--shadow` | `0 10px 30px rgba(6, 6, 7, 0.08)` | 박스 그림자 |

## 폰트 · 타이포그래피

```
본문 폰트:   ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif
line-height: 1.65 (본문), 1.25 (제목)
줄바꿈:      word-break: keep-all; overflow-wrap: anywhere;  (한글 줄바꿈)
```
- 외부 웹폰트를 불러오지 않는다 (시스템 폰트 스택만).

## 간격 · 모양

```
보더-라디우스:  hero 24px / section 20px / card 14px / chip(pill) 999px
카드 패딩:       18px
section 패딩:    clamp(22px, 4vw, 34px)
그리드 간격:     12~14px
```

## 표(테이블)를 새로 만들 때

gpters-k-skill-report-template.html에는 표 스타일이 없다(카드 위주). 데이터 목록처럼
표가 필요하면 위 `:root` 변수를 그대로 쓰되 아래 규칙만 맞춘다.

- 헤더행 배경: `var(--gpters-primary)` / 글자색 흰색
- 데이터행: `var(--gpters-surface)`와 `var(--gpters-surface-subdued)` 교차
- 테두리: `1px solid var(--gpters-line)`
- 셀 패딩: `12px 16px`
- 상품 URL은 `<a ... target="_blank" rel="noopener noreferrer">` 링크로

## 지켜야 할 것

- **외부 CSS·JS·폰트·이미지 금지** (gpters-k-skill-report-template.html과 동일 규칙).
- `:root` 값을 여기서 임의로 바꾸지 않는다 — 브랜드 일관성의 출처는 template html.
- 새 색이 꼭 필요하면 template html에 먼저 추가하고 이 문서를 맞춘다(drift 방지).
