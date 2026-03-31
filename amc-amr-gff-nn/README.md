# GatedFusionFormer NeuralNetwork

> **說明**：原始 `AMR_GateFusionFormer_v8_clean.ipynb`（64 cells）Productionization

> 門控機制在數學上表現為一個信噪比相關的路由系統，在高信噪比條件下智能地優先使用頻率特徵（短時傅立葉變換，STFT），
> 而在嚴重噪聲條件下則退而求其次使用結構保持特徵（短時差分/圖像質量，S-TD/IQ）。

---

## 資料集

本套件使用 [RadioML 2016.10a (RML2016.10a)](https://www.deepsig.ai/datasets)。
下載後解壓，使用 `RML2016.10a_dict.pkl` 作為 `--data` 參數。

---

## 模型架構

GatedFusionFormer NeuralNetwork 融合三種模態特徵：

```
IQ Signal  (2, T)   → Conv1d Embedding
STFT Map   (1,32,T) → 2D Conv + Freq-Adaptive Pool
S-TD Stats (2, T)   → Conv1d Embedding
                           ↓
              GatingNetwork (動態融合權重)
                           ↓
              FusionTransformerBlock × depth
              (Conv Encoder + Multi-Head Attention)
                           ↓
                    Linear Classifier
```

詳見 [`model.py`](model.py)。

---

## 目錄結構

```
amc-amr-gff-nn/
├── assets/
├── src/
│   ├── __init__.py
│   ├── run.py                 # CLI / subcommands entrypoint
│   ├── export.py              # 模型匯出 / ONNX / TorchScript (選用)
│   ├── utils.py               # 共用工具（IO、plotting、metrics）
│   ├── configs/
│   │   └── config.py          # 預設設定 / hyperparams
│   ├── core/                  # 分析/實驗模組（evaluate, deep_analysis, ...）
│   │   ├── dataset.py
│   │   ├── evaluate.py
│   │   ├── deep_analysis.py
│   │   ├── ablation.py
│   │   ├── gating_weights.py
│   │   └── cnn_vs_transformer.py
│   └── models/
│       ├── factory.py         # build_model(...)
│       ├── model.py
│       ├── gff_nn.py
│       └── cnn2.py / mod_rec_net.py
├── README.md
```

---

## 環境需求

```bash
pip install torch torchvision timm scipy scikit-learn matplotlib seaborn tqdm pandas
```

---

## 通用執行方式

所有腳本共用相同的兩個必填參數：

| 參數 | 說明 |
  - `--weights` : 訓練後的 model weights 檔案（.pth） — 必填
  - `--data`    : RML2016.10a_dict.pkl 的完整路徑 — 必填

選用參數：

| 參數 | 預設 | 說明 |
|---|---|---|
| `--batch-size` | 256 | 推理批次大小 |
| `--output-dir` | `outputs` | 圖表儲存目錄 |
  - `--device`  : `cpu` 或 `cuda`（預設自動偵測）
---

## 各實驗說明

### `evaluate.py` — 基礎模型評估

```bash
python src/run.py evaluate --weights path/to/model.pth --data path/to/RML2016.10a_dict.pkl --batch-size 256
```

**輸出：**
- `confusion_matrix_counts.png` — 原始計數混淆矩陣
- `confusion_matrix_normalized.png` — 歸一化混淆矩陣
- `accuracy_vs_snr.png` — 整體 Accuracy vs SNR

---

### `deep_analysis.py` — 深度性能分析

```bash
python src/run.py deep_analysis --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `per_class_accuracy_vs_snr.png` — 各類別 Accuracy vs SNR
- `confused_categories_high_snr.png` — 高 SNR 易混淆類別柱狀圖
- `tsne_visualization.png` — t-SNE 特徵空間可視化（低 / 高 SNR）

![per_class_acc_vs_snr](assets/per_class_acc_vs_snr.png)
![tsne_visualization](assets/tsne_visualization.png)
---

### `ablation.py` — 模態消融實驗

```bash
python src/run.py ablation --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `ablation_single_modality.png` — 單模態消融 Accuracy vs SNR
- `ablation_pairwise_modality.png` — 成對模態消融 Accuracy vs SNR
- `ablation_confused_categories.png` — 高 SNR 易混淆類別對比

![ablation_single_modality](assets/ablation_single_modality.png)
![ablation_pairwise_modality](assets/ablation_pairwise_modality.png)


---

### `gating_weights.py` — 門控網絡權重分析

```bash
python src/run.py gating --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `gating_weights_vs_snr.png` — IQ / STFT / S-TD 模態重要性 vs SNR

![gating_weights_vs_snr](assets/gating_weights_vs_snr.png)

---

### TODO:
### `cnn_vs_transformer.py` — CNN vs Transformer 對比

```bash
python src/run.py compare --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `gffnn_compare_acc.png` — 整體 Accuracy vs SNR 對比折線圖
- `gffnn_compare_overall.png` — 整體準確率柱狀圖



---

（若 prefer module run）
```bash
python -m src.run evaluate --weights ... --data ...
```

---

## 輸出說明

- 所有圖表、可視化結果、CSV、與 logs 會儲存在 `--output-dir` 指定的目錄（預設 `outputs/`）。
- 常見輸出檔例：
  - `confusion_matrix_counts.png`
  - `confusion_matrix_normalized.png`
  - `accuracy_vs_snr.png`
  - `per_class_accuracy_vs_snr.png`
  - `tsne_visualization.png`
  - `gating_weights_vs_snr.png`
  - `ablation_*.png`
  - `cnn_vs_transformer_accuracy.png`

### 程式化呼叫（當作 library 使用）

如果你想在其他程式中直接使用模型或 pipeline，可以匯入 factory 與工具函式：
```python
from src.models.factory import build_model
from src.core.dataset import RMLDataset
from src.utils import load_weights, predict_batch

# 建構模型
model = build_model(name="gff_nn", num_classes=11)
# 載入權重
load_weights(model, "path/to/model.pth")
# 資料/推理
dataset = RMLDataset("path/to/RML2016.10a_dict.pkl", split="test")
preds = predict_batch(model, dataset, device="cuda")
```
（上述 API 名稱為範例；請以實際 code 中的 function/class 名稱為準）

---

### 維護與開發建議

- 將 CLI 的 subcommands 套用 unittest / pytest 測試，以確保 refactor 後 CLI 行為的改變。
- 將 config（超參數）移到 YAML/JSON，並加入版本記錄，方便在實驗重現時載入 exact config。
- 在模型 factory 與 config 之間標註相容性（哪個 model-name 需要哪些 config keys），減少使用錯誤。

### 版本紀錄（小節）

- README.v4.md — 本檔（模組化 / production-friendly）
