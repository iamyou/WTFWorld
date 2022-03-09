import json
import os
import openpyxl
import threading

class Excel:
    def __init__(self,excelPath,excelSheet):
        self.wb = openpyxl.workbook(excelPath)
        self.ws = wb[excelSheet]
    def getCellMax(self,rowOrcolumn):
        if (roOrcolumn == "row"):
            return self.ws.max_row
        else:
            return self.ws.max_column
    def getCellValue(self,row,list):
        return self.ws(row,list).value

def logoPrinter():
    print("________       .___                                  __      __            .__       .___")
    print("\_____  \    __| _/__.__. ______ ______ ____ ___.__./  \    /  \___________|  |    __| _/")
    print(" /   |   \  / __ <   |  |/  ___//  ___// __ <   |  |\   \/\/   /  _ \_  __ \  |   / __ | ")
    print("/    |    \/ /_/ |\___  |\___ \ \___ \\  ___/\___  | \        (  <_> )  | \/  |__/ /_/ | ")
    print("\_______  /\____ |/ ____/____  >____  >\___  > ____|  \__/\  / \____/|__|  |____/\____ | ")
    print("        \/      \/\/         \/     \/     \/\/            \/                         \/ ")
    print("  _________________   ____  __. __________      .__.__       .___                        ")
    print(" /   _____/\______ \ |    |/ _| \______   \__ __|__|  |    __| _/___________             ")
    print(" \_____  \  |    |  \|      <    |    |  _/  |  \  |  |   / __ |/ __ \_  __ \            ")
    print(" /        \ |    `   \    |  \   |    |   \  |  /  |  |__/ /_/ \  ___/|  | \/            ")
    print("/_______  //_______  /____|__ \  |______  /____/|__|____/\____ |\___  >__|               ")
    print("        \/         \/        \/         \/                    \/    \/                   ")

def ResetRowAndColumn():
    global row
    global column
    row = 1
    column = 1

def PackageList_getConfigcolumn():
    global column_program
    global column_language
    global column_type
    global column_moduleRequired
    global column_tag
    global column_compiledInto
    global column_class
    global column_logicPath
    packageList = Excel("./packageList.xlsx","main")
    max_column = packageList.getCellMax("column")
    ResetRowAndColumn()
    while(column<max_column+1):
        if(packageList.getCellValue(1,column) == "PROGRAM"):
            column_program = column
        elif(packageList.getCellValue(1,column) == "LANGUAGE"):
            column_language = column
        elif (packageList.getCellValue(1, column) == "TYPE"):
            column_type = column
        elif (packageList.getCellValue(1, column) == "MODULE REQUIRED"):
            column_moduleRequired = column
        elif (packageList.getCellValue(1, column) == "TAG"):
            column_tag = column
        elif (packageList.getCellValue(1, column) == "COMPILED INTO"):
            column_compiledInto = column
        elif (packageList.getCellValue(1, column) == "CLASS"):
            column_class = column
        elif (packageList.getCellValue(1, column) == "LOGIC PATH"):
            column_logicPath =column
        else:
            pass
        column +=1

def PackageList_identifyLogicPath():#Depends on PackageList_getConfigcolumn()
    list_program = []
    list_language = []
    list_type = []
    list_moduleRequired = []
    list_tag = []
    list_compiledInto = []
    list_class = []
    list_logicPath = []
    list_programPath = []
    packageList = Excel("./packageList.xlsx", "main")
    max_row = packageList.getCellMax("row")
    ResetRowAndColumn()
    row +=1
    while(row<max_row+1):
        list_program.append(packageList.getCellValue(row,column_program))
        list_language.append(packageList.getCellValue(row,column_language))
        list_type.append(packageList.getCellValue(row,column_type))
        list_moduleRequired.append(packageList.getCellValue(row,column_moduleRequired))
        list_tag.append(packageList.getCellValue(row,column_tag))
        list_compiledInto.append(packageList.getCellValue(row,column_compiledInto))
        list_class.append(packageList.getCellValue(row,column_class))
        list_logicPath.append(packageList.getCellValue(row,column_logicPath))
        row +=1
    row = 0
    while(row < max_row):
        list_programPath.append("..\\source\\" + list_class[row] + "\\" + list_program[row])
        row +=1

def dllmake_auto():
    list_dll_program = []
    list_dll_programID = []
    row = 0
    for compiledInto in list_compiledInto:
        if (compiledInto = "dll"):
            list_dll_programID.append(row)
        row += 1
    for programID = list_dll_programID:
        list_dll_program.append(list_programPath[programID])