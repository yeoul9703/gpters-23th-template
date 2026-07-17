# 환경별 셋업 참고 — Windows/Mac 터미널 · Python/uv

> `g23-welcome` 본문에서 필요할 때만 열어본다. 매 세션 자동으로 읽지 않는다.
> 관련 논의: `context/python-setup-uv-consistency-2026-07-04.md` · 관련 원칙: `ticket/_discuss.md` P1(스킬은 가볍게, Python 사전교육 안 함)

## 1. Windows/Mac 터미널 차이 — g23-setup의 "시스템 감지" 단계에서 필요할 때만

- **macOS**: 터미널 앱 상관없이(Terminal/iTerm2 등) Claude Code가 그대로 동작. 기본 셸은 zsh.
- **Windows**: 터미널이 여러 종류(PowerShell / Git Bash / WSL) — 참가자가 뭘 쓰는지에 따라 명령 문법이 갈린다(경로 구분자, `ls` vs `dir`, 따옴표 규칙 등). Claude Code 자체는 셋 다에서 동작하지만, **명령 예시를 안내할 땐 참가자가 쓰는 터미널에 맞춰야 한다** (CLAUDE.md "bash를 전제하지 않는다" 원칙).
- 확실치 않으면 "지금 쓰는 터미널이 뭔가요? (PowerShell / Git Bash / WSL)"로 확인하고 그 하나로 통일해서 안내한다.

## 2. Python이 필요해질 때 — uv 컨벤션 (드묾, 온디맨드 전용)

대부분의 skill은 SKILL.md 한 장짜리 자연어 지시문이라 여기 해당하지 않는다. **참가자가 고른 skill 아이디어가 실행 중 Python 스크립트·라이브러리를 요구할 때만** 참고한다.

이때 그때그때 다른 방식(conda / `pip install --user` / brew python 등)으로 대응하면 참가자마다 환경이 달라져 트러블슈팅 비용이 계속 새로 든다 — **uv로 통일**한다.

**uv 설치 (최초 1회, OS별로 다름)**
- macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh` (또는 `brew install uv`)
- Windows (PowerShell): `irm https://astral.sh/uv/install.ps1 | iex`

**설치 후 실행 방식은 OS 무관 동일**
```
uv run --with <패키지명> script.py
```
- venv를 직접 만들고 activate할 필요 없음 — uv가 그때그때 격리된 환경에서 실행한다.
- 시스템에 Python이 아예 없어도 uv가 알아서 받아온다.
- `uv venv`(수동 venv 생성)는 더 무거운 경로라 기본으로 권장하지 않는다 — 기본은 `uv run --with`.
