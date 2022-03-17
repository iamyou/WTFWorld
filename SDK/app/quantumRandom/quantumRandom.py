import requests
from bs4 import BeautifulSoup
import json

def QuantumRandomNumber(randomAmount,randomLimit):
    if(int(randomAmount) > 1000 or int(randomAmount) < 0 or int(randomLimit) > 10000 or int(randomLimit) < 0):
        return "int randomAmount 0 ~ 1000 int randonLimit 0 ~ 10000"
    else:
        apiUrl = 'http://www.randomnumbers.info/cgibin/wqrng.cgi'
        randomINI = {
            'amount':str(int(randomAmount)),
            'limit':str(int(randomLimit))
        }
        apiReturn = requests.post(apiUrl,randomINI)
        if (apiReturn == "<Response [404]>"):
            return "Quantum machine disconnected"
        else:
            apiReturn.encoding = 'utf-8'
            apiReturn_html = apiReturn.text
            apiReturnData = BeautifulSoup(apiReturn_html,features='html.parser')
            stringID = 0
            for string in apiReturnData.strings:
                if(stringID == 19):
                    randomData = string
                stringID += 1
            return randomData.split()

def EventHappenJudge(event):#{"eventName":(int)0~1,...} << eventList << (json) << {"event":[(list)...]}
    event_loads = json.loads(event)
    eventList = event_loads["event"]
    eventNum = len(eventList)
    eventHappen = QuantumRandomNumber(eventNum,"1")
    eventHappenJudge = {}
    eventID = 0
    for eventName in eventList:
        eventHappenJudge[eventName] = int(eventHappen[eventID])
        eventID +=1
    return json.dumps(eventHappenJudge)