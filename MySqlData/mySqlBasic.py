import basicVar
import pandas as pd


def ShowTables():
    mycursor = basicVar.mydb.cursor()
    mycursor.execute("show tables")
    tables=[]
    for x in mycursor:
        print(x[0])
        tables.append(x[0])
    return tables
def GetTableAllData(table):
    mycursor=basicVar.mydb.cursor()
    mycursor.execute("select * from "+table)
    return mycursor.fetchall()
def GetTableLimitData(table,num):
    mycursor=basicVar.mydb.cursor()
    print("select *from "+table+" limit "+str(num))
    mycursor.execute("select *from "+table+" limit "+str(num))
    return mycursor.fetchall()

