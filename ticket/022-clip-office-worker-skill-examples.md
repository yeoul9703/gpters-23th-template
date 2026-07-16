---
id: 022
title: "사무직 보편 업무" 스킬 예시 클리핑 점검·보강 (gpters + k-skill)
type: mission      # skill | mission | fix
status: doing       # todo | doing | done
created: 2026-07-04
---

## 뭘 하려는가 (한 줄)

미션 문서(우선 week-2.md)의 "문제 찾기/막히면" 안내가 실제 사례 없이 추상적으로만 남는 문제를, gpters + k-skill 클리핑으로 보강한다.

## 왜 / 언제 쓰는 일인가

week-2.md에 세 순간(출근 후/점심 후/퇴근 전)별 예시 skill 힌트를 넣을지 논의하다가,
"결국 예시는 gpters + k-skill 클리핑에서 가져올 건데 아직 제대로 안 됐다"는 지적이 나왔다.
`g23-thinking-partner`나 미션 템플릿이 "이런 문제엔 이런 skill" 식으로 제안하려면 실제 사례 근거가 있어야 하는데:

- 기존 `clips/` 50개([[014-clip-gpters-50]])는 g23-case-writer **문체 레퍼런스** 목적으로 뽑혀서, loop 엔지니어링·멀티에이전트·앱 배포 등 다소 고급·개발자향 사례 비중이 크다. "사무직 보편 업무"(이메일 정리, 캘린더 확인, 보고서 작성 등) 관점으로 다시 걸러보지 않았다.
- k-skill 저장소 쪽은 정적 클립이 아예 없다 — `g23-k-skills-search`가 그때그때 `k-skill-researcher`로 라이브 검색만 한다.

## 결정할 것

- [x] 기존 50개 clips 중 "사무직 보편 업무"에 맞는 것만 골라 별도 태깅/목록화할지, 새로 클리핑할지 → **둘 다** (2026-07-14, 사용자 확정: 신규 클리핑 + 기존 재태깅 병행)
- [ ] k-skill 저장소 쪽도 정적으로 몇 개 클립해둘지, 아니면 `g23-k-skills-search`의 라이브 검색에 계속 맡길지
- [ ] 이 예시들을 어디서 참조하게 할지 — `g23-missions/reference/`, `g23-thinking-partner`의 참고 포인터, 혹은 개별 week-*.md

## 조사 결과 (2026-07-14) — 신규 후보 풀 크기

"신규 50개"는 불가능하다고 판단(advisor 검토 확정). `ai-study-post` 전체/태그 목록 + 게시판별 루트(wealth·marketing·ax-lab·dev·nocode·media·chatbot·research·law) 총 10회 목록 조회로 얻은 첫 배치(각 ~15~30개, 스킬 스코프상 그 이상 긁지 않음)를 기존 51개 source URL과 대조한 결과:

**신규 — 확실한 fit (12개)**
1. 매번 까먹던 교육 문의, Claude Code로 '놓침 0' 자동 알림 루프 — `nocode/post/maebeon-ggameogdeon-gyoyug-munyi-claude-codero-nohcim-0-jadong-alrim-rupeu-kAqgb1jsliu0Va5`
2. 회사 소개 문서를 '감지→판정→승인' 루프로 자동 업데이트 — `nocode/post/attempt-change-company-introduction-yrwS1IM2hDMiffp`
3. 매주 수 시간 걸리던 검수 업무, 자동 채점 루프 — `dev/post/inspection-work-used-take-jNxuTN7fHM7ls37`
4. 매주 반복하던 기업 리서치를 AI가 스스로 채점 — `nocode/post/we-turned-corporate-research-NnVShCQx9eZrYn3`
5. 매일 아침 흩어진 업무를 한 곳에 — 데일리 브리핑 루프 — `nocode/post/maeil-acim-heuteojin-eobmureul-han-gose----aiege-deilri-beuriping-rupeu-Sz6OqBCQZpBsBp6`
6. 로나와 반복 업무 자동화하기 — `nocode/post/automate-repetitive-tasks-rona-RtzrhKy1goQC6Zf`
7. 자동 메일 발송 시스템 구축: 실패 방지와 검증까지 — `marketing/post/establishing-automatic-mail-sending-uhWQCSJ0yiRSZAi`
8. 챗봇으로 매출 취합 리포트 — `chatbot/post/sales-collection-report-using-nFXQ2c4tA5V4nHz`
9. 결과보고서, 클로드 스킬로 쉽게 하기 — `research/post/result-report-easy-claude-3DAJ6yQpLUyCi54`
10. 반복되는 휴가 질문, 이제 AI로 구성원 가이드북 만들기 — `law/post/repeated-vacation-questions-now-gnY4Ej9jc5vKX5I`
11. AI로 회의부터 기사 작성, 영상 생성까지 한방에! — `chatbot/post/meetings-article-writing-video-EmyRFrXBtWzapE5`
12. 우리 팀 위키는 매일 새벽 4시 40분에 혼자 공부해요 — `ax-lab/post/we-study-our-team-pVzHdXiSgS8tFAT`

**신규 — 애매하지만 넓히면 포함 (9개)**
13. "괜찮은데?" AI 초안, 데이터로 재보니 15번 중 13번 틀림 — `dev/post/you-okay-when-measured-cwaGKJld3PXNN6j`
14. AI가 만든 결과를 AI가 채점 — B2B 세일즈 리드 관리 — `nocode/post/why-you-shouldnt-let-bUAfzrGmKwhWluU`
15. 네이버 블로그 노출체크 클로드코드로 자동화 — `marketing/post/automate-naver-blog-exposure-cTCST3bitrQVuJn`
16. AI에게 링크드인 포스팅 초안 작성을 맡겼는데 — `marketing/post/entrusted-ai-draft-my-8bA9tlc3IDKs0wW`
17. 고객이 "뭘 적어야 하지?" 고민 않는 사건 접수 폼 만들기 — `law/post/when-customer-asks-what-9C6uSpYIee7XlTJ`
18. AI에게 유투브 요약정리를 맡겼는데 — `media/post/entrusted-ai-summarize-youtube-Sqgc0IT4fayD4sP`
19. HROS를 만들다가 AI 두 명을 토론시켜봤습니다 — `chatbot/post/creating-hros-had-two-kX3cWubMb4KvMyP`
20. "AI 전담팀 만들지 마세요" 마이리얼트립이 깨달은 것 — `ax-lab/post/dont-create-dedicated-ai-meOlbR9rj01vLWE`
21. 대한민국 현행 법령 검색 방법 — `law/post/there-way-search-current-13y6yve5DFniiBV`

**기존 51개 중 재태깅 대상 — 확실한 fit (13개)**: 001, 005, 008, 013, 014, 019, 024, 031, 039, 040, 043, 046, 047

**기존 51개 중 재태깅 대상 — 애매(넓히면 포함) (9개)**: 002, 007, 018, 022, 026, 033, 037, 038, 044

나머지(신규 목록에서 걸러진 것들과 기존 51개 중 나머지)는 개발자 툴 빌드·영상/콘텐츠 제작·마케팅 소재 제작 등으로 "사무직 보편 업무"보다는 특정 직군·고급 사례에 가까워 제외.

## 할 것 (체크리스트)

- [x] 범위 확정 — 사용자 확정(2026-07-14): "확실한 fit만"(신규 12 + 재태깅 13 = 25). 실행 스펙: [[022-clip-office-worker-skill-examples.task.json]]
- [x] 신규 후보 클립 생성 — `fetch_post.py` 순차 실행 12/12 성공(실패 0), clips/052~063 저장. gpters-clipper 절차(왜 클립했나/핵심요약/원문발췌/원문전문/내 업무에 어떻게/훔칠 점) 전부 반영.
- [x] 기존 클립 재태깅 — 001·005·008·013·014·019·024·031·039·040·043·046·047 frontmatter `tags:`에 `office-general` 추가(기존 태그는 유지, 본문 무변경).
- [x] clips/README 인덱스 갱신 — 052~063 목록 추가 + "사무직 보편 업무 예시 찾기" 절 신설(`tags: office-general` grep 안내, 25개).
- [x] 검증 — 신규 12개 전부 섹션 순서(왜 클립했나→핵심요약→원문발췌→원문전문→...→내 업무에 어떻게→훔칠 점) 확인, source URL 중복 0건, 전체 클립 63개.

## 막힌 점 / 메모

- **2026-07-14 추가**: `ticket/clips/` → `clips/`(루트)로 폴더 이동. "클리핑은 티켓과 성격이 다른 자료"라는 구분(ticket/README.md "두 종류가 있다")이 폴더 계층에도 드러나도록. `gpters-clipper`·`g23-case-writer` SKILL.md, `ticket/README.md`의 경로 참조 갱신 완료. 과거 done 티켓 본문(003/007~009/012~014/024/026/030 등)의 `ticket/clips/` 문구는 당시 기록 그대로 두고 손대지 않음(append-only 로그 관례).
- **gpters 쪽 클리핑은 done, 남은 결정 2건**: (1) k-skill 저장소 정적 클립 여부(2026-07-04 결정 미확정 그대로), (2) 이 예시들을 week-2.md 등에서 실제로 어떻게 참조하게 할지. status를 done이 아닌 doing으로 유지하는 이유.
- 신규 12개는 실패 0건으로 전부 성공(task.json의 on_block 기준 미도달). 애매한 후보 9개(신규)·9개(재태깅)는 이번엔 제외 — 필요해지면 022 조사 결과 절의 목록을 그대로 재사용.
- 이 티켓이 끝나야 [[017-week2-curriculum-alignment]]에서 보류했던 "예시 힌트"·"막히면" 섹션을 실제로 채울 수 있다 (017 자체는 문구 정합 목적으로 이미 done — 이건 그 위에 얹는 보강 작업).
- 관련이지만 다른 용도: [[020-cross-week-examples-and-tags]]는 "스터디장 사례글" 자리에 공식 커리큘럼 예시 3개를 채우는 것 — 참가자용 문제-제안 예시가 아니다.
- 관련: [[021-welcome-daily-moments-detail]] (온보딩 쪽 하루 세 시점 디테일 — 같은 "세 시점" 축을 쓰지만 논의 대상은 welcome).
- (구) 023-week1-kskill-environment-independent-wow는 삭제됨(2026-07-14) — "환경 무관" 필터 문제의식은 027 ②의 후보 조건(자격증명 불필요 등)으로 흡수. 이 022가 클리핑 예시를 고를 때도 같은 조건을 기준으로 삼으면 됨.
