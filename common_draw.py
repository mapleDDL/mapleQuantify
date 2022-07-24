import matplotlib.pyplot as plt
import numpy as np

# 折线图绘制 支持多条折线
def drawPolyLine(dataList, lineType='solid', color='r', xlabel='date', ylabel='value'):
    if(len(dataList) == 1):
        plt.plot(dataList[0][0], dataList[0][1], ls=lineType, color=color)
    else:
        for i in dataList:
            plt.plot(i[0], i[1], ls=lineType)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(linestyle='--', linewidth=0.5)
    plt.show()

# 柱状图绘制
def drawBar(xData, yData, color='SeaGreen', xlabel='date', ylabel='value', width=0.5):
    plt.bar(xData, yData, color=color, width=width)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def test():
    xpoints0 = np.array(["2022-6-20", "2022-6-21", "2022-6-22", ""])
    ypoints0 = np.array([6, 2, 13, 10])
    xpoints1 = np.array(["2022-6-21", "2022-6-22", ""])
    ypoints1 = np.array([4, 11, 9])
    dataList = []
    dataList.append([xpoints0, ypoints0])
    dataList.append([xpoints1, ypoints1])
    drawPolyLine(dataList)


if __name__ == '__main__':
    test()