# 计算5日线相关的数据
from datetime import date
import common_draw
import pandas as pd
import common

# 配置信息
depositoryExcelName = "maple的小仓.xlsx"

def mainAllAbout5days():

    nameList, codeList = common.getMyStocks()
    data = pd.read_excel(depositoryExcelName, sheet_name=nameList[0])

    xLineList     = []
    yLineList     = []
    xLineList5Day = []
    yLineList5Day = []
    drawList      = []
    sum5day       = 0
    for i in range(len(data)):
        if i < 5:
            sum5day += data["close"][i]
        else:
            sum5day += data["close"][i]
            sum5day -= data["close"][i-5]
            xLineList5Day.append(i)
            yLineList5Day.append(sum5day*1.0/5)
        xLineList.append(i)
        yLineList.append(data["close"][i])

    drawList.append([xLineList, yLineList])
    drawList.append([xLineList5Day, yLineList5Day])
    common_draw.drawPolyLine(drawList)
    return 0


if __name__ == "__main__":
    mainAllAbout5days()