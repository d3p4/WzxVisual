import numpy as np
from matplotlib import pyplot as plt

#三维数据
x = [14,13,15,17,16,11,12]
y = [28.43,24.28,25.61,24.82,28.86,31.26,27.28]
z = [504.91,495.89,534.61,455.45,425.73,435.61,485.18]

#定义坐标轴
fig = plt.figure(figsize=(13,9))
ax1 = plt.axes(projection='3d')

#绘制散点图
cValue = ['r','y','g','b','r','y','g']
ax1.scatter3D(x,y,z,s=200,c=cValue,linewidths=y,marker='o')

#设置刻度值的字体大小
plt.tick_params(labelsize=13)

plt.show()