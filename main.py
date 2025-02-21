# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:05:08 2025

@author: user
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 設定 Matplotlib 中文顯示與負號正常顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


# 定義函數
def linear(x, a, b):
    return a * x + b

def exp2_func(x, a, b):
    return a * (x ** b)

# 讀取 CSV 資料
data = pd.read_csv('202501_clean.csv')
# 設定時間格式與篩選條件
data['ts'] = pd.to_datetime(data['ts'], errors='coerce')
data.dropna(subset=['ts'], inplace=True)



data['Q'] = 35/60
WL = 5.2
area = 510
t = 1
a = 2.056

DOS = 10.15


data['ODR'] = None
data['slope'] = None


for i in range(len(data['DO'])-5):

    
    slope = data['DO'][i+1] - data['DO'][i]
    Q = data['Q'][i]
    OUR1 = 2 * area * WL * (-slope) + Q * a
    equation_Q_new = OUR1 / 2.056
    
    # df['ma_PH'][i+5] = equation_Q_new   
    data['ODR'][i+5] = OUR1/60
    data['slope'][i+5] = slope
    
# 刪除前五行
data = data.iloc[5:]


# 計算 ODR、COD、NH3-N
data['ODR_equation'] = 117 / (1 + np.exp(0.055 * (data['ORP'] - 204)))  # 假設這是適用的公式
data['COD'] = 5226.9 * np.exp(-0.019 * ((np.log((117 / data['ODR_equation']) - 1) / 0.055) + 204))
data['NH3-N'] = (5226.9 / 10) * np.exp(-0.019 * ((np.log(117 / data['ODR_equation'] - 1) / 0.055) + 204))

data['equation_DO_inference'] = exp2_func(data['ODR_equation'], 18.31, -0.67)
data['equation_KLA'] = linear(data['ODR_equation'], 0.1, 0.55)
data['DO_inference'] = DOS - (data['ODR_equation'] / data['equation_KLA'])



# 繪製 ORP 與 ODR 圖
fig, ax1 = plt.subplots(figsize=(15, 8))
ax2 = ax1.twinx()
ax1.set_xlabel('ts')
ax1.set_ylabel('ORP(mV)')
ax2.set_ylabel('ODR(gO2/min)')
ax1.plot(data['ts'], data['ORP'], color="blue", label="ORP")
ax2.plot(data['ts'], data['ODR_equation'], color="red", label="ODR")
# ax2.set_ylim([0, 150])
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2)
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  # 調整邊距
plt.savefig('ORP_ODR.png')

# 繪製 COD 與 NH3-N 圖
fig, ax1 = plt.subplots(figsize=(15, 8))
ax1.set_xlabel('ts')
ax1.plot(data['ts'], data['COD'], color="blue", label="COD")
ax1.plot(data['ts'], data['NH3-N'], color="red", label="NH3-N")
ax1.legend(loc='upper left')
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  # 調整邊距
plt.savefig('COD_NH3N.png', dpi=300)

# 繪製 DO 與 DO* 圖
fig, ax1 = plt.subplots(figsize=(15, 8))
ax1.set_xlabel('ts')
ax1.plot(data['ts'], data['DO'], color="blue", label="DO")
ax1.plot(data['ts'], data['DO_inference'], color="red", label="DO*")
ax1.set_ylabel('DO(mg/L)')
ax1.legend(loc='upper left')
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  # 調整邊距
plt.savefig('DO_DO-inference.png', dpi=300)

# 繪製 ODR 與 ODR* 圖
fig, ax1 = plt.subplots(figsize=(15, 8))
ax1.set_xlabel('ts')
ax1.plot(data['ts'], data['ODR'], color="blue", label="ODR")
ax1.plot(data['ts'], data['ODR_equation'], color="red", label="ODR*")
ax1.set_ylabel('ODR(gO2/min)')
ax1.legend(loc='upper left')
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  # 調整邊距
plt.savefig('ODR_ODR-inference.png', dpi=300)

# 儲存清理後的資料
data.to_csv('202501_clean.csv', index=False, encoding='utf_8_sig')
print(data.head())
