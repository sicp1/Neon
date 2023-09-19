import pandas as pd

from MySqlData.mySqlBasic import GetTableAllData


def DownloadMysqlDataAsExcel(table):
    Arr=GetTableAllData(table)
    print(Arr)
    MysqlData=pd.DataFrame(data=Arr)
    MysqlData.to_excel("./DownLoad_Excel/"+table+".xlsx")
