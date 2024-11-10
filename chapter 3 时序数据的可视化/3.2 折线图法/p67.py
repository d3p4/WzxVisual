import matplotlib. pyplot as plt
import numpy as np
import pymysql
plt. rcParams['font.sans-serif'] = ['SimHei']
plt. rcParams['axes.unicode_minus'] = False

conn = pymysql.connect(host='127.0.0.1', port=3306, user='sales',
                       password='123456', db='sales', charset='utf8')
cursor = conn. cursor()

sql_num="SELECT weekofyear(order_date),ROUND(SUM(sales)/10000,2),ROUND(SUM(profit)/10000,2) FROM orders WHERE dt=2020 and weekofyear(order_date)<=26 GROUP BY weekofyear(order_date)"
cursor.execute(sql_num)
sh = cursor.fetchall()
v1 = []
v2 = []
v3 = []
for s in sh:
    v1.append(s[0])
    v2.append(s[1])
    v3.append(s[2])

plt. figure(figsize=(11, 7))
plt.plot(v1, v2, linestyle='-.', color='red', linewidth=3.0, label='销售额')
plt.plot(v1, v3, marker='*', color='green', markersize=10, label='利润额 ')

plt. ylim((-1, 16))
plt. xticks(np. arange(0, 27, 2), rotation=45, fontsize=13)
plt. yticks(np. arange(0, 17, 1), fontsize=13)
plt.xlabel("日期（第几周）", fontsize=13)
plt.ylabel("销售额与利润额", fontsize=13)
plt.title("2020年上半年企业每周销售额与利润额分析", fontsize=16)
plt. legend(loc='upper left', fontsize=13)
plt. show()
