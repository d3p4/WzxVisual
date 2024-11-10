import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid', {'font.sans-serif': ['SimHei', 'Arial']})
df_stock = pd.read_excel(r'D:\Python数据可视化分析与案例实战\ch04\中国平安.xls')

#把日期修改为行索引
df_stock.set_index('date',inplace = True) #inplace对数据进行永久改变

#抽取开盘，最高，最低，收盘 这些数据（就是讲dataframe变得小一点）
new_df = df_stock.loc[:, ['open','high','low','close']]

#绘制OHLC
plt.figure(figsize=(10,6))
plt.title('中国平安2020年上半年股价OHLC图',size=20)
sns.lineplot(data = new_df.iloc[:117])  #前117行数据

#给x轴加上标签
plt.xlabel('日期',size=16)
#设置刻度值的字体大小
plt.tick_params(labelsize=16)
#设置图例
plt.legend(loc='upper right',fontsize=16)