# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:30:16 2024

@author: user
"""

import pandas as pd

def data_clean(record_list):
    if record_list:
        max_value = max(record_list)
        min_value = min(record_list)
        record_list.remove(max_value)
        record_list.remove(min_value)
        average_value = sum(record_list) / len(record_list)
    else:
        print("record_list 為空，無法計算。")
        average_value = None
    return average_value

def process_batches(df, ts_col, value_cols, batch_size):
    df = df.rename(columns={ts_col: 'ts'})
    ts_list = []
    processed_values = {col: [] for col in value_cols}

    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i+batch_size]
        
        if len(batch) < batch_size:
            break
        
        last_ts = batch['ts'].iloc[-1]
        ts_list.append(last_ts)

        for col in value_cols:
            values = batch[col].tolist()
            avg_value = data_clean(values)
            processed_values[col].append(avg_value)
        
        print(f"Batch {i // batch_size + 1}:")
        print(f"資料時間: {last_ts}")
        for col in value_cols:
            print(f"{col} (去頭尾平均): {processed_values[col][-1]}")
        print("\n")
    
    return pd.DataFrame({'ts': ts_list, **processed_values})

# 讀取CSV文件
all_2210 = pd.read_csv("202412202501_data/202501.csv")

# 設定批次大小
batch_size = 12

# 處理資料
df_all = process_batches(
    all_2210, 
    ts_col='Date', 
    value_cols=['ORP','DO'], 
    batch_size=batch_size
)

df_all.to_csv('202501_clean.csv', index=False)

