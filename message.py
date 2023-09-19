import basicMeassage
################################
#type=0为HTML类型，type=1为callback类型 type=2为callback_mysql类型
################################
def HTMLMessage(HTML):
    return basicMeassage.basicMessage(0,HTML,"")
def CallBackMessage(returnValue,outputLocation):
    return basicMeassage.basicMessage(1,returnValue,outputLocation)
def CallBackMessage_mysql(returnValue,outputLocation):
    return basicMeassage.basicMessage(2,returnValue,outputLocation)
def DownloadMessage(returnValue,outputLocation):
    return basicMeassage.basicMessage(3,returnValue,outputLocation)