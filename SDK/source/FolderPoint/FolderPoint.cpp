#define DLLEXPORT extern "C" __declspec(dllexport)

/*
#include <iostream>
#include <string>
*/
#include "../WindowsRegistry/WindowsRegistry.h"

namespace FolderPoint{
    const int logicLayer = 3;
    const int logicLayerChar = logicLayer * 2;
    /*
    void concreteConsist(char top[],char tail[]=""){
        if (std::strcmp(tail,"") == 0){
            std::strcpy(concretePath,top);
        } else{
            std::strcpy(concretePath,top);
            std::strcat(concretePath,"\\");
            std::strcat(concretePath,tail);
        }
    }
    */
}

DLLEXPORT BOOL filePath(LPCTSTR logicPath,std::string *concretePath){
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

/*
DLLEXPORT char* filePath(char *logicPath) {
    if (std::strlen(logicPath) > FolderPoint::logicLayerChar){
        std::cout << "error" << std::endl;
    }else{
        if (std::strcmp(logicPath,"a") == 0) {
            FolderPoint::concreteConsist(FolderPoint::concreteTop_Main);
        }
        if (std::strcmp(logicPath,"a1") == 0) {

            FolderPoint::concreteConsist(FolderPoint::concreteTop_Main,"character");
        }
        if (std::strcmp(logicPath,"a2") == 0) {
            FolderPoint::concreteConsist(FolderPoint::concreteTop_Main,"environment");
        }
        if (std::strcmp(logicPath,"a3") == 0) {
            FolderPoint::concreteConsist(FolderPoint::concreteTop_Main,"resource");
        }
    }
    return FolderPoint::concretePath;
}
 */