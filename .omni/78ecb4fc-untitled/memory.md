# Workspace Context

<!-- This file is auto-maintained. The Repositories section is refreshed -->
<!-- by the system. The AI should maintain Environment & Key Discoveries. -->

**Workspace root (absolute path):** `/home/workspaces/conversations/78ecb4fc-f4f7-400d-a996-e2454cc37674`

## Repositories

- **`from-carbon-to-metro/`** — Branch: `omni/78ecb4fc/from-carbon-to-metro`, Remote: `sofiayan0523/from-carbon-to-metro`
  - > 2026 捷運盃黑客松「玩點生活・智慧串聯」創新應用競賽 — App Mockup

- **`personal-auto/`** — Branch: `omni/78ecb4fc/personal-auto`, Remote: `sofiayan0523/personal-auto`

- **`sofia-s-blog/`** — Branch: `omni/78ecb4fc/sofia-s-blog`, Remote: `sofiayan0523/sofia-s-blog`
  - **URL**: https://lovable.dev/projects/REPLACE_WITH_PROJECT_ID

## Environment & Tools

- `from-carbon-to-metro/` is a static GitHub Pages prototype repo with no build step; local preview works with `python3 -m http.server 4173 --bind 127.0.0.1`.
- GitHub Pages for `sofiayan0523/from-carbon-to-metro` deploys from `main` branch root via built-in `pages-build-deployment`; production URL is `https://sofiayan0523.github.io/from-carbon-to-metro/`.
- `from-carbon-to-metro/` offline zip regeneration should use `python3 -m zipfile -c offline/from-carbon-to-metro-offline.zip from-carbon-to-metro`; the workspace does not have the `zip` binary.

## Key Discoveries

- 捷運盃黑客松決賽 prototype requirement: concept prototype is 40% of final score (technical feasibility 20% + UX 20%), due 2026-08-24 12:00 with prototype URL, testing steps, and Office 2024 PPTX; official rules say final computer has no internet, so offline fallback is mandatory.
- 捷運盃黑客松 Phase 3 implementation commit `c33f6b9` adds a local carbon trip simulator using `90 gCO2e/km`, 5kg -> 1.2x and 10kg -> 1.5x green multiplier thresholds, and remaining kg/km progress UI.
- Z App decision subtasks: decision detail UI queries `entity_tasks.entity_type="decision"` even though the backing table is `minutes`; when creating tasks for a decision/minutes record, set `entity_type` to `decision` and `entity_id` to the minutes ID.
- 捷運盃黑客松 prototype repo is cloned locally at `from-carbon-to-metro/`; harness implementation branch is `omni/78ecb4fc/from-carbon-to-metro`, target branch is `main`, and Phase 0 delivery strategy is documented in `from-carbon-to-metro/docs/delivery-strategy.md`.
- 捷運盃黑客松 prototype source is remote repo `sofiayan0523/from-carbon-to-metro` (GitHub Pages URL `https://sofiayan0523.github.io/from-carbon-to-metro/`); Phase 1 implementation commit `b3e7b7c` upgrades it to a static HTML/CSS/JavaScript app shell with four navigable areas and bundled local CJK font assets plus OFL license text for offline/headless QA readability.
- 捷運盃黑客松 PR #1 已於 2026-06-30T01:35:25Z 由 Sofia 合併到 `main`（merge commit `d502b6b`）；GitHub Pages 已於 01:36:07Z 完成部署；production `https://sofiayan0523.github.io/from-carbon-to-metro/` 確認服務 Phase 6 內容（四個 nav、MetroNotoTC 字型、proof flow、離線包）；Z human-merge ticket `f9380036` 已 resolved；harness 全部完成。
- Z App Profile IDs: Sofia's actual human profile ID is `54d58944-1c93-4711-9a90-0753b42e2b17` (@Sofia), whereas her Personal AI profile ID is `f165fb13-9874-1837-fc1b-7de9a1aa58bb` (Sofia Personal AI).
- 捷運盃黑客松 harness-dev loop was marked `# DONE` on 2026-06-29T19:07Z and independently verified complete on 2026-06-29T19:56Z after Phase 0-6 reviewer PASS, QA fallback PASS 5/5, Dev Monitor=false, and PR/Z human-merge handoff completed; remaining action is Sofia merge of PR #1 and post-merge GitHub Pages verification.
- 捷運盃黑客松 PM Z card: active decision/minutes ID is `9fae481f-ac84-4be8-a90c-5317ce351a1a`; duplicate empty card `a0b32763-3db4-4109-8cf1-338cc1b0cf84` was archived on 2026-06-26.
- 捷運盃黑客松 QA fallback sub-loop `758a4e76-905d-43c4-8bc1-2ff4e2e7c328` was created on 2026-06-29T18:16Z with model `gpt-5.5` to test local/offline prototype surfaces while PR #1 remains human-merge pending.
- 捷運盃黑客松 QA report `.omni/harness-dev/qa.md` completed on 2026-06-29T18:27Z: local fallback (`4173`) and offline package (`4174`) both passed desktop/mobile, proof privacy, no external runtime dependency, and no OPEN bugs; production still needs post-merge verification.
- 捷運盃黑客松 Phase 5 implementation commit `c355c04` adds a local Numbers proof/privacy flow with opt-in consent, de-identified payload, deterministic demo hash, fixed proof timestamp, dynamic audit trail, and optional Capture/Numbers live integration slot while preserving offline fallback.
- 捷運盃黑客松 Phase 2 implementation commit `ab39d64` adds a local deterministic AI route recommendation flow: six mock merchants, filter/preference/sort controls, dataset-rendered pins, merchant details, and points earn/spend simulation with no external API dependency.
- 捷運盃黑客松 Phase 4 implementation commit `9fb2e84` adds a local dynamic green-point report, task progress, achievements, JS-rendered trend chart, and share-card modal; completing trips updates home and carbon dashboard state from the same offline demo model.
- 捷運盃黑客松 Phase 6 implementation commit `fd9a4e5` adds judge-facing `TESTING_STEPS.md`, `SUBMISSION_CHECKLIST.md`, offline instructions/manifest, and `offline/from-carbon-to-metro-offline.zip` (`sha256=ffb9971e700dc1c92a5671afa498621207c67a70da4b2c890677905ec0c24559`) while documenting that GitHub Pages production updates after merge to `main`.
- 捷運盃黑客松 2026-06-30 UI/UX refresh replaces `from-carbon-to-metro/index.html` with Sofia's bundled four-tab prototype (`今天` / `路線` / `減碳` / `我的`), localizes React/ReactDOM/Babel into `assets/vendor/`, adds a local share dialog fallback, and regenerates `offline/from-carbon-to-metro-offline.zip` with `sha256=19e936ddaa5f5ca882380f7b5b9963054025ff0ee4d4122f9bd6f48f8eed5fe3`.

## Harness Dev

In this conversation, the AI agent operates as a state machine with three roles:
- **Developer (開發員)** → gpt-5.5: Implements code phase-by-phase, deploys, fixes bugs
- **Reviewer (審查員)** → claude-opus-4-7: Code reviews in separate sub-loops (context reset)
- **QA Tester (測試員)** → gpt-5.5: Agent browser testing, writes qa.md

Model delegation: main loop = Developer.
Review/QA = one-shot sub-loops with respective models.
State is tracked via dev-plan.md phase statuses and dev-diary.md last entry.
Artifacts directory: .omni/harness-dev/
Auto merge & deploy: no — from config.md
Dev monitor: no — from config.md
Harness run id: 3fb9148d-b1a1-49a6-9a28-d87daacd6576


## Installed Skills

- **`aeo-assessment`** (system)
- **`agent-readiness-generator`** (system)
- **`ai-bot-traffic`** (system)
- **`dev-monitor`** (system)
- **`doc-coauthoring`** (system)
- **`frontend-design`** (system)
- **`google-ads`** (system)
- **`google-workspace`** (system)
- **`gov-projects-search`** (space)
- **`harness-agent`** (system)
- **`harness-dev`** (system)
- **`harness-execution`** (system)
- **`harness-plan`** (system)
- **`harness-supervisor`** (system)
- **`image-generation`** (system)
- **`internal-comms`** (system)
- **`line-messaging`** (system)
- **`meta-ads`** (system)
- **`morning-brief`** (space)
- **`ms-office-suite`** (system)
- **`omni-help`** (system)
- **`pdf`** (system)
- **`short-video`** (system)
- **`skill-creator`** (system)
- **`theme-factory`** (system)
- **`webapp-testing`** (system)
- **`z-agent-ticket-creation`** (system)
- **`z-check-comment`** (system)
- **`z-report-status`** (system)
- **`z-sync`** (system)
- **`z-ticket-check`** (system)
- **`z-writing-rules`** (system)


---
_Last system refresh: 2026-06-30 09:59 UTC_
