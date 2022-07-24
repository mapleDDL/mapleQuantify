import time

def getTodayDate():
    timeNow       = time.time()
    timeNowStruct = time.localtime(timeNow)
    timeRes = str(timeNowStruct.tm_year) + '-' + str(timeNowStruct.tm_mon) + '-' + str(timeNowStruct.tm_mday)
    return timeRes

def getBeginDate():
    timeNow       = time.time()
    timeNowStruct = time.localtime(timeNow)
    timeRes = str(timeNowStruct.tm_year) + '-01-01'
    return timeRes

def test():
    formatDate = getTodayDate()
    print(formatDate)

if __name__ == '__main__':
    test()
