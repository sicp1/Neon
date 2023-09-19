#起点
import asyncio
import websockets
from threading import Thread
from basicVar import myData
import AnalysisData.analysisBasic
import MySqlData.mySqlBasic
import basic
import basicData
import basicVar
import mainData
import mainFunc
from AnalysisData import analysisBasic,analysisFunc
from AnalysisData.analysisFunc import LineChart, BarChart
from AnalysisData.analysisBasic import ToStrData,SelectDataByIndex
from MySqlData import mySqlBasic

from HTMLSocket import HTMLSocket
from MySqlData.mySqlFunc import ShowMySqlDataBases ,GetTableAllData
from ExcelData.excelBasic import GetAllData
def init():#初始化
    basicData.GetExcel_Sheet("./static/FirstData.xlsx","回收订单明细","firstdata")
    basicData.SelectNowExcel("firstdata")
    mainData.MainData()
init()
###用户编写区域############
async def start(websocket):

    print("-----start-----")
    await mainFunc.NormalCard(websocket,BarChart("bar1",myData["firstdata_7_8_name"],myData['firstdata_7_8_data'],"型号与报单数量")+
                              BarChart("bar2",myData['firstdata_7_12_name'],myData['firstdata_7_12_data'],"型号与收单数量")+
                              BarChart("bar3",myData['firstdata_7_name'],myData['firstdata_8_data'],"型号与报单数量"),"数据分析")
    # await mainFunc.NormalCard(websocket,mainFunc.BeautifulInput("x1","请在这里输入x1")+
    #
    # mainFunc.BeautifulInput("x2","请在这里输入x2")+
    # mainFunc.NextLine()
    # +mainFunc.BeautifulButton("计算","GenShenStart","""["x1","x2"]""","y1")
    # +mainFunc.NextLine()
    # +mainFunc.BeautifulOutPut("y1","输出")
    #                           ,"结果")LineChart("firstLove",myData['sztu1'],myData['sztu2'], "excel1")+
    #                               LineChart("twiceLove",myData['863_1'],myData['863_2'],"excel2")+
    # await mainFunc.NormalCard(websocket, mainFunc.BeautifulInput("x1", "请在这里输入x1") +
    #                           mainFunc.BeautifulInput("x2","请在这里输入x2")+
    #                            mainFunc.NextLine()
    #                            +mainFunc.BeautifulButton("计算","GenShenStart","""["x1","x2"]""","y1")
    #                            +mainFunc.NextLine()
    #                            +mainFunc.BeautifulOutPut("y1","输出") ,"结果")
    #
    # await mainFunc.NormalCard(websocket, BarChart("threeLove",myData['863_1'],myData['863_2'],'excel3')+LineChart("firstLove",myData['sztu1'],myData['sztu2'], "excel1")+
    #                             LineChart("twiceLove",myData['863_1'],myData['863_2'],"excel2"), "数据分析")
     #await mainFunc.NormalCard(websocket,ShowMySqlDataBases("mysql1",5)+mainFunc.BeautifulOutPut("mysql1","数据库mysql1"),"数据库")
#################
async def Main(websocket, path):
    await start(websocket)
    async for callback in websocket:
        await basic.CallAtom(callback,websocket)
Thread_HTMLSocket = Thread(target=HTMLSocket)
Thread_HTMLSocket.start()
start_server = websockets.serve(Main, "127.0.0.1", 8888)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


