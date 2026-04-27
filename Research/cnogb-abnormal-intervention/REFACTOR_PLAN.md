# cnogb-abnormal-intervention — Refactor & Publication Plan

目的：將研究型 Jupyter notebook 解構為可維護、可重現並適合公開的 Python 專案；保留 `assets/` 結果與 README 敘事，移除公開 repo 中的 `.ipynb`。

主要輸出
- `REFACTOR_PLAN.md`（本檔）
- `src/` 核心模組骨架（`data.py`, `features.py`, `model.py`, `train.py`, `evaluate.py`, `explain.py`, `utils.py`）
- `run.py` 一鍵執行入口
- `requirements.txt` 或 `environment.yml`
- 維持 `assets/`（figures, tables, predictions, metrics）與 `README.md`

步驟（逐步執行）
1. Freeze assets：確認並保留 `assets/` 中要公開的圖表與表格。  (0.25 天)
2. Cell 分類：把 notebook 的 cell 分為 Data / Features / Model / Train / Eval / Viz / Notes 類別。 (0.5 天)
3. 抽取函式：把每類中可重用的程式碼搬到 `src/`，每個檔案負責單一責任。 (1~2 天)
4. 建立入口：`run.py` or `python -m src.run`，可從 raw data 一鍵重建 assets。 (0.5 天)
5. 測試重跑：用相同 seed 跑一次，檢查主要圖表與指標與 notebook 輸出一致或差異可解釋。 (0.5~1 天)
6. 清理與移除：確認無誤後把 `.ipynb` 從公開 repo 移除（或移到 private/archive）。 (0.25 天)

檔案對應建議
- `src/data.py`  => 下載/載入/清理/切分數據、cache 路徑
- `src/features.py`  => derived / transformer features 與其他衍生特徵、標準化、滑動視窗
- `src/model.py`  => Transformer encoder 與 baseline 模型建構、load/save
- `src/train.py`  => 訓練迴圈、early stopping、checkpoint
- `src/evaluate.py`  => 指標計算 (R2, RMSE)、產生預測檔、儲存 metrics
- `src/explain.py`  => permutation importance、MC dropout 預測不確定度
- `src/utils.py`  => seed 控制、I/O、logging、plot helpers
- `run.py`  => 解析 CLI / config，串起 `data -> features -> train -> evaluate -> save assets`

驗收準則
- `python run.py --config configs/example.yml` 能在乾淨環境下重跑並產生 `assets/` 中關鍵圖表與 `metrics/`。
- README 描述如何重現（資料來源、最小依賴、執行範例）。
- Notebook 已從公開分支移除或放入 private/archive（按你決定）。

風險與備註
- 若 notebook 中含有隱含環境設定或外部未加入 repo 的大資料檔，需先整理資料取得步驟並放入 `README`。
- 建議保留一個非常精簡的 demo notebook（只做結果展示），但不包含完整實驗 cell。

下一步（你選一）：
-- A：我幫你把 `ETF及BP預測_基於_Transformer_Encode.ipynb` 做 cell → 檔案清單（每個 cell 標注目標檔案與優先順序）。
- B：我直接產生 `src/` 空骨架與 `run.py` 範本，供你填入細節。

請選擇 A 或 B。