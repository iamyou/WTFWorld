import json
import os

def filePath(path):
    if (os.path.exists(path) == False):
        os.makedirs(path)
    return path

def getPackList():
    packListFile = open(".\packList.json", "r")
    packList = json.loads(packListFile.read())
    packListFile.close()
    return packList

def compileDll(packList_dll):
    for dll in packList_dll:
        os.system("g++ " + "..\source\\" + dll + "\\" + dll + ".cpp -shared -o " + filePath("..\package\compiled\\") + dll + ".dll")

def packWorking():
    packList = getPackList()
    compileDll(packList["dll"])

packWorking()
