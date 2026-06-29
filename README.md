# 從碳客變捷客 (From Carbon to Metro)

> 2026 捷運盃黑客松「玩點生活・智慧串聯」創新應用競賽 — App Mockup

## 線上預覽

🔗 **[Live Demo](https://sofiayan0523.github.io/from-carbon-to-metro/)**

## 本地預覽

目前專案是純靜態 HTML/CSS/JavaScript，可直接開啟 `index.html`，或用本機靜態 server 預覽：

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

開啟 <http://127.0.0.1:4173/>。

## 決賽交付策略

決賽 prototype 採 GitHub Pages 作為線上展示，並在最後交付離線備援包，確保主辦單位電腦沒有網路時仍可完成 demo。細節見 [`docs/delivery-strategy.md`](docs/delivery-strategy.md)。

## 專案介紹

「從碳客變捷客」是整合於台北捷運 Go App 的 AI 智慧服務模組，結合**個人化點數導航**與**碳足跡回饋**雙引擎：

- 🤖 **AI 點數路線引擎** — 根據用戶通勤路線推薦沿途賺點 / 用點商家
- 🌿 **碳足跡綠點加成** — 將以捷運取代私人運具的碳節省量轉換為捷運點乘數加成
- 📊 **今日綠點報告** — 個人化儀表板，整合減碳成績、推薦路線、社群排名

## 四大可導航區塊

1. **首頁・今日綠點報告** — Hero Card + AI 推薦商家清單
2. **AI 點數路線地圖** — 互動式捷運地圖 + 累點/用點/AI 推薦 Pin
3. **個人碳足跡儀表板** — 14 天減碳趨勢圖 + 等級徽章
4. **會員・可信數據證明** — 本機 demo state、去識別摘要與 proof shell

## 團隊：通勤族也想拯救地球

| 成員 | 任職單位 | 分工 |
|------|---------|------|
| 嚴世紀（隊長） | 主張數據股份有限公司 Numbers Protocol | 系統架構、AI 推薦、碳數據可信度 |
| 鍾天傑 | 連加網絡商業股份有限公司 LINE Pay | 點數經濟、支付整合、UX |
| 嚴世裕 | 台北市政府地政局 | ESG 政策對接、政府資料整合 |

## 技術

純 HTML/CSS/JavaScript（無 build step、無外部 API 依賴），任何現代瀏覽器可開啟。繁中文字型以本地 `assets/fonts/` 打包，確保離線 demo 與 QA 截圖可讀。正式產品將整合於台北捷運 Go App，串接環境部碳排係數資料集與捷運點數系統。
