import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid', {'font.sans-serif': ['SimHei', 'Arial']})

df_stock = pd.read_excel('D:/py_practice/python可视化/各章节数据源/ch04/stocks.xls')

df_stock.set_index('date', inplace=True)

new_df = df_stock.loc[:, ['open', 'high', 'low', 'close']]

plt.figure(figsize=(11, 7))
plt.title('股票价格OHLC图', size=20)
sns.lineplot(data=new_df.iloc[:120])
plt.xlabel('日期', size=16)
plt.tick_params(labelsize=13)

plt.legend(loc='upper right', fontsize=16)
