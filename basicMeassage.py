import json


def basicMessage(type,context,other):
    message={
        "type":type,
        "context":context,
        "other":other
    }

    #type为报文类型 context为报文主要内容 other为报文其他内容
    return json.dumps(message)


#前端报文  type类别一致
# message={
#         "type":type,
#         "context":context,
#         "other":other
#     }