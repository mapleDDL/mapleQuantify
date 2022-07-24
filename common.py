# 通用函数
stockNameFile = 'myStocks.txt'

def getMyStocks():
    stockFile = open(stockNameFile, 'r', encoding='UTF-8')
    nameList = []
    codeList = []
    line = stockFile.readline()
    while line:
        if len(line) > 1:
            lineSplit = line.split(' ')
            nameList.append(lineSplit[0])
            codeList.append(lineSplit[1])
            line = stockFile.readline()
        else:
            line = stockFile.readline()
    return nameList.copy(), codeList.copy()