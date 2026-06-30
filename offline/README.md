# 離線備援包說明

本資料夾保存「從碳客變捷客」決賽 prototype 的離線交付說明與 manifest。實際壓縮包為：

```text
offline/from-carbon-to-metro-offline.zip
```

## 使用方式

1. 將 zip 複製到沒有網路的電腦。
2. 解壓縮。
3. 進入解壓後的 `from-carbon-to-metro/` 資料夾。
4. 優先使用本地 static server：

   ```bash
   python3 -m http.server 4173 --bind 127.0.0.1
   ```

5. 開啟：

   ```text
   http://127.0.0.1:4173/
   ```

6. 如果現場電腦沒有 Python，直接開啟 `index.html` 作為 fallback。

詳細操作步驟見 zip 內的 `TESTING_STEPS.md`。

## 離線保證

- 主 demo path 不依賴外部 API、CDN、圖片、模型服務、Capture / Numbers live API 或 blockchain RPC。
- AI 推薦、碳足跡、綠點倍率、路線集章、每日綠點卡、分享卡與 proof record 都由本機 JavaScript state 驅動。
- 新版 UI/UX 的主要 bundle 位於 `index.html`；固定版本前端 runtime 已放在 `assets/vendor/`，字型資源與授權文件保留在 `assets/fonts/`。
- Proof flow 的 live integration slot 是加分展示說明，沒有網路時仍以 deterministic demo hash 完成。

## 重新產生 zip

在 repo 根目錄完成文件或程式更新後，可重新打包：

```bash
rm -rf /tmp/from-carbon-to-metro-offline
mkdir -p /tmp/from-carbon-to-metro-offline/from-carbon-to-metro
cp -R index.html README.md TESTING_STEPS.md SUBMISSION_CHECKLIST.md docs assets offline /tmp/from-carbon-to-metro-offline/from-carbon-to-metro/
rm -f /tmp/from-carbon-to-metro-offline/from-carbon-to-metro/offline/from-carbon-to-metro-offline.zip
cd /tmp/from-carbon-to-metro-offline
python3 -m zipfile -c /path/to/repo/offline/from-carbon-to-metro-offline.zip from-carbon-to-metro
```

重新打包後，請至少重跑 `TESTING_STEPS.md` 的離線測試流程。
