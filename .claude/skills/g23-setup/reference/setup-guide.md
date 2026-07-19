# 환경별 셋업 참고 — Windows/Mac 터미널 · Node 18 · Python/uv

> `g23-setup` 본문에서 필요할 때만 열어본다. 매 세션 자동으로 읽지 않는다.

## 1. Windows/Mac 터미널 차이 — g23-setup ③(시스템 감지) 단계에서 필요할 때만

- **macOS**: 터미널 앱 상관없이(Terminal/iTerm2 등) Claude Code가 그대로 동작. 기본 셸은 zsh.
- **Windows**: 터미널이 여러 종류(PowerShell / Git Bash / WSL) — 참가자가 뭘 쓰는지에 따라 명령 문법이 갈린다(경로 구분자, `ls` vs `dir`, 따옴표 규칙 등). Claude Code 자체는 셋 다에서 동작하지만, **명령 예시를 안내할 땐 참가자가 쓰는 터미널에 맞춰야 한다** (CLAUDE.md "bash를 전제하지 않는다" 원칙).
- 확실치 않으면 "지금 쓰는 터미널이 뭔가요? (PowerShell / Git Bash / WSL)"로 확인하고 그 하나로 통일해서 안내한다.

## 2. k-skill 설치·체험 — Node 18 이상과 플러그인 설치 (g23-setup ⑤)

k-skill 플러그인 설치와 `/k-skill:market-kurly-search` 같은 체험 실행은 Node 18 이상과 인터넷 연결이 필요하다.

- 버전 확인: `node --version` → `v18` 이상이면 통과
- Node가 없거나 18 미만이면 스터디 시간에 장시간 설치를 시도하지 않는다. 설치는 실습 후 리더 안내에 따라 잇고, 셋업은 다음 단계로 넘어간다.
- 인터넷이 잠시 끊기면 한 번만 재시도한다.
- 설치 명령은 둘 다 필요하다.
  ```text
  /plugin marketplace add NomaDamas/k-skill
  /plugin install k-skill@k-skill
  ```
- 첫 명령 뒤 `/k-skill:market-kurly-search`가 안 보이면 두 번째 install 명령 누락부터 확인한다.
- 체험은 **"설치가 되고 한 번 돌아간다"까지만** 확인한다. 결과 CSV·표·HTML 같은 산출물을 만들지 않는다.

## 3. Python이 필요해질 때 — uv 컨벤션 (드묾, 온디맨드 전용)

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
