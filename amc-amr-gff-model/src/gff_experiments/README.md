# GFF Experiments — GatedFusionFormer 實驗套件

> **重構說明**：本目錄將原始 `Recs_of_AMR_GateFusionFormer_v8_clean.ipynb`（64 個 cells、大量重複代碼）
> 拆解為可**獨立執行**的輕量腳本，每支腳本對應一個明確的實驗目標。

---

## 目錄結構

```
gff_experiments/
├── config.py                  # 全局共享配置 (類別、模型超參、設備)
├── dataset.py                 # RMLDataset — IQ → IQ / STFT / S-TD 多模態轉換
├── model.py                   # GatedFusionFormer v3.0 完整定義（含消融支援）
├── utils.py                   # set_seed / load_rml_data / build_loader / load_model
│
├── 01_evaluate.py             # 基礎評估：混淆矩陣 + Accuracy vs SNR
├── 02_deep_analysis.py        # 深度分析：Per-class SNR / 易混淆類別 / t-SNE
├── 03_ablation.py             # 消融實驗：單模態 + 成對模態
├── 04_gating_weights.py       # 門控網絡權重分析：模態重要性 vs SNR
└── 05_cnn_vs_transformer.py   # CNN Backbone vs Transformer 性能對比
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
