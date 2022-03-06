#define DLLEXPORT extern "C" __declspec(dllexport)
/*
#include <iostream>
#include <string>
*/
#include "../WindowsRegistry/WindowsRegistry.h"

BOOL filePath(LPCTSTR logicPath,std::string *concretePath){
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

int main(){
    char *dllPath_;
    dllPath("FolderPoint",dllPath_);
    std::cout << "3." << *dllPath_ << std::endl;
    return 0;
}