#define DLLEXPORT extern "C" __declspec(dllexport)
/*
#include <iostream>
#include <string>
*/
#include "../WindowsRegistry/WindowsRegistry.h"
#include <Python.h>

/*
DLLEXPORT BOOL dllPath(std::string dllName,std::string *dllPath){
    WindowsRegistry::Op registryRead;
    if (registryRead.OpenKey("SOFTWARE\\OdysseyWorld\\FolderPoint") == false){
        return false;
    }else{
        if (registryRead.Read("a1b1",dllPath) == false){
            return false;
        }else{
            *dllPath = *dllPath + "\\" + dllName + ".dll";
            return true;
        }
    }
}
*/

BOOL dllPath(std::string dllName,std::string *dllPath){
    WindowsRegistry::Op registryRead;
    if (registryRead.OpenKey("SOFTWARE\\OdysseyWorld\\FolderPoint") == false){
        return false;
    }else{
        if (registryRead.Read("a1b1",dllPath) == false){
            return false;
        }else{
            *dllPath = *dllPath + "\\" + dllName + ".dll";
            return true;
        }
    }
}

DLLEXPORT PyObject* dllPath_Py(PyObject* self, PyObject* args)
{
    char* name = new char[1024];
    char* path = new char[1024];
    if (!PyArg_ParseTuple(args, "ss", name, path)) 
    {
        return NULL;
    }
    else {
        std::string sName = name;
        std::string sP = path;
        std::string* sPath = &sP;
        if (dllPath(sName, sPath)) 
        {
            return Py_True;
        }
        else {
            return Py_False;
        }
    }
}

int main(){
    return 0;
}