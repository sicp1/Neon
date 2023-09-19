import basicData
from AnalysisData.analysisBasic import ToStrData, SelectDataByIndex, DataToSumData, FillTheNan

from ExcelData.excelBasic import GetAllData
from MySqlData.mySqlBasic import GetTableAllData
from basicVar import myData
def MainData():#数据处理
    data=GetAllData()
    print(data)
    motherAge_babyType=DataToSumData(data,9,1)
    del motherAge_babyType['name'][3]
    del motherAge_babyType['data'][3]
    myData['motherAge']=motherAge_babyType['data']
    myData['babyType']=motherAge_babyType['name']


    # myData['sztu1']=SelectDataByIndex(GetTableAllData("student_users"), 0)
    # myData['sztu2']=SelectDataByIndex(GetTableAllData("student_users"), 1)
    # #ToStrData(SelectDataByIndex(GetAllData(),9)),SelectDataByIndex(GetAllData(),1)
    # print(GetAllData())
    # a=DataToSumData(GetAllData(),9,1)
    # del a['name'][3]
    # del a['data'][3]
    # myData['863_1']=a['name']
    # myData['863_2']=a['data']
    # basicData.SelectNowExcel("fujian1")
    # print(GetAllData())







