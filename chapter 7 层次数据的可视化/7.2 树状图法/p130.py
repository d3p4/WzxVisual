import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import squarify
from dbconn import conn

sql = "SELECT region, ROUND(SUM(sales)/10000, 2) as sales FROM orders WHERE dt=2020 GROUP BY region ORDER BY sales DESC"
df = pd.read_sql(sql, conn)

plt.figure(figsize=(11, 7))
colors = ['Coral', 'Gold', 'LawnGreen', 'LightSkyBlue', 'LightSteelBlue', 'CornflowerBlue']
plot = squarify.plot(
    sizes=df['sales'],
    label=df['region'],
    color=colors,
    alpha=0.9,
    value=df['sales'],
    edgecolor='white',
    linewidth=8
)

plt.rc('font', size=16)
plot.set_title('2020年上半年各地区商品销售额统计', fontdict={'fontsize': 20})
plt.axis('off')
plt.tick_params(top='off', right='off')
plt.show()
