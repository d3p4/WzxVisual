import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

month = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
sales = [200, 197, 233, 216, 345, 319, 197, 357, 376, 416, 355, 408]

plt.figure(figsize=(11, 7))
plt.plot(month, sales, linestyle='-.', marker='*', color='green', markersize=10, linewidth=3.0)
plt.tick_params(labelsize=16)
plt.xlabel('月份', size=16)
plt.ylabel('订单量', size=16)
plt.title('2019年12个月某企业商品的订单量分析', loc='center', size=20)

plt.show()
