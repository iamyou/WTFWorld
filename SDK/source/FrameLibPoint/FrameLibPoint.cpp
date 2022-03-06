#define DLLEXPORT extern "C" __declspec(dllexport)
/*
#include <iostream>
#include <string>
*/
#include "../WindowsRegistry/WindowsRegistry.h"

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

BOOL dllPath(char* dllName,char *dllPath) {
    WindowsRegistry::Op registryRead;
    if (registryRead.OpenKey("SOFTWARE\\OdysseyWorld\\FolderPoint") == false) {
        return false;
    } else {
        std::string dllName_str = dllName;
        std::string dllPath_str;
        if (registryRead.Read("a1b1", dllPath_str) == false) {
            return false;
        } else {
            dllPath_str = dllPath_str + "\\" + dllName_str + ".dll";
            std::cout << dllPath_str << std::endl;
            return true;
        }
    }
}
int main(){
    char* dllPath_;
    dllPath("FolderPoint",dllPath_);
    return 0;
}