# 從碳客變捷客 (From Carbon to Metro)

> 2026 捷運盃黑客松「玩點生活・智慧串聯」創新應用競賽 — App Mockup

## 線上預覽

🔗 **[Live Demo](https://sofiayan0523.github.io/from-carbon-to-metro/)**

## 本地預覽

目前專案是純靜態 HTML/CSS/JavaScript。建議用本機靜態 server 預覽，確保本地字型與離線 QA 行為和 GitHub Pages 一致：

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

開啟 <http://127.0.0.1:4173/>。

如果現場電腦沒有 Python，也可以直接用瀏覽器開啟 `index.html` 作為 fallback；主 demo 邏輯仍會在本機執行。

## 決賽交付策略

決賽 prototype 採 GitHub Pages 作為線上展示，並在最後交付離線備援包，確保主辦單位電腦沒有網路時仍可完成 demo。細節見 [`docs/delivery-strategy.md`](docs/delivery-strategy.md)。

## 決賽提交包

- 線上 prototype：<https://sofiayan0523.github.io/from-carbon-to-metro/>
- 測試步驟：[`TESTING_STEPS.md`](TESTING_STEPS.md)
- 送件檢查清單：[`SUBMISSION_CHECKLIST.md`](SUBMISSION_CHECKLIST.md)
- 離線備援包：`offline/from-carbon-to-metro-offline.zip`
- 離線包說明：[`offline/README.md`](offline/README.md)

## 專案介紹

「從碳客變捷客」是整合於台北捷運 Go App 的 AI 智慧服務模組，結合**個人化點數導航**與**碳足跡回饋**雙引擎：

- 🤖 **AI 點數路線引擎** — 根據用戶通勤動線推薦沿途賺點 / 用點商家與集章任務
- 🌿 **碳足跡綠點加成** — 以 `90 gCO₂e/km × 通勤距離` 換算碳節省量，並用 5 kg / 10 kg 門檻轉成捷運點乘數加成
- 🎁 **今日綠點互動** — 完成通勤、翻每日綠點卡、累積點數與查看推薦站點
- 🔐 **Numbers 可信證明** — 以 opt-in 隱私同意呈現去識別月度 proof record、demo hash 與可重播稽核軌跡

## 四大可導航區塊

1. **今天** — 通勤減碳摘要、捷運點餘額、每日綠點卡與順路推薦
2. **路線** — 板南線站點情境、AI 商家推薦、分類篩選與綠章任務
3. **減碳** — 日 / 月 / 年報告切換、額外通勤模擬、5 kg / 10 kg 綠點加成門檻、減碳森林與 14 天趨勢
4. **我的** — 成就徽章牆、Numbers 可信證明、opt-in 控制、demo hash、稽核軌跡重播與分享卡

## 團隊：通勤族也想拯救地球

| 成員 | 任職單位 | 分工 |
|------|---------|------|
| 嚴世紀（隊長） | 主張數據股份有限公司 Numbers Protocol | 系統架構、AI 推薦、碳數據可信度 |
| 鍾天傑 | 連加網絡商業股份有限公司 LINE Pay | 點數經濟、支付整合、UX |
| 嚴世裕 | 台北市政府地政局 | ESG 政策對接、政府資料整合 |

## 技術

純 HTML/CSS/JavaScript（無 build step、無外部 API 依賴），任何現代瀏覽器可開啟。新版 UI/UX 以 bundled `index.html` 交付，前端 runtime 固定版本放在 `assets/vendor/`，字型資源則隨 bundle 與 `assets/fonts/` 授權文件一起保留，確保 GitHub Pages 與離線包都不需要 CDN。AI 路線推薦目前使用本機 mock 商家資料集，碳足跡則以本機 `90 gCO₂e/km` 公式、5 kg → 1.2x、10 kg → 1.5x 門檻運算；通勤完成、每日綠點卡、路線集章、成就徽章、趨勢圖、分享卡與可信證明都由同一組本機 demo state 驅動。Proof flow 只保留月份、減碳值、距離區間、任務類型與 demo hash，不保存完整起訖站、商家、精確時間或個人識別碼；正式產品可在使用者同意後改接 Capture / Numbers API 註冊同一類 hash。正式產品將整合於台北捷運 Go App，串接環境部碳排係數資料集與捷運點數系統。
