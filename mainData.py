import basicData
from AnalysisData.analysisBasic import ToStrData, SelectDataByIndex, DataToSumData, FillTheNan

from ExcelData.excelBasic import GetAllData
from MySqlData.mySqlBasic import GetTableAllData
from basicVar import myData
def MainData():#数据处理
    all=GetAllData()
    del all[0]
    all_7_8=DataToSumData(all,7,8)
    all_7_12=DataToSumData(all,7,12)
    del all_7_8['name'][9]
    del all_7_8['data'][9]
    del all_7_12['name'][9]
    del all_7_12['data'][9]

    all_7_12['data'][8]=0
    all_7_8['data'][8]=0
    print("all_7_12:", all_7_12)
    myData['firstdata_7_8_name']=all_7_8['name']#_7_8黑白 数据
    myData['firstdata_7_8_data']=all_7_8['data']
    myData['firstdata_7_12_name']=all_7_12['name']
    myData['firstdata_7_12_data']=all_7_12['data']

    myData['firstdata_7_name']=SelectDataByIndex(FillTheNan(SelectDataByIndex(all,7),"").values.tolist(),0)

    myData['firstdata_8_data']=SelectDataByIndex(FillTheNan(SelectDataByIndex(all,8),0).values.tolist(),0)

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





