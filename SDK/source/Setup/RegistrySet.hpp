#include "../WindowsRegistry/WindowsRegistry.h"

namespace RegistrySet {
    BOOL Install() {
        WindowsRegistry::Op registryInstall;
        return registryInstall.CreateKey("SOFTWARE//OdysseyWorld//FolderPoint");
    }

    BOOL Uninstall(){
        WindowsRegistry::Op registryUninstall;
        return registryUninstall.DeleteKey("HKEY_LOCAL_MACHINE","SOFTWARE//OdysseyWorld//FolderPoint");
    }
}
