import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from dbconn import conn
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


cursor = conn.cursor()
sql_num = "SELECT trade_date,amount FROM stocks WHERE year(trade_date)=2020 order by trade_date asc"
cursor.execute(sql_num)
sh = cursor.fetchall()
v1 = []
v2 = []
for s in sh:
    v1.append(s[0])
    v2.append(s[1])
data = pd.DataFrame(v2, v1)


plot_acf(data, lags=40)
plt.title("股票成交额的自相关图")
plt.show()


plot_pacf(data, lags=40)
plt.title("股票成交额的偏相关图")
plt.show()
