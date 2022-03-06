#include "../WindowsRegistry/WindowsRegistry.h"
#ifndef RegistrySet_H
#define RegistrySet_H

namespace RegistrySet {
    BOOL Install() {
        WindowsRegistry::Op registryInstall;
        if (registryInstall.CreateKey("SOFTWARE\\OdysseyWorld\\FolderPoint") == false){
            return false;
        }else{
            registryInstall.Write("a","OdysseyWorld");
            //
            registryInstall.Write("a1","OdysseyWorld\\character");
            registryInstall.Write("a1b1","OdysseyWorld\\character\\frameLib");
            //
            registryInstall.Write("a2","OdysseyWorld\\environment");
            //
            registryInstall.Write("a3","OdysseyWorld\\resource");
            return true;
        }
    }

    BOOL Uninstall(){
        WindowsRegistry::Op registryUninstall;
        return registryUninstall.DeleteKey("HKey_Current_User","SOFTWARE\\OdysseyWorld\\FolderPoint");
    }
}

#endif
