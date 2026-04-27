# Abnormal Transformer Detect — Colab Cells → Implementation & Experiment Path

來源 notebook: `ETF及BP預測_基於_Transformer_Encode.ipynb` (原始 notebook 名稱含 fc7 已在專案檔名中移除)

說明：下列依 notebook 中包含 `# Colab Cell` 的 code block 順序，為每一個 block 增補：
- 精確功能說明
- 建議搬入的 `src/` 檔案或 `configs/`、`scripts/` 位置
- 產出 artifacts（中間/最終）
- 在完整實驗流程中的位置（步驟編號）

簡短實驗路徑總覽（步驟）：
1. 環境與套件準備 (env)
2. 資料上傳與萃取 (ingest)
3. 欄位清理與驗證 (preprocess)
4. 特徵工程與縮放 (features)
5. 時序序列化 (sequence)
6. Dataset / DataLoader 準備 (dataloader)
7. 模型建立 (model)
8. 訓練迴圈 (train)
9. 評估與不確定性估計 (evaluate + mc-dropout)
10. 特徵重要性與殘差分析 (explain)
11. 匯出與報告 (export/report)

---

## 研究設計總覽

```
Phase 0: 數據收集與預處理
    ├── 6 份債券/利率數據（政金債 + SHIBOR/DR007）
    ├── A 股銀行板塊（AKShare）
    └── 港股/美債（yfinance）

Phase 1: 單域異常檢測（L0）
    ├── 同標的歷史期 vs 觀察期
    ├── 第一梯隊模型 baseline
    └── 合成異常注入驗證

Phase 2: 跨標的一致性驗證（L1）
    ├── 三大政金債交叉驗證
    ├── Leave-one-out domain 實驗
    └── Cross-era Discriminator

Phase 3: 跨資產類別對照（L2）
    ├── A 股銀行板塊對照實驗
    ├── Granger causality 動態分析
    └── 第二梯隊模型驗證

Phase 4: 跨市場遷移（L3）
    ├── 港股/美債遷移實驗
    ├── 三步遷移路徑
    └── 第三梯隊模型評估
```

## 項目結構（建議 tree）

```
cn-ogb-anomaly-intervention/
├── README.md                   # 本文件
├── configs/                    # 實驗配置（YAML）
│   ├── base.yaml
│   ├── abnormal_transformer.yaml
│   ├── tranad.yaml
│   └── patchtst.yaml
├── data/
│   ├── raw/                    # 原始數據
│   ├── processed/              # 預處理後數據
│   └── external/               # yfinance / AKShare 下載
├── src/
│   ├── data/                   # 數據加載與預處理
│   │   ├── loader.py
│   │   ├── features.py         # 微觀結構特徵計算
│   │   └── preprocessing.py
│   ├── models/                 # 模型實現
│   │   ├── abnormal_transformer/
│   │   ├── tranad/
│   │   ├── patchtst/
│   │   ├── dada/
│   │   ├── ts2vec/
│   │   ├── timesnet/
│   │   └── dann/
│   ├── evaluation/             # 評估模組
│   │   ├── metrics.py          # AUROC, AUPRC, F1 等
│   │   ├── synthetic.py        # 合成異常注入
│   │   ├── statistical.py      # KS test, CUSUM, Hurst
│   │   └── calibration.py      # 校準曲線
│   ├── transfer/               # 遷移學習模組
│   │   ├── alignment.py        # MMD, CORAL, OT
│   │   ├── adapter.py          # Adapter-based transfer
│   │   └── progressive.py      # 三步遷移流程
│   └── utils/
│       ├── config.py
│       ├── logging.py
│       └── visualization.py
├── notebooks/                  # 探索性分析 Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_analysis.ipynb
│   ├── 03_baseline_experiments.ipynb
│   └── 04_transfer_experiments.ipynb
├── experiments/                # 實驗腳本
│   ├── run_l0.py               # L0 層實驗
│   ├── run_l1.py               # L1 層實驗
│   ├── run_l2.py               # L2 層實驗
│   ├── run_l3.py               # L3 層實驗
│   └── run_ablation.py         # Ablation study
├── results/                    # 實驗結果（gitignored）
├── scripts/                    # 輔助腳本
│   ├── download_data.py        # 數據下載
│   └── setup_env.sh            # 環境設置
├── tests/                      # 單元測試
├── requirements.txt
└── pyproject.toml
```

1. Colab Cell 1 — 安裝必要套件
   - 功能：安裝與鎖定依賴（pandas, openpyxl, numpy, torch, scikit-learn, matplotlib, seaborn 等）。
   - 建議放置：`requirements.txt` / `environment.yml`；`scripts/setup_env.sh`。
   - 產出：可重現的依賴清單（artifact: `requirements.txt`）。
   - 實驗步驟：步驟 1（env）。

2. Colab Cell 2 — 匯入套件檢查
   - 功能：檢查並匯入專案所需的核心套件，供後續模組使用。
   - 建議放置：轉為 `src/__init__.py` 與 `src/utils/__init__.py` 的 import 清單示例；or 放在 `run.py` 頂部。
   - 產出：import smoke-test。
   - 實驗步驟：手動檢查（1→2）。

3. Colab Cell 3 — Matplotlib 中文字體設定
   - 功能：系統字體安裝與 matplotlib 參數設定（僅 Colab/展示所需）。
   - 建議放置：`src/utils/visualization.py` 中的 `set_matplotlib_defaults()` 函式（只在 notebook/plotting 時呼叫）。
   - 產出：可重現的圖表字型設定。
   - 實驗步驟：可選（reporting）。

4. Colab Cell 4 — 處理上傳的檔案（ingest）
   - 功能：處理 Colab 上傳介面，將檔案移至 `dataset/`。
   - 建議放置：`scripts/ingest.py` 或 `src/data/loader.py::ingest_uploaded_files()`。
   - 產出：`data/raw/` 或 `data/uploaded/` 中的原始檔案。
   - 實驗步驟：步驟 2（ingest）。

5. Colab Cell 5 — 找到配對的 train/exam Excel 檔案
   - 功能：實作 `find_paired_files()`，輸出訓練/考試檔案配對清單。
   - 建議放置：`src/data/loader.py::find_paired_files()`。
   - 產出：`paired_files`（list of dicts）供後續批次處理。
   - 實驗步驟：步驟 2→3（ingest→preprocess）。

6. Colab Cell 6 — 定義核心參數
    - 功能：將 notebook 中硬編碼參數（TARGET_COLUMN、時間欄位、derived feature 欄位清單、SEQUENCE_LENGTH 等）抽出為配置。
    - 建議放置：`configs/training.yaml` 與 `src/config.py`（載入 YAML）。
    - 產出：可參數化的 `training.yaml`。
   - 實驗步驟：在所有其他步驟前（config）。

7. Colab Cell 7 — 欄位清理與檔案載入函式
   - 功能：實作 `clean_column_names_general(df)` 與 `load_and_clean_file(path)`，包含類型轉換與缺值處理規則。
   - 建議放置：`src/data/preprocessing.py`（函式：`clean_column_names_general`, `load_and_clean_file`）。
   - 產出：`DataFrame`（cleaned）與清理日志。
   - 實驗步驟：步驟 3（preprocess）。

8. Colab Cell 8 — 處理與驗證單一資料集對的高階函式
   - 功能：`process_and_validate_pair(pair)` 結合載入、欄位檢查、時間連續性驗證、目標欄位存在性檢查。
   - 建議放置：`src/data/processing.py::process_and_validate_pair()`。
   - 產出：`processed_info` 字典（包含 cleaned dfs、feature_columns、valid flag）。
   - 實驗步驟：步驟 3（preprocess）。

9. Colab Cell (derived-feature processing) — 載入並驗證配對資料
    - 功能：依指定特徵集合載入（例如 ADBC_train/exam），驗證時間欄位與目標可用性，建立 `processed_pair_info`。
    - 建議放置：`src/data/processing.py` 中的 `process_pair()`。
    - 產出：`processed_pair_info`（主資料結構，後續所有步驟共享）。
   - 實驗步驟：步驟 3→4（preprocess→features）。

10. Colab Cell 9 — 定義模型/訓練參數字典
    - 功能：定義 `training_params`（網路尺寸、學習率、序列長度等），應同步到 configs。
    - 建議放置：`configs/experiment_transformer.yaml` 與 `src/config.py`。
    - 產出：`params` 物件供 `train` 使用。
    - 實驗步驟：config。

11. Colab Cell 10 — 資料排序（按時間特徵）
    - 功能：將 train/exam DataFrame 按時間欄位排序與重索引以確保序列連續性。
    - 建議放置：`src/data/preprocessing.py::sort_by_time()`（在 `process_*` 流程中呼叫）。
    - 產出：時間排序後的 DataFrame（artifact: `data/processed/*.parquet`）。
    - 實驗步驟：步驟 3（preprocess）。

12. Colab Cell 11 — 特徵縮放與類別處理
    - 功能：建立並擬合 `ColumnTransformer`（數值 MinMaxScaler、類別 OneHotEncoder 等）與 `target_scaler`。
    - 建議放置：`src/features/preprocessor.py`（函式: `fit_feature_preprocessor`, `transform_features`），scaler 存為 `artifacts/feature_preprocessor.pkl`。
    - 產出：transformed X, scaled y，以及 scaler artifact。
    - 實驗步驟：步驟 4（features）。

13. Colab Cell 12 — 建立時間序列序列（sliding windows）
    - 功能：`create_sequences(X, y, seq_len)` 建構 (X_seq, y_seq) sliding-window。
    - 建議放置：`src/data/sequence.py::create_sequences()`。
    - 產出：序列化的 numpy arrays / tensors，保存為 `artifacts/sequences/*.npz`。
    - 實驗步驟：步驟 5（sequence）。

14. Colab Cell 13 — 轉為 PyTorch Tensor 並建立 DataLoaders
    - 功能：建立 `TensorDataset`、`DataLoader`（train/val/test），含 batch size 與 shuffle 設定。
    - 建議放置：`src/data/dataset.py::build_dataloaders()`。
    - 產出：`train_loader', `exam_loader`；若需要可序列化採樣狀態。
    - 實驗步驟：步驟 6（dataloader）。

15. Colab Cell 14 — 定義 Transformer 模型 (PyTorch)
    - 功能：實作 `PositionalEncoding` 與 `TransformerPredictor` 類別（輸入 d_model、nhead、num_layers、dropout 等）。
    - 建議放置：`src/models/transformer.py`（包含 model 類別與一個 `build_model(params, feature_dim)` helper）。
    - 產出：已初始化的 `model`（artifact: `checkpoints/initial_state.pt`）。
    - 實驗步驟：步驟 7（model）。

16. Colab Cell 15 — 設定損失函數與優化器
    - 功能：建立 `criterion`、`optimizer` (Adam) 以及 optional scheduler。
    - 建議放置：`src/train/optimizer.py` 或 `src/train.py` 的初始化段。
    - 產出：optimizer state，存於訓練 checkpoint 中。
    - 實驗步驟：步驟 7→8（model→train）。

17. Colab Cell 16 — 定義訓練函式 `train_epoch`
    - 功能：實作一個 training epoch（forward, loss.backward, optimizer.step），包含 grad clipping 與 logging。
    - 建議放置：`src/train/loop.py::train_epoch()`。
    - 產出：epoch-level loss；整合到 training history。
    - 實驗步驟：步驟 8（train）。

18. Colab Cell 17 — 定義評估函式 `evaluate_model`
    - 功能：在 eval 模式下計算 loss 與收集預測，用以計算 RMSE/R2。
    - 建議放置：`src/evaluate/eval.py::evaluate_model()`。
    - 產出：validation loss 與 raw predictions。
    - 實驗步驟：步驟 8→9（train→evaluate）。

19. Colab Cell 18 (part A/B) — get_training_components
    - 功能：封裝訓練所需組件的工廠函式（model, loaders, optimizer, criterion, scheduler, device），後續 notebook 使用此輸出啟動訓練。
    - 建議放置：`src/train/components.py::get_training_components()`（確保單一責任與可測試）。
    - 產出：一致的啟動物件集合（供 `experiments/run_*` 調用）。
    - 實驗步驟：步驟 7→8（train）。

20. Colab Cell 19 — 訓練與評估主迴圈
    - 功能：完整 epoch 迴圈（train + evaluate），儲存 checkpoint、更新學習率、收集歷史記錄並輸出 logs。
    - 建議放置：`experiments/run_training.py`（或 `experiments/run_l0.py`），並由 CLI `run.py` 呼叫。
    - 產出：`checkpoints/*.pt`, `artifacts/train_history.json`。
    - 實驗步驟：步驟 8（train）。

21. Colab Cell 20 — 模型評估：生成預測並計算指標
    - 功能：使用最佳 checkpoint 在考試集上生成預測、逆縮放並計算 RMSE、R²；產生 `evaluation_metrics` 與 `evaluation_results_df`。
    - 建議放置：`src/evaluate/metrics.py` 與 `experiments/evaluate_transformer.py`（或 `experiments/evaluate.py`）。
    - 產出：`evaluation_metrics_transformer.json`, `evaluation_results_transformer.csv`。
    - 實驗步驟：步驟 9（evaluate）。

22. Colab Cell 21 — 視覺化預測結果
    - 功能：繪製實際 vs 預測的時間序列、殘差圖，並標記重要事件。
    - 建議放置：`src/utils/visualization.py::plot_predictions()` 與 `notebooks/visualize_transformer.ipynb`。
    - 產出：PNG/SVG 圖檔存於 `assets/`。
    - 實驗步驟：步驟 10（reporting）。

23. Colab Cell 22 — 評估結果分析與比較（文字與圖）
    - 功能：將指標化為文字結論、比較不同 feature-set（derived features vs 原始）的表現，並輸出觀察報告。
    - 建議放置：`notebooks/analysis_transformer.ipynb` 或 `reports/analysis_transformer.md`（自動化可用 `src/reports/generate_report.py`）。
    - 產出：分析報告 `reports/transformer_analysis.pdf` 或 `.md`。
    - 實驗步驟：步驟 10（reporting）。

24. Colab Cell 23 — 儲存預測結果為 CSV
    - 功能：將 `evaluation_results_df`（或 `evaluation_results_df_transformer`）匯出為 CSV 方便外部檢視與保存。
    - 建議放置：`scripts/export_predictions.py` 或 `src/utils/io.py::save_predictions()`。
    - 產出：`results/prediction_transformer_adbc.csv`。
    - 實驗步驟：步驟 11（export）。

25. Colab Cell 23B — Permutation Importance（特徵重要性）
    - 功能：實作 `PyTorchPredictorForImportance` 包裝與 `calculate_permutation_importance()`，以打亂特徵測量對指標的影響。
    - 建議放置：`src/explain/permutation_importance.py`。
    - 產出：`permutation_importance_transformer.csv` 與繪圖。
    - 實驗步驟：步驟 10（explain）。

26. Colab Cell (MC Dropout function) — 定義 MC Dropout 預測函式
    - 功能：`predict_with_mc_dropout()` 多次前向傳播以估計 epistemic uncertainty（啟用 dropout 在推理時）。
    - 建議放置：`src/explain/uncertainty.py`。
    - 產出：`pred_mean', `pred_std` time series，保存為 `artifacts/mc_dropout/*.npz`。
    - 實驗步驟：步驟 9→10（evaluate→explain）。

27. Colab Cell (MC Dropout execute) — 執行 MC Dropout 並反向轉換
    - 功能：對考試集執行 MC Dropout、逆縮放並記錄不確定性以輔助 outlier 判定。
    - 建議放置：`experiments/run_training.py` 的 optional 分支或 `scripts/mc_dropout_exec.py`。
    - 產出：`mc_dropout_results_{exp}.csv`。
    - 實驗步驟：步驟 9（evaluate）與步驟 10（explain）。

28. Colab Cell (Residuals & Outlier Detection) — 殘差計算與視覺化
    - 功能：計算 residual、absolute_error，並以 2σ（或 percentile-based）標準標記潛在異常；產出殘差圖與 outlier list。
    - 建議放置：`src/evaluate/outliers.py` 或 `src/explain/outlier_detection.py`。
    - 產出：`results/outliers_{exp}.csv` 與相應圖表。
    - 實驗步驟：步驟 10（explain）。

---

完整實驗運行範例（建議）：

1) 安裝與建立虛擬環境

```bash
python -m pip install -r requirements.txt
```

2) 執行單次 Transformer 實驗（假設 `experiments/run_training.py` 已實作並可讀取 configs）

```bash
python experiments/run_training.py --config configs/training.yaml
```

3) 評估與生成報告

```bash
python experiments/evaluate_transformer.py --checkpoint checkpoints/best.pt --out_dir results/
python src/reports/generate_report.py --metrics results/evaluation_metrics_transformer.json --out reports/transformer_report.pdf
```

下一步建議（我可以代勞）：
- 自動把每個 Colab cell 的 code 拆成對應 `src/` 檔案範本並加入簡單單元測試（回覆「拆檔」開始）。
- 或先生成 `configs/training.yaml`、`requirements.txt` 與 `experiments/run_training.py` 的最小可執行範本以便快速驗證。

已開始把 `abnormal_transformer_detect.md` 升級為包含實作對應與完整實驗路徑；`TODO` 中已標註後續拆檔工作為 in-progress。 
