#define DLLEXPORT extern "C" __declspec(dllexport)

/*
#include <iostream>
#include <string>
*/
#include "../WindowsRegistry/WindowsRegistry.h"

DLLEXPORT BOOL FolderPoint(LPCTSTR logicPath,std::string *concretePath){
    WindowsRegistry::Op registryRead;
    if (registryRead.OpenKey("SOFTWARE\\OdysseyWorld\\FolderPoint") == false){
        return false;
    }else{
        if (registryRead.Read(logicPath,concretePath) == false){
            return false;
        }else{
            return true;
        }
    }
}
DLLEXPORT BOOL FolderPoint_register(char* headerPath,char* folderName,char* logicPathLevel,char* logicPath){
    WindowsRegistry::Op registryRead;
    if (registryRead.OpenKey("SOFTWARE\\WTFWorld\\FolderPoint") == false) {
        return false;
    }else{
        return true;
    }
}

