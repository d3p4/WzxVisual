import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_excel("D:/py_practice/python可视化/各章节数据源/ch09/经营数据.xls")
sns.pairplot(iris, hue='type',
             plot_kws={'alpha': 0.6, 's': 80, 'edgecolor': 'k'}, height=3)
plt.show()
