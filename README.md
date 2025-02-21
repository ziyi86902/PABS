# 專案名稱：水質數據處理與分析

## 介紹
此專案包含兩個主要的 Python 腳本，分別負責水質數據的清理與處理 (`data_clean_all.py`)，以及可視化分析 (`main.py`)。

---

## 目錄
- `data_clean_all.py`：
  - 讀取原始水質數據 (CSV 格式)
  - 進行去頭尾平均處理
  - 依照批次大小 (`batch_size`) 分段計算
  - 儲存清理後的數據

- `main.py`：
  - 讀取清理後的水質數據 (`202501_clean.csv`)
  - 計算 ODR、COD、NH3-N 等關鍵參數
  - 生成相關的趨勢圖並儲存

---

## 依賴套件
請確保已安裝以下 Python 套件：
```bash
pip install pandas matplotlib numpy
```

---

## 使用方式
### 1. 執行數據清理
```bash
python data_clean_all.py
```
執行後會產生 `202501_clean.csv`。

### 2. 執行數據分析與繪圖
```bash
python main.py
```
執行後將產生以下圖表：
- `ORP_ODR.png`
- `COD_NH3N.png`
- `DO_DO-inference.png`
- `ODR_ODR-inference.png`

清理後的數據將儲存於 `202501_clean.csv`。

---

## 主要函數說明
### `data_clean_all.py`
- `data_clean(record_list)`: 移除最大與最小值後計算平均值。
- `process_batches(df, ts_col, value_cols, batch_size)`: 依照批次大小處理數據，並計算去頭尾平均值。

### `main.py`
- `linear(x, a, b)`: 線性函數。
- `exp2_func(x, a, b)`: 指數函數。
- 計算 ODR、COD、NH3-N，並繪製相應圖表。

---

## 文件結構
```
.
├── data_clean_all.py  # 數據清理與預處理
├── main.py            # 數據分析與可視化
├── 202501_clean.csv   # 清理後的數據 (程式執行後產生)
├── ORP_ODR.png        # ORP 與 ODR 圖
├── COD_NH3N.png       # COD 與 NH3-N 圖
├── DO_DO-inference.png # DO 預測對比圖
└── ODR_ODR-inference.png # ODR 預測對比圖
```

---

## 注意事項
- `data_clean_all.py` 需要對應的原始數據檔 `202501.csv` 才能執行。
- `main.py` 需要先執行 `data_clean_all.py` 來產生 `202501_clean.csv`，否則會無法運行。

---