import MySqlData
import mainFunc
from MySqlData.mySqlBasic import ShowTables, GetTableLimitData, GetTableAllData


def ShowMySqlDataBases(name,num):#name为唯一的名字 num为想要展示多少个数据
    tables=ShowTables()
    HTML_button=""
    for table in tables:
        #mainFunc.BeautifulButton("原神","GenShenStart","""["x1","x2"]""","y1")
        HTML_button+=mainFunc.BeautifulButtonForMysql(table,"GetTableLimitData_TableHTML","""["{table}","{num}"]""".format(table=table,num=num),str(name))
    return HTML_button
def GetTableLimitData_TableHTML(table,num):
    Arr=GetTableLimitData(table,num)
    return mainFunc.TableShowMysqlData(Arr)+ mainFunc.BeautifulButtonForMysqlToExcel("下载数据表"+table,"DownloadMysqlDataAsExcel",table)




