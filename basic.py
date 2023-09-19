#basicAtom#######
import json
import MySqlData.mySqlFunc
import userFunc
import basicDownload
import message
async def SendAtom(html,websocket):
    await websocket.send(html)
async def CallAtom(callback,websocket):
    CallBack=json.loads(callback)
    if CallBack["type"]==1:
        await websocket.send(message.CallBackMessage(eval("userFunc."+CallBack["context"]),CallBack["other"]))
    elif CallBack["type"]==2:
        await websocket.send(message.CallBackMessage_mysql(eval("MySqlData.mySqlFunc." + CallBack["context"]), CallBack["other"]))
    elif CallBack["type"]==3:
        await websocket.send(message.DownloadMessage(eval("basicDownload."+CallBack["context"]),CallBack["other"]))
##################

#cmdRun##################
def run_cmd(cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import run
    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True)
###########################
