import baostock as bs
import pandas as pd
import common
import common_time

def logSystem():
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

def logoutSystem():
    bs.logout()

def initParams():
    fields    = 'date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST'
    beginDate = common_time.getBeginDate()
    endDate   = common_time.getTodayDate()                                                
    return fields, beginDate, endDate

def mainStock():

    logSystem()

    fields, beginDate, endDate = initParams()
    nameList, codeList         = common.getMyStocks()
    stockNum                   = len(nameList)
    writer                     = pd.ExcelWriter('maple的小仓.xlsx')

    for i in range(stockNum):
        
        rs = bs.query_history_k_data_plus(codeList[i][0:-1], fields, start_date=beginDate, end_date=endDate, frequency="d", adjustflag="3")
        if eval(rs.error_code) > 0:
            print('nameList[i]' + ' error code: ' + rs.error_code)
        print(nameList[i] + ' result: ' + rs.error_msg)
        
        data_list = []
        while (rs.error_code == '0') and rs.next():
            tempData = rs.get_row_data()
            data_list.append(tempData)
            result = pd.DataFrame(data_list, columns=rs.fields)
        
        result.to_excel(writer, sheet_name=nameList[i])

    writer.save()

    logoutSystem()


if __name__ == "__main__":
    mainStock()