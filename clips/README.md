# clips — 지피터스 사례 클리핑

지피터스 "베스트 사례"·"ax" 사례 중 **진짜 쓸모 있는 글**만 모아둔다.
많이 모으는 게 목적이 아니다. 나중에 내 skill/업무에 써먹을 것만.

## 클리핑 하는 법

1. `_template.md` 를 복사해 `NNN-짧은-슬러그.md` 로 저장 (다음 연번).
2. **링크·왜 클립했나·내 업무에 어떻게** 세 줄만 있어도 충분. `## 글쓰기에서 훔칠 점` 도 남기면 좋다.
3. **`## 원문 발췌` 는 AI가 다시 쓴 문장이 아니라 원문을 그대로 복사한다.** 문체 레퍼런스가 목적이라 이 부분만큼은 요약·재구성 금지.
4. **`## 원문 전문` 에 기사 본문 전체를 문단 그대로 붙여넣는다.** 발췌 2~3줄만으론 글 전체의 구성·논증 흐름이 안 보인다. `uv run .claude/skills/gpters-clipper/scripts/fetch_post.py "<원본 URL>"` 의 stdout을 그대로 쓰고(WebFetch는 모델이 요약·재구성하므로 금지), **4-backtick 펜스(````)**로 감싸 본문 안 코드블록에도 구조가 깨지지 않게 한다. 스크립트가 사이트 셸을 걸러내고 본문만 준다 — 단, 끝부분에 그 글의 댓글이 이어질 수 있다(잘라내도 되고, 애매하면 그대로 둔다).
5. 실제로 티켓으로 옮겨 작업하게 되면, 티켓에서 이 클립을 링크한다.

## 문체 레퍼런스

- [`_style-reference.md`](_style-reference.md) — 클립 50개에서 뽑은 "AI 티 안 나는 글" 공통 규칙 (g23-case-writer 근거)

## 사무직 보편 업무 예시 찾기

특정 직군이 아닌 사무직이면 공감할 업무(이메일·문서관리·검수·보고서·HR 등) 사례만 보고 싶으면 `tags`에 `office-general`이 붙은 클립을 찾는다 (`grep -l "office-general" clips/*.md`, 25개). 경위: [[022-clip-office-worker-skill-examples]].

## 모은 클립 (63, task 014 · 2026-07-03 / 원문 발췌 추가 · task 024 · 2026-07-04 / 원문 전문 추가 · task 026 · 2026-07-14 — `scripts/fetch_post.py`(uv Python + selector)로 51개 전부 재백필, 전수 검증 51/51 clean. 경위: [[026-clip-full-body-text]] / 사무직 보편 업무 관점 12개 추가 + 기존 13개 office-general 재태깅 · task 022 · 2026-07-14)

- [`001-government-report-loop-engineering.md`](001-government-report-loop-engineering.md) (ax) — 정부과제 최종 보고서 작성을 루프 엔지니어링으로 해보기
- [`002-icp-reverse-design-outbound.md`](002-icp-reverse-design-outbound.md) (ax) — 자사 데이터로 ICP를 거꾸로 설계하고, 아웃바운드 타깃을 하루 만에 뽑은 이야기
- [`003-persona-ux-improvement-loop.md`](003-persona-ux-improvement-loop.md) (ax) — 가상 페르소나 5명으로 설치 UX를 하루 만에 갈아엎은 개선 루프
- [`004-ai-era-archetype-test.md`](004-ai-era-archetype-test.md) (ax) — AI 시대 아키타입 5가지, 나의 아키타입은? (자가진단테스트)
- [`005-dinner-scheduler-claude-code.md`](005-dinner-scheduler-claude-code.md) (ax) — "회식 날짜 잡기 너무 귀찮아서" 비개발자가 Claude Code로 4일 만에 앱을 만든 이야기
- [`006-vibecoder-git-superpowers.md`](006-vibecoder-git-superpowers.md) (ax) — 바이브코더의 깃 협업, superpowers를 뜯어서 정리해봤습니다
- [`007-three-ai-judges-scoring.md`](007-three-ai-judges-scoring.md) (ax) — AI 심사위원을 3명 고용했더니 생긴 일
- [`008-finance-automation-harness.md`](008-finance-automation-harness.md) (ax) — 나는 검토만 했는데, AI가 재무 자동화를 끝냈다 — 비결은 '하네스'였다
- [`009-loop-engineering-content-quality.md`](009-loop-engineering-content-quality.md) (ax) — loop 엔지니어링이 뭔데? 일단 콘텐츠 품질 개선에 붙여본 기록
- [`010-codex-qa-loop-bugs.md`](010-codex-qa-loop-bugs.md) (ax) — 코덱스 QA 루프 활용 · 클로드코드에서 '눈에 안 보이는 버그' 잡기
- [`011-shortform-video-real-problem.md`](011-shortform-video-real-problem.md) (ax) — AI에게 숏폼 영상을 맡겼는데, 진짜 문제는 "만드는 것"이 아니었다
- [`012-rona-landing-page-skill.md`](012-rona-landing-page-skill.md) (ax) — 로나로 GPTers 랜딩페이지 스킬 만들기
- [`013-scattered-info-operations-hub.md`](013-scattered-info-operations-hub.md) (ax) — 이메일·메신저·시트 흩어진 정보, AI에게 "모아줘" 했더니 운영허브가 됐어요
- [`014-month-end-close-three-tweaks.md`](014-month-end-close-three-tweaks.md) (ax) — 로나(Rona) 스킬을 그대로 따르지 않은 3가지 — 월간 결산 자동화 후기
- [`015-storybook-secretary-in-hours.md`](015-storybook-secretary-in-hours.md) (ax) — 글 한 편을 '읽어주는 그림책'으로 바꾸는 비서를 2시간 반 만에 만들었어요
- [`016-ai-terms-shorts-workflow.md`](016-ai-terms-shorts-workflow.md) (ax) — AI 기초 용어를 '쇼츠 시리즈'로 찍어내는 워크플로우
- [`017-rona-vs-hyperframes-comparison.md`](017-rona-vs-hyperframes-comparison.md) (ax) — Rona를 활용해 Hyperframe 영상 비교해보기
- [`018-recruitment-video-business-clarity.md`](018-recruitment-video-business-clarity.md) (ax) — "[Rona 스킬] 채용 소개 영상 하나 만들려다, 회사의 사업 방향이 정리된 이야기"
- [`019-db-privacy-law-check.md`](019-db-privacy-law-check.md) (ax) — Rona로 'DB 법 점검 스킬'을 만들어, 우리 서비스 DB를 개인정보보호법 기준으로 까봤습니다
- [`020-reversing-paid-course-free.md`](020-reversing-paid-course-free.md) (ax) — 유료 강의를 AI로 리버싱해 무료로 학습하기
- [`021-baseball-statusline-claude-custom.md`](021-baseball-statusline-claude-custom.md) (ax) — 야구... 좋아하세요? 취향 확실한 MZ의 클로드 사용법 (Statusline 스코어 보드)
- [`022-google-indexing-auto-monitor.md`](022-google-indexing-auto-monitor.md) (ax) — 구글 색인 문제, 매일 자동으로 감시하고 '진짜 고칠 것'만 골라내기
- [`023-claude-code-ad-video.md`](023-claude-code-ad-video.md) (ax) — "[이게되네] ClaudeCode로 제대로 된 광고 영상 만들기"
- [`024-webinar-review-automation-ppodung.md`](024-webinar-review-automation-ppodung.md) (ax) — 지피터스 웨비나후기 정리, OpenClaw 뽀둥이가 후기리뷰 자동화했어요
- [`025-codex-remote-mobile-control.md`](025-codex-remote-mobile-control.md) (best) — Codex Remote 사용법 — 출근길 폰으로 집 컴퓨터의 코덱스 작업 이어가기
- [`026-jeditor-ai-detail-page.md`](026-jeditor-ai-detail-page.md) (best) — 제디터 사용법과 요금 총정리 — 상품 설명 하나로 AI 상세페이지 만들기
- [`027-loop-engineering-six-parts.md`](027-loop-engineering-six-parts.md) (best) — 루프 엔지니어링이란? 클로드 코드로 'AI를 돌리는 시스템' 만드는 6가지 부품
- [`028-content-loop-source-automation.md`](028-content-loop-source-automation.md) (best) — 매일 반복하던 콘텐츠 작성, AI '루프'로 소스 찾기부터 자동화한 방법
- [`029-grumpy-agent-team-experiment.md`](029-grumpy-agent-team-experiment.md) (best) — AI 에이전트 협업, 한 명을 까칠하게 만들면 일을 더 잘할까
- [`030-autonoma-e2e-ai-verification.md`](030-autonoma-e2e-ai-verification.md) (best) — AI가 "다 됐어요" 할 때가 제일 무섭습니다 — 오픈소스 E2E 검증 Autonoma 써본 후기
- [`031-loop-engineering-for-pm.md`](031-loop-engineering-for-pm.md) (best) — 프롬프트 다음은 루프 엔지니어링 — PM이 'AI가 매번 좋아지는 시스템'을 만드는 법
- [`032-codex-record-replay-skills.md`](032-codex-record-replay-skills.md) (best) — Codex Record & Replay 사용법 — 반복 작업을 녹화하면 재사용 스킬이 됩니다
- [`033-claude-tag-vs-openclaw.md`](033-claude-tag-vs-openclaw.md) (best) — Claude Tag vs OpenClaw 비교 — 팀 슬랙 에이전트와 개인 로컬 에이전트
- [`034-chatgpt-dreaming-memory.md`](034-chatgpt-dreaming-memory.md) (best) — ChatGPT 메모리 'Dreaming' 완벽 정리
- [`035-gemini-deep-research-game-sound.md`](035-gemini-deep-research-game-sound.md) (best) — 2회차 립리서치 과제
- [`036-organizing-102-videos-structure.md`](036-organizing-102-videos-structure.md) (best) — "[3부작 1편] GPTers 22기 영상 102개를 정리해보니, 도구보다 구조가 보였습니다"
- [`037-good-vs-risky-automation.md`](037-good-vs-risky-automation.md) (best) — "[3부작 2편] 좋은 AI 자동화와 위험한 AI 자동화를 가르는 기준"
- [`038-ai-automation-as-os.md`](038-ai-automation-as-os.md) (best) — "[3부작 3편] 그래서 저는 AI 자동화를 운영체계처럼 다루기로 했습니다"
- [`039-income-tax-helper-from-docs.md`](039-income-tax-helper-from-docs.md) (best) — 공식 수록형식 문서를 AI에게 먹여 만든 '종합소득세 신고도우미'
- [`040-notion-replacement-work-os.md`](040-notion-replacement-work-os.md) (best) — "[Claude Code] 노션 구독료 0원! 사무실 맥미니에 우리 팀 업무 OS를 올린 후기"
- [`041-capacitor-ios-app-4day-launch.md`](041-capacitor-ios-app-4day-launch.md) (best) — Claude Code로 웹앱을 iOS 앱으로 — Capacitor + App Store 심사 4일 출시기
- [`042-nonmajor-todo-app-cloud-deploy.md`](042-nonmajor-todo-app-cloud-deploy.md) (best) — 비전공자(공인중개사)가 To-Do 앱을 직접 만들고 클라우드 배포까지 성공한 후기
- [`043-ai-multitask-3x-speed.md`](043-ai-multitask-3x-speed.md) (best) — "\"AI 켜놓고 딴짓합니다\" 내가 남들보다 일 3배 빨리 끝내는 이유"
- [`044-synthetic-persona-format-validation.md`](044-synthetic-persona-format-validation.md) (best) — 설문 없이 가상 고객 반응 3,400건 — 합성 페르소나로 신규 포맷 검증한 실전기
- [`045-ai-data-wipe-hook-guard.md`](045-ai-data-wipe-hook-guard.md) (best) — "\"되돌려줘\" 한 마디에 AI가 분류한 데이터를 다 날렸어요 (바우처 웹앱 2편)"
- [`046-counseling-voucher-webapp-2days.md`](046-counseling-voucher-webapp-2days.md) (best) — 코딩 모르는 자동화 담당자가 이틀 만에 상담센터 행정 웹앱을 배포했어요 (바우처 웹앱 1편)
- [`047-claude-hooks-obsidian-journal.md`](047-claude-hooks-obsidian-journal.md) (best) — Claude Code 훅으로 옵시디언 업무 일지 자동화하기
- [`048-instagram-cardnews-8slide-pipeline.md`](048-instagram-cardnews-8slide-pipeline.md) (best) — "[활용 사례] Claude로 인스타 카드뉴스 8슬라이드 자동 생성한 후기"
- [`049-interview-multiagent-skill-combo.md`](049-interview-multiagent-skill-combo.md) (best) — 스킬로 스킬을 만든 하루 — 인터뷰형 스킬과 멀티에이전트 스킬 조합
- [`050-ralph-wiggum-goal-content-loop.md`](050-ralph-wiggum-goal-content-loop.md) (best) — 랄프 위검 방식으로 GSC 트래픽 2배 콘텐츠 무한 생성 — Claude Code /goal 활용기
- [`051-chatbot-vs-agent-openclaw-class40.md`](051-chatbot-vs-agent-openclaw-class40.md) (ax) — 뽀짝이의 OpenClaw 수업 #40 — 챗봇과 에이전트의 결정적 차이 (gpters-clipper 스크립트 파이프라인 검증용, task 026)
- [`052-inquiry-alert-loop-zero-miss.md`](052-inquiry-alert-loop-zero-miss.md) (ax, office) — 매번 까먹던 교육 문의, Claude Code로 '놓침 0' 자동 알림 루프 만들기
- [`053-company-doc-detect-approve-loop.md`](053-company-doc-detect-approve-loop.md) (ax, office) — 회사 소개 문서를, '감지→판정→승인' 루프로 자동 업데이트 되게 바꾸는 시도
- [`054-inspection-work-self-grading-loop.md`](054-inspection-work-self-grading-loop.md) (ax, office) — 매주 수 시간 걸리던 검수 업무, 루프 엔지니어링으로 자동 채점 루프 만들기
- [`055-corporate-research-self-grading-loop.md`](055-corporate-research-self-grading-loop.md) (ax, office) — 매주 반복하던 기업 리서치를, AI가 스스로 채점하는 '루프'로 만들었어요
- [`056-daily-briefing-loop-scattered-work.md`](056-daily-briefing-loop-scattered-work.md) (ax, office) — 매일 아침 흩어진 업무를 한 곳에 — AI에게 '데일리 브리핑 루프'를 맡긴 이야기
- [`057-rona-repetitive-tasks-automation.md`](057-rona-repetitive-tasks-automation.md) (ax, office) — 로나와 반복 업무 자동화하기
- [`058-automatic-mail-sending-failsafe.md`](058-automatic-mail-sending-failsafe.md) (ax, office) — 자동 메일 발송 시스템 구축: 실패 방지와 검증까지
- [`059-sales-report-telegram-automation.md`](059-sales-report-telegram-automation.md) (ax, office) — 챗봇으로 매출 취합 리포트
- [`060-result-report-claude-skill.md`](060-result-report-claude-skill.md) (ax, office) — 결과보고서, 클로드 스킬로 쉽게 하기
- [`061-hr-vacation-faq-guidebook.md`](061-hr-vacation-faq-guidebook.md) (ax, office) — 반복되는 휴가 질문, 이제 AI로 구성원 가이드북 만들기
- [`062-newsroom-bot-meeting-to-script.md`](062-newsroom-bot-meeting-to-script.md) (ax, office) — AI로 회의부터 기사 작성, 영상 생성까지 한방에!
- [`063-team-wiki-self-learning-loop.md`](063-team-wiki-self-learning-loop.md) (ax, office) — 우리 팀 위키는 매일 새벽 4시 40분에 혼자 공부해요 — 문서가 스스로 배우게 만들기까지 한 달
