import numpy as np
import pandas as pd


def TwoTupleTOTwoList(Arr):
    Arr_ret=[]
    for item in Arr:
        Arr_ret.append(list(item))
    return Arr_ret
def DataToSumData(Arr,nameIndex,dataIndex):
    SumData={}
    for item in Arr:
        if item[nameIndex] in SumData:
            SumData[item[nameIndex]]+=item[dataIndex]
        else:
            SumData[item[nameIndex]]=item[dataIndex]
    return {"name":list(SumData.keys()),"data":list(SumData.values())}

def FillTheNan(Arr,fill):
    Arr=pd.DataFrame(Arr)
    print(Arr)
    return Arr.fillna(fill)


###################################################################\
#lambda

SelectDataByIndex=lambda Arr,Index:[item[Index] for item in Arr ]
ListToStr=lambda Arr:"["+",".join(Arr)+"]"
ToStrData=lambda Arr:['"'+str(item)+'"' for item in Arr]

