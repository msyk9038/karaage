# Kindle の蔵書一覧から年ごとの月別購入冊数をグラフ化
# %% read csv file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
df = pd.read_csv('./Kindle.csv')
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
df = df.sort_values('PurchaseDate')
df['yr'] = df['PurchaseDate'].apply(lambda x:int(f'{x.year}'))
df['mo'] = df['PurchaseDate'].apply(lambda x:int(f'{x.month:02}'))
# %% draw graph
plt.rcParams["font.size"] = 18
fig, ax = plt.subplots(3, 1, figsize=(10, 15), facecolor='w', sharex=True, sharey=True)
for idx, val in enumerate(df['yr'].unique()):
    data = df.query('yr == @val').groupby('mo').size()
    print(data.index, data.values)
    ax[idx].plot(data.index, data.values)
    ax[idx].set_title(val)
    ax[idx].text(0.05, 0.85, f'books/per : {np.mean(data):,.0f}', transform=ax[idx].transAxes)
plt.savefig('./compare_3yr_per_month.png')
plt.show()
# %% confirm content at most point at 2019 
df.query('yr==2019 and mo==11')
