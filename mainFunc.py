#数据分析函数
import basic
import message
async def NormalCard(websocket,contextHTML,title):
    HTML="<div class=\"card\"><div class=\"card-content\"><h2>{title}</h2><div class=\"contextHTML\">{contextHTML}</div></div></div>".format(title=title,contextHTML=contextHTML)
    await basic.SendAtom(message.HTMLMessage(HTML),websocket)
#####################################################################################################################
# #FuncName为函数名字如add，XArr为x名字，并且格式为[x1,x2,x3,x4]，注意x要顺序排列

def BeautifulButtonForMysql(text,FuncName,XArr,Y):#FuncName为函数名字如add，XArr为x名字，并且格式为[x1,x2,x3,x4]，注意x要顺序排列
    HTML="""<button onclick='mysqlForLimit("{FuncName}",{XArr},"{Y}")' style="display: inline-block;
                padding: 10px 20px;
                background-color: #3498db;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
                transition: background-color 0.3s ease;"
        onmouseover="this.style.backgroundColor='#2980b9';"
        onmouseout="this.style.backgroundColor='#3498db';">
  {text}
</button>
""".format(text=text,FuncName=FuncName,XArr=XArr,Y=Y)
    return HTML
def BeautifulButtonForMysqlToExcel(text,FuncName,Table):
    HTML = """<button onclick='mysqlDownloadExcel("{FuncName}","{Table}")' style="display: inline-block;
                    padding: 10px 20px;
                    background-color: #3498db;
                    color: #ffffff;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    text-align: center;
                    text-decoration: none;
                    transition: background-color 0.3s ease;"
            onmouseover="this.style.backgroundColor='#2980b9';"
            onmouseout="this.style.backgroundColor='#3498db';">
      {text}
    </button>
    """.format(text=text, FuncName=FuncName, Table=Table)
    return HTML

def BeautifulButton(text,FuncName,XArr,Y):#FuncName为函数名字如add，XArr为x名字，并且格式为[x1,x2,x3,x4]，注意x要顺序排列
    HTML="""<button onclick='CallBack("{FuncName}",{XArr},"{Y}")' style="display: inline-block;
                padding: 10px 20px;
                background-color: #3498db;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
                transition: background-color 0.3s ease;"
        onmouseover="this.style.backgroundColor='#2980b9';"
        onmouseout="this.style.backgroundColor='#3498db';">
  {text}
</button>
""".format(text=text,FuncName=FuncName,XArr=XArr,Y=Y)
    return HTML
def Space():
    return"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"
def NextLine():
    return "<br><br>"
def BeautifulInput(XLabel,placeholder):#XLabel为标记该输入框
    HTML="""
    <input type="text" id="{XLabel}" style="padding: 10px;
                          font-size: 16px;
                          border: 2px solid #3498db;
                          border-radius: 5px;
                          outline: none;
                          transition: border-color 0.3s ease;"
       onfocus="this.style.borderColor='#2980b9';"
       onblur="this.style.borderColor='#3498db';"
       placeholder="{placeholder}">
       """.format(XLabel=XLabel,placeholder=placeholder)
    return HTML
def BeautifulOutPut(Y,title):
    HTML="""
   <div style="padding: 5px;
            font-size: 16px;
            background-color: #f2f2f2;
            border: 2px solid #3498db;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: left;
            line-height: 1.6;">

  <h2 style="margin-bottom: 10px;">{title}</h2>
  
  <div id="{Y}"></div>
 
</div>
""".format(title=title,Y=Y)
    return HTML
def TableShowMysqlData(Arr):
    HTML="""
    <table border="1">
    
    """
    #二维
    HTML_inner=""
    for item in Arr:
        HTML_inner+="""<tr>"""
        for atom in item:
            HTML_inner+=""" 
  <td>{atom}</td>
""".format(atom=atom)
        HTML_inner+="""
        </tr>"""
    HTML+=HTML_inner
    HTML+="""
    </table>"""
    return HTML


