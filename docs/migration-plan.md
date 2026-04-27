# 遷移計畫 | Migration Plan

## 遷移目標 | Migration Goals

將 repository 從扁平化的專案列表結構重構為功能分類的治理結構。

## 遷移原則 | Migration Principles

1. **僅進行目錄遷移與文件整理**
2. **嚴格禁止修改任何程式碼內容**
3. **原封不動搬移專案，不重寫、不重構、不格式化**
4. **保持專案內容完整性**

## 遷移對照表 | Migration Mapping

| 原路徑 | 新路徑 | 備註 |
|--------|--------|------|
| `bond-weighted-forecast/` | `Research/cnogb-abnormal-intervention/` 與 `Research/cnpbb-abnormal-drift/` | 研究專案分流後的兩個目錄 |
| `machine-learning-applications-in-fmri/` | `Research/machine-learning-applications-in-fmri/` | 路徑遷移 |
| `e-learning-fa-ipy/` | `Research/e-learning-fa-ipy/` | 路徑遷移 |
| `amc-amr-gff-nn/` | `Development/amc-amr-gff-nn/` | 路徑遷移 |
| `animated-gradient-text-starter/` | `Development/animated-gradient-text-starter/` | 路徑遷移 |
| `r3f-portfolio/` | `Development/r3f-portfolio/` | 路徑遷移 |
| `binance-multi-assets-singal-agent/` | `Development/binance-multi-assets-singal-agent/` | 路徑遷移 |
| `sw-single-page-cv-latex-templates/` | `Other/sw-single-page-cv-latex-templates/` | 路徑遷移 |

## 遷移階段 | Migration Phases

### Phase 1: 盤點
- ✅ 盤點現有 root 內容
- ✅ 確認專案分類
- ✅ 建立遷移對照表

### Phase 2: 建立新目錄
- ✅ 建立 `Research/`
- ✅ 建立 `Development/`
- ✅ 建立 `Other/`
- ✅ 建立 `catalog/`
- ✅ 建立 `docs/`

### Phase 3: 搬移專案
- ✅ 將專案原封不動搬移到對應目錄
- ✅ `bond-weighted-forecast/` 分流為 `cnogb-abnormal-intervention/` 與 `cnpbb-abnormal-drift/`
- ✅ 僅移動檔案位置，不更動檔案內容

### Phase 4: 更新索引與文件
- ✅ 建立 `catalog/projects.yml`
- ✅ 建立 `catalog/index.md`
- 🔄 更新 root `README.md`
- ✅ 建立 `docs/` 中的治理文件

### Phase 5: 驗證
- 🔄 確保每個專案都可以在新位置找到
- 🔄 確保沒有遺漏專案
- 🔄 確保沒有建立任何未授權目錄
- 🔄 確保沒有修改任何程式碼內容

## 注意事項 | Notes

- 不建立 `platform/` 或 `domains/` 目錄
- 不建立實體 `incubation/`, `stable/`, `archived/` 目錄
- 生命週期狀態作為 metadata 儲存在 `catalog/projects.yml`
