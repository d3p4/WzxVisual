import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei']

x = np.arange(0, 30, 1)
y1 = 3*np.sin(2*x)+2*x+1
y2 = 2*np.cos(2*x)+3*x+9

plt.figure(figsize=(11, 7))

plt.plot(x, y1, linestyle='-.', color='red', linewidth=5.0)
plt.plot(x, y2, marker='*', color='green', markersize=10)

plt.xlabel('日期', size=16)
plt.ylabel("金额", size=16, rotation=90, verticalalignment='center')

x_major_locator = MultipleLocator(2)
y_major_locator = MultipleLocator(10)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.tick_params(labelsize=16)

plt.xlim(0, 30)
plt.ylim(0, 100)

plt.legend(labels=['利润额', '销售额'], loc='upper left', fontsize=15)
plt.title('2020年9月企业商品销售业绩分析', loc='center', size=20)
plt.show()
