# 決賽送件檢查清單

最後更新：2026-06-29

本清單對齊 2026 捷運盃黑客松決賽 prototype 交付需求。決賽送件截止時間為 2026-08-24 12:00，交付內容需包含 prototype URL、應用測試步驟與 Office 2024 PowerPoint 簡報。

## Prototype 交付物

- [x] 線上 prototype URL：<https://sofiayan0523.github.io/from-carbon-to-metro/>
- [x] 本地可執行 source repo：`sofiayan0523/from-carbon-to-metro`
- [x] 離線備援包：`offline/from-carbon-to-metro-offline.zip`
- [x] 測試步驟：`TESTING_STEPS.md`
- [x] 交付策略：`docs/delivery-strategy.md`
- [ ] Office 2024 PPTX 決賽簡報
- [ ] 送件前將 prototype branch 合併到 `main`，讓 GitHub Pages production 更新到最終版本

## 必做功能覆蓋

- [x] Judge-operable demo path：首頁 -> AI 路線 -> 碳足跡 -> 可信證明 -> 分享卡
- [x] AI 點數推薦：商家資料集、偏好、篩選、排序、推薦理由與累兌點模擬
- [x] 碳足跡綠點加成：`90 gCO2e/km` 公式、5 kg -> `1.2x`、10 kg -> `1.5x`
- [x] 今日綠點報告：本日 / 本月 / 本年摘要、任務、成就、趨勢圖與分享卡
- [x] Numbers Protocol 可信數據亮點：opt-in、去識別 payload、demo hash、audit trail、live integration slot
- [x] 離線 fallback：所有主流程都可在無網路狀態完成

## QA 與驗證

- [x] Local static server smoke test documented
- [x] Online URL smoke test documented
- [x] Offline package smoke test path documented
- [x] Desktop layout checklist documented
- [x] Mobile layout checklist documented
- [x] Proof privacy leak checklist documented
- [ ] Phase 6 Reviewer 審查通過
- [ ] QA Tester 以 agent browser 完成 desktop / mobile 測試
- [ ] PR opened against `main`
- [ ] Human merge completed
- [ ] Merge 後重新確認 production URL 顯示 Phase 6 版本

## 離線包內容

- [x] `index.html`
- [x] `README.md`
- [x] `TESTING_STEPS.md`
- [x] `SUBMISSION_CHECKLIST.md`
- [x] `docs/delivery-strategy.md`
- [x] `assets/fonts/NotoSansCJKtc-Regular.otf`
- [x] `assets/fonts/OFL.txt`
- [x] `assets/fonts/NOTICE.md`
- [x] `offline/README.md`
- [x] `offline/package-manifest.txt`

## 素材與授權

- [x] 未使用官方捷運 Logo 或未授權官方 UI 素材
- [x] 未使用外部圖片、音樂、地圖底圖或第三方 script
- [x] 本地繁中文字型附帶 OFL 授權全文
- [x] 商家僅作為文字 mock 情境，沒有商標圖、廣告圖或交易資料
- [x] 沒有 secrets、tokens、API key、真實會員資料、票務資料或付款資料

## 隱私與可信數據

- [x] Proof record 不保存完整起訖站
- [x] Proof record 不保存商家名稱
- [x] Proof record 不保存精確時間
- [x] Proof record 不保存精確通勤距離
- [x] Proof record 使用區間 bucket：趟數 bucket、距離 bucket
- [x] Demo hash 可離線重現，固定示範輸出為 `0x51989C8D`
- [x] Live Capture / Numbers 註冊只作為 optional slot，不阻塞主 demo

## 外部時程提醒

- [ ] 2026-07-11 workshop 後補充現場回饋與最終 demo script
- [ ] 2026-07-28 線上投票材料確認：公開 teaser、prototype 存取策略與投票推廣素材
- [ ] 2026-08-24 12:00 前完成 prototype URL、測試步驟與 Office 2024 PPTX 送件

## Merge 前檢查

- [ ] `git diff --check`
- [ ] inline JavaScript `node --check`
- [ ] 外部依賴掃描：無 `<script src>`、外部圖片、`fetch`、XHR、service worker、WebSocket
- [ ] secret scan：無 API key、token、password、private key
- [ ] 本地 server 可回應 `HTTP 200`
- [ ] 離線包解壓後可打開首頁
- [ ] GitHub Pages production merge 後可回應 `HTTP 200`
