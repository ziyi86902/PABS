# README

## 專案名稱
隨機插入 CSV 數據至 MySQL 資料庫

## 簡介
本專案使用 Python 讀取 CSV 檔案的數據，並隨機選擇一行插入到 MySQL 資料庫中，每次插入後會等待一段時間（可自訂時間間隔）。

## 先決條件
在運行本程式前，請確保已安裝以下環境與工具：
- Python 3.x
- MySQL 資料庫
- 必要的 Python 套件（pymysql）

## 安裝步驟
1. 安裝 Python 必要套件：
   ```bash
   pip install pymysql
   ```
2. 設定 MySQL 伺服器，並確保有可用的數據庫與表格。

## 使用方法
1. 修改 `insert_random_data_from_csv` 函數中的資料庫連線資訊：
   ```python
   host = "192.168.50.84"
   port = 3306
   user = "sa"
   password = "0000"
   database = "demo"
   table_name = "demo_PH_1102_pred"
   csv_file_path = "PH_1102.csv"
   interval_seconds = 5
   ```
2. 確保 `csv_file_path` 指向有效的 CSV 檔案。
3. 執行程式：
   ```bash
   python your_script.py
   ```

## 主要功能
- 檢查表是否存在，若不存在則自動建立。
- 從 CSV 檔案讀取數據，隨機選取一行數據插入到 MySQL 資料庫。
- 自動新增 ID 欄位並記錄當前時間。
- 透過 `interval_seconds` 設定插入間隔時間。

## 程式邏輯
1. 連接 MySQL 資料庫。
2. 確保指定的表存在，若無則創建。
3. 讀取 CSV 數據，檢查欄位名稱是否匹配。
4. 取得當前最大 ID，確保 ID 連續。
5. 隨機選取一行數據並插入。
6. 以指定間隔時間（如 5 秒）重複插入過程。

## 錯誤排除
### 1. 無法連接 MySQL
- 確保 MySQL 伺服器運行中。
- 檢查 `host`、`port`、`user`、`password` 是否正確。
- 確保用戶有對應的資料庫權限。

### 2. CSV 檔案讀取失敗
- 確保 CSV 檔案存在且路徑正確。
- 檢查 CSV 欄位名稱是否符合程式內預設的欄位。

### 3. 資料未成功插入
- 檢查 MySQL 表結構是否符合程式定義。
- 確保 CSV 內的數據能轉換為 `FLOAT` 格式。


