import json
import os
import openpyxl
import shutil

programPool = {}

class Program:
    def __init__(self,name=None,extension=None,type=None,moduleRequired=None,tag=None,compiledInto=None,devClass=None):
        self.Name = name
        self.Extension = extension
        self.Type = type
        self.ModuleRequired = moduleRequired
        self.Tag = tag
        self.CompiledInto = compiledInto
        self.Class = devClass
    def Path(self):
        return  self.Name + "." + self.Extension

class File:
    def __init__(self,filePath,fileName):
        self.FilePath = filePath
        self.FileName = fileName
        if (os.path.exists(filePath) == False):
            os.makedirs(filePath)
    def Write(self,content):
        file = open(self.FilePath + "\\" + self.FileName,"w")
        file.write(content)
        file.close()

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

def LogoPrinter():
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

def PackageList_identity():
    global programPool
    packageList = Excel("./packageList.xlsx","main")
    max_column = packageList.getCellMax("column")
    max_row = packageList.getCellMax("row")
    ResetRowAndColumn()
    while(column<max_column+1):
        if(packageList.getCellValue(1,column) == "PROGRAM"):
            column_program = column
        elif(packageList.getCellValue(1,column) ==t_extension):
            column_extension = column
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
            column_logicPath = column
        else:
            pass
        column +=1
    ResetRowAndColumn()
    row +=1
    while(row<max_row+1):
        programName = packageList.getCellValue(row,column_program)
        exec("{} = Program(\"{}\")".format(programName,packageList.getCellValue(row,column_program)))
        exec("{}.Extension = \"{}\"".format(programName,packageList.getCellValue(row,column_extension)))
        exec("{}.Type = \"{}\"".format(programName,packageList.getCellValue(row,column_type)))
        exec("{}.ModuleRequired = \"{}\"".format(programName,packageList.getCellValue(row,column_moduleRequired)))
        exec("{}.Tag = \"{}\"".format(programName,packageList.getCellValue(row,column_tag)))
        exec("{}.CompiledInte = \"{}\"".format(programName,packageList.getCellValue(row,column_compiledInto)))
        exec("{}.Class = \"{}\"".format(programName,packageList.getCellValue(row,column_class)))
        exec("programPool[\"{}\"] = {}".format(programName.programName))
        row +=1

def Compiled_dll(program,sourcePath,compiledPath):
    if (program.Extension == "c"):
        debug = os.popen("gcc " + sourcePath + "\\" + program.Path() + " -shared -o " + compiledPath + "\\" + program.Name + ".dll")
        if(os.path.exists(compiledPath + "\\" + program.Name + ".dll") == False):
            debugLog = File(compiledPath,"error-compiled-dll-" + program.Name + ".log")
            debugLog.Write(debug.read())
            return False
        else:
            return True
    elif (program.Extension == "cpp")
        debug = os.popen("g++ " + sourcePath + "\\" + program.Path() + " -shared -o " + compiledPath + "\\" + program.Name + ".dll")
        if (os.path.exists(compiledPath + "\\" + program.Name + ".dll") == False):
            debugLog = File(compiledPath, "error-compiled-dll-" + program.Name + ".log")
            debugLog.Write(debug.read())
            return False
        else:
            return True
    elif (program.Extension == "py")
        shutil.copyfile(sourcePath + "\\" + program.Path(),compiledPath + "\\" + program.Name + "\\" + program.Name + ".py")
        pydSetUp = File(compiledPath,program.Name + "\\setup.py")
        pydSetUp.Write("from distutils.core import setup\nfrom Cython.Build import cythonize\nsetup(ext_modules=cythonize(" + program.Name + ".py\"))")
        debug = os.popen("python " + compiledPath + "\\" + program.Name + "\\setup.py" + " build_ext --inplace")
        if (os.path.exists(compiledPath + "\\" + program.Name + "\\" + program.Name + ".cp37-win_amd64" + ".pyd") == False):#TODO:".cp37-win_amd64" must be depended on developers' devices
            debugLog = File(compiledPath, "error-compiled-pyd-" + program.Name + ".log")
            debugLog.Write(debug.read())
            os.remove(compiledPath + "\\" + program.Name)
            return False
        else:
            shutil.copyfile(compiledPath + "\\" + program.Name + "\\" + program.Name + ".cp37-win_amd64" + ".pyd",compiledPath + "\\" + program.Name + ".pyd")
            os.remove(compiledPath + "\\" + program.Name)
            return True
    else:
        pass