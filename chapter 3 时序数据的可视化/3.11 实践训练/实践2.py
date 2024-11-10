import matplotlib.pyplot as plt
import numpy as np
from dbconn import conn

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

cursor = conn.cursor()
sql_num = "SELECT weekofyear(order_date), count(order_id) FROM orders WHERE dt=2020 and 'return'=0 and weekofyear(order_date) <= 26 GROUP BY weekofyear(order_date)"
cursor.execute(sql_num)
sh = cursor.fetchall()
v1 = []
v2 = []
for s in sh:
    v1.append(s[0])
    v2.append(s[1])

plt.figure(figsize=(11, 7))
plt.plot(v1, v2, marker='*', color='magenta', linewidth=3.0, linestyle='--', markersize=10)
plt.ylim((-1, 100))
plt.xticks(np.arange(0, 27, 2), rotation=45, fontsize=13)
plt.yticks(np.arange(0, 101, 10), fontsize=13)
plt.xlabel("日期（第几周）", fontsize=13)
plt.ylabel("有效订单量", fontsize=13)
plt.title("2020年上半年企业每周的商品有效订单量", fontsize=16)

plt.show()
