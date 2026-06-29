# 決賽 prototype 交付策略

最後更新：2026-06-29

本文件記錄「從碳客變捷客」決賽 prototype 的 Phase 0 交付決策。目標是讓後續開發、審查與 QA 可以用同一組依據判斷線上展示、離線備援與權限風險。

## 現況

- Repository：`sofiayan0523/from-carbon-to-metro`
- Default branch：`main`
- Workspace 開發分支：`omni/78ecb4fc/from-carbon-to-metro`
- Production URL：<https://sofiayan0523.github.io/from-carbon-to-metro/>
- GitHub Pages 來源：`main` branch `/`
- GitHub Pages 狀態：`built`
- CI / Pages workflow：GitHub 內建 `pages-build-deployment`
- 現有程式：`index.html` 與 `README.md`
- 現有技術型態：純 HTML/CSS/JavaScript，無 build step，無外部 API，無登入；AI 路線推薦使用本機 mock 商家資料集與 deterministic scoring；碳足跡使用 `90 gCO₂e/km × distance` 本機公式與 5 kg / 10 kg 綠點倍率門檻；今日綠點報告、任務進度、成就徽章、14 天趨勢圖、分享卡與可信證明都由本機 demo state 驅動；可信證明使用固定 demo timestamp、去識別 payload、deterministic demo hash 與 opt-in 隱私同意，不保存完整起訖站、商家、精確時間或個人識別碼；繁中文字型已在 repo 內本地打包，避免離線或 headless QA 環境缺字

## 線上展示策略

預設使用 GitHub Pages 作為線上 prototype 連結。原因是：

- 決賽交付需要一個可開啟的 prototype URL。
- 現有 repo 已啟用 GitHub Pages，且 URL 已可回應 `200 OK`。
- Prototype 不含真實會員、票務、支付或商家資料，因此不需要把主 demo 放在登入牆後。
- 以靜態網站交付可降低決賽前部署失敗風險。

後續每個開發 phase 仍應遵守：

- 主 demo 流程不得依賴外部 API 才能完成。
- 碳足跡與綠點倍率需保留本機公式 fallback：`90 gCO₂e/km`、5 kg → 1.2x、10 kg → 1.5x。
- 今日綠點報告、任務成就與成果分享卡需保留本機 state fallback，確保沒有網路時仍能完成評審操作路徑。
- Numbers proof 需保留本機去識別 payload、demo hash 與 audit trail fallback；任何 Capture / Numbers API 註冊都只能放在 optional live slot，不得阻塞主 demo。
- 若加入任何網路整合，只能作為 bonus 或 live slot，必須保留 deterministic fallback。
- PR target 固定為 `main`，merge 後由 GitHub Pages 內建 workflow 更新 production。

## Access-control 策略

預設採公開 demo，不加密碼、不要求登入。

公開 demo 的界線：

- 可展示：假資料、去識別化通勤情境、mock 商家、mock proof、可解釋的 AI scoring。
- 不可展示：真實 Go App 會員資料、真實票務紀錄、真實付款資訊、任何未授權品牌素材或 private credentials。

如果後續 Sofia 或主辦方要求限制存取，處理方式是：

- 保留一條公開 teaser 或投票用頁面。
- 另建受限 prototype URL 或簡易 demo password，但不可讓評審主流程依賴公司 SSO。
- 同步更新 `TESTING_STEPS.md`，確保評審能不靠人工協助完成測試。

此需求目前不是 Phase 0 blocker，因為現有公開 prototype 已符合送件 URL 的最低需求，且內容可設計為不含敏感資料。

## 離線備援策略

官方規則指出決賽主辦單位電腦不提供網路，因此離線備援是必做項目。

離線 package 的最低標準：

- 可直接開啟 `index.html` 完成主 demo path。
- 所有 CSS、JS、字型、圖像與資料都在 repo/package 內。
- 不依賴 CDN、外部圖片、第三方 script、live API 或 blockchain RPC。
- 若有 bonus live integration，必須在沒有網路時自動降級為 mock proof / demo record；目前 proof flow 已固定示範時間並用去識別 payload 產生 deterministic demo hash。

Phase 6 交付時已產出：

- `offline/from-carbon-to-metro-offline.zip`：包含 `index.html`、文件、delivery strategy、離線說明與本地字型。
- `TESTING_STEPS.md`：包含線上測試、離線測試、桌面 / 手機檢查、隱私與素材檢查。
- `SUBMISSION_CHECKLIST.md`：列出 prototype URL、離線包、PPTX、測試步驟、素材授權、proof privacy 與 merge 前檢查。
- `offline/README.md` 與 `offline/package-manifest.txt`：說明離線包內容、使用方式與重新打包流程。

## 本地開發與驗證

目前 repo 沒有 build step，可用靜態 server 驗證：

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

再開啟：

```text
http://127.0.0.1:4173/
```

Phase 0 已完成的 smoke test：

- `curl -fsSI http://127.0.0.1:4173/` 回傳 `HTTP/1.0 200 OK`。
- Browser snapshot 可讀到三個既有畫面：首頁・今日綠點報告、AI 點數路線地圖、個人碳足跡儀表板。
- Production URL `https://sofiayan0523.github.io/from-carbon-to-metro/` 回傳 `HTTP/2 200`。

## 後續 phase 的交付要求

每個 phase 完成後要保留以下性質：

- 可本地開啟。
- 可由 GitHub Pages 靜態部署。
- 主 demo path 離線可用。
- 沒有 secrets、tokens、真實會員資料或未授權素材。
- 若新增 npm/build tool，必須同步更新本文件與 `README.md` 的本地執行方式。
