import mysql.connector
import pandas as pd
import pymysql
import basicVar


def GetMysql(host,user,password,database,port,name):
    mydb = pymysql.connect(
        host=host,  # 数据库主机地址
        user=user,# 数据库用户名
        passwd=password  # 数据库密码

        ,charset='utf8',
        db=database,
        port=port
    )
    basicVar.mydbArr[name]=mydb


def GetExcel_Sheet(Path,sheet,name):
    basicVar.excelArr[name]=pd.read_excel(Path,sheet_name=sheet)
def GetExcel(Path,name):#示例C:\\Users\\ASUS\\PycharmProjects\\b2021\\fujian2.xlsx
    basicVar.excelArr[name]=pd.read_excel(Path)

def SelectNowExcel(name):
    basicVar.excel=basicVar.excelArr[name]
    return ""
def SelectNowDb(name):
    basicVar.mydb=basicVar.mydbArr[name]
    return ""