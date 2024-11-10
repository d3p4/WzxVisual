import seaborn as sns
import matplotlib.pyplot as plt

sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sns.set_style("white", {"axes.facecolor": '#FFFAFA'})
data = [[1.023312, 0.111484, 0.624475, 0.682342, 1.551981, 2.029264],
        [0.701567, 0.807321, 0.866991, 1.592059, 1.461618, 2.131652],
        [0.110403, 0.523769, 0.985059, 1.524016, 1.635007, 2.279868]]
sns.boxplot(data=data)
plt.show()
