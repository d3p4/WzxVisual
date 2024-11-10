import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def meanX(dataX):
    return np.mean(dataX, axis=0)


def pca(XMat, k):
    average = meanX(XMat)
    m, n = np.shape(XMat)
    avgs = np.tile(average, (m, 1))
    data_adjust = XMat - avgs
    covX = np.cov(data_adjust.T)
    featValue, featVec = np.linalg.eig(covX)
    index = np.argsort(-featValue)
    finalData = []
    if k > n:
        print("k must lower than feature number")
        return
    selectVec = np.matrix(featVec.T[index[:k]])
    finalData = data_adjust * selectVec.T
    reconData = (finalData * selectVec) + average
    return finalData, reconData


def loaddata(datafile):
    return np.array(pd.read_csv(datafile, sep="\t", header=None)).astype(np.float)


def plotBestFit(data1, data2):
    dataArr1 = np.array(data1)
    dataArr2 = np.array(data2)
    m = np.shape(dataArr1)[0]
    axis_x1 = []
    axis_y1 = []
    axis_x2 = []
    axis_y2 = []
    for i in range(m):
        axis_x1.append(dataArr1[i, 0])
        axis_y1.append(dataArr1[i, 1])
        axis_x2.append(dataArr2[i, 0])
        axis_y2.append(dataArr2[i, 1])
    fig = plt.figure(figsize=(11, 7))
    ax = fig.add_subplot(111)
    ax.scatter(axis_x1, axis_y1, s=50, c='red', marker='s')
    ax.scatter(axis_x2, axis_y2, s=50, c='blue')
    plt.xlabel('x1', fontsize=16)
    plt.ylabel('x2', fontsize=16)
    plt.title('2020年第三季度销售数据的变量降维', fontsize=20)
    plt.show()


def main():
    datafile = "D:/py_practice/python可视化/各章节数据源/ch09/经营数据.txt"
    XMat = loaddata(datafile)
    k = 2
    return pca(XMat, k)


if __name__ == "__main__":
    finalData, reconMat = main()
    plotBestFit(finalData, reconMat)