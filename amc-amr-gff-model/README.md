# GFF Experiments — GatedFusionFormer 實驗套件

> **說明**：原始 `AMR_GateFusionFormer_v8_clean.ipynb`（64 cells）

---

## 目錄結構

```
gff_project/
├── configs/               # ⚙️ 實驗配置 (YAML) - 存放 4 個模型的超參數
├── models/                # 🧠 模型庫
│   ├── backbones/         # 特徵提取器 (MCLDNN, SA-CNN, IQFormer)
│   ├── factory.py         # 🏭 模型工廠 (一鍵生成指定模型)
│   └── gated_fusion.py    # 💎 你的核心研究：GatedFusionFormer
├── core/                  # 🛠️ 核心引擎
│   ├── dataset.py         # 多模態轉換 (IQ/STFT/STD) 與 Data Loader
│   ├── trainer.py         # 統一的訓練與驗證循環
│   └── analyzer.py        # 深度診斷 (SNR-Acc, Confusion Matrix)
├── run.py                 # 🚀 唯一入口 (支持交互式中斷與實驗選擇)
└── utils.py               # 🧰 輔助工具 (Plotting, Logger, Profiler)
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
|---|---|
| `--weights` | 訓練好的模型權重路徑 (`.pth`) |
| `--data` | `RML2016.10a_dict.pkl` 資料集路徑 |

選用參數：

| 參數 | 預設 | 說明 |
|---|---|---|
| `--batch-size` | 256 | 推理批次大小 |
| `--output-dir` | `outputs` | 圖表儲存目錄 |

---

## 各實驗說明

### `01_evaluate.py` — 基礎模型評估

```bash
python 01_evaluate.py --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `confusion_matrix_counts.png` — 原始計數混淆矩陣
- `confusion_matrix_normalized.png` — 歸一化混淆矩陣
- `accuracy_vs_snr.png` — 整體 Accuracy vs SNR

---

### `02_deep_analysis.py` — 深度性能分析

```bash
python 02_deep_analysis.py --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `per_class_accuracy_vs_snr.png` — 各類別 Accuracy vs SNR
- `confused_categories_high_snr.png` — 高 SNR 易混淆類別柱狀圖
- `tsne_visualization.png` — t-SNE 特徵空間可視化（低 / 高 SNR）

---

### `03_ablation.py` — 模態消融實驗

```bash
python 03_ablation.py --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `ablation_single_modality.png` — 單模態消融 Accuracy vs SNR
- `ablation_pairwise_modality.png` — 成對模態消融 Accuracy vs SNR
- `ablation_confused_categories.png` — 高 SNR 易混淆類別對比

---

### `04_gating_weights.py` — 門控網絡權重分析

```bash
python 04_gating_weights.py --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `gating_weights_vs_snr.png` — IQ / STFT / S-TD 模態重要性 vs SNR

---

### `05_cnn_vs_transformer.py` — CNN vs Transformer 對比

```bash
python 05_cnn_vs_transformer.py --weights model.pth --data RML2016.10a_dict.pkl
```

**輸出：**
- `cnn_vs_transformer_accuracy.png` — 整體 Accuracy vs SNR 對比折線圖
- `cnn_vs_transformer_overall.png` — 整體準確率柱狀圖

---

## 資料集

本套件使用 [RadioML 2016.10a (RML2016.10a)](https://www.deepsig.ai/datasets)。
下載後解壓，使用 `RML2016.10a_dict.pkl` 作為 `--data` 參數。

---

## 模型架構

GatedFusionFormer v3.0 融合三種模態特徵：

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
