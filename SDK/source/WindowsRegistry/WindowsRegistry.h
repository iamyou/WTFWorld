#include <windows.h>
#include <assert.h>
#include <string.h>
#include <iostream>
#include <Winreg.h>
#ifndef WindowsRegistry_H
#define WindowsRegistry_H

namespace WindowsRegistry{
    class Op{
        private:
            HKEY cHKey;
        public:
            Op(HKEY hKey = HKEY_CURRENT_USER){//Get Administrator exchange:HKEY_LOCAL_MACHINE
                cHKey = hKey;
            };
            BOOL SetHKEY(LPCTSTR strKey);
            BOOL OpenKey(LPCTSTR lpSubKey);
            void Close();
            BOOL CreateKey(LPCTSTR lpSubKey);
            BOOL DeleteKey( LPCTSTR lphKey, LPCTSTR lpSubKey );
            BOOL DeleteValue( LPCTSTR lpValueName );
            BOOL SaveKey( LPCTSTR lpFileName );
            BOOL RestoreKey( LPCTSTR lpFileName );
            BOOL Read( LPCTSTR lpValueName, std::string* lpVal );
            BOOL Read( LPCTSTR lpValueName, DWORD* pdwVal );
            BOOL Read( LPCTSTR lpValueName, int* pnVal );
            BOOL Write( LPCTSTR lpSubKey, LPCTSTR lpVal );
            BOOL Write( LPCTSTR lpSubKey, DWORD dwVal );
            BOOL Write( LPCTSTR lpSubKey, int nVal );
            ~Op(){
                Close();
            }
    };

    /*
    LPCTSTR BasicSubKey = "SOFTWARE//OdysseyWorld";
    LPCTSTR lpSubKeyConsist(LPCTSTR lpSubKeyTail){
        LPCTSTR subKey = BasicSubKey;
        std::strcat(subKey,"//");
        std::strcat(subKey,lpSubKeyTail);
        return subKey;
    }
    */

    BOOL Op::SetHKEY(LPCTSTR strKey) {
        assert(cHKey);
        assert(strKey);
        if( 0 == strcmp(strKey,"HKEY_CLASSES_ROOT") )
        {
            cHKey = HKEY_CLASSES_ROOT;
            return TRUE;
        }
        if( 0 == strcmp(strKey,"HKEY_CURRENT_USER") )
        {
            cHKey = HKEY_CURRENT_USER;
            return TRUE;
        }
        if( 0 == strcmp(strKey,"HKEY_LOCAL_MACHINE") )
        {
            cHKey = HKEY_LOCAL_MACHINE;
            return TRUE;
        }
        if( 0 == strcmp(strKey,"HKEY_USERS") )
        {
            cHKey = HKEY_USERS;
            return TRUE;
        }
        if( 0 == strcmp(strKey,"HKEY_PERFORMANCE_DATA") )
        {
            cHKey = HKEY_PERFORMANCE_DATA;
            return TRUE;
        }
        if( 0 == strcmp(strKey,"HKEY_PERFORMANCE_TEXT") )
        {
            cHKey = HKEY_PERFORMANCE_TEXT;
            return TRUE;
        }
        if( 0 == strcmp(strKey,"HKEY_PERFORMANCE_NLSTEXT") )
        {
            cHKey = HKEY_PERFORMANCE_NLSTEXT;
            return TRUE;
        }
#if(WINVER >= 0x0400)
        if( 0 == strcmp(strKey,"HKEY_CURRENT_CONFIG") )
    {
        cHKey = HKEY_CURRENT_CONFIG;
        return TRUE;
    }
    if( 0 == strcmp(strKey,"HKEY_DYN_DATA") )
    {
        cHKey = HKEY_DYN_DATA;
        return true;
    }
#endif
        return false;
    }

    BOOL Op::OpenKey(LPCTSTR lpSubKey) {
        //lpSubKey = lpSubKeyConsist(lpSubKeyTail);
        assert(cHKey);
        assert(lpSubKey);
        HKEY hKey;
        long lReturn = RegOpenKeyEx(cHKey, lpSubKey, 0L, KEY_READ | KEY_WRITE | KEY_EXECUTE, &hKey);
        if(ERROR_SUCCESS == lReturn){
            cHKey =hKey;
            return true;
        }
        return false;
    }

    void Op::Close() {
        if(cHKey){
            RegCloseKey(cHKey);
            cHKey = NULL;
        }
    }

    BOOL Op::CreateKey(LPCTSTR lpSubKey){
        //lpSubKey = lpSubKeyConsist(lpSubKeyTail);
        assert(cHKey);
        assert(lpSubKey);
        HKEY hKey;
        DWORD dw;
        long lReturn = RegCreateKeyEx(cHKey,lpSubKey,0L, NULL, REG_OPTION_VOLATILE, KEY_ALL_ACCESS, NULL, &hKey, &dw);
        if(ERROR_SUCCESS == lReturn){
            cHKey = hKey;
            return true;
        }
        return false;
    }

    BOOL Op::DeleteKey(LPCTSTR lphKey, LPCTSTR lpSubKey) {
        assert(lphKey);
        assert(lpSubKey);
        assert(cHKey);
        SetHKEY(lphKey);
        long lReturn = RegDeleteValue(cHKey,lpSubKey);
        if (ERROR_SUCCESS == lReturn){
            return true;
        }
        return false;
    }

    BOOL Op::DeleteValue(LPCTSTR lpValueName) {
        assert(cHKey);
        assert(lpValueName);
        long lReturn = RegDeleteValue(cHKey, lpValueName);
        if (ERROR_SUCCESS == lReturn){
            return true;
        }
        return false;
    }

    BOOL Op::SaveKey(LPCTSTR lpFileName)
    {
        assert(cHKey);
        assert(lpFileName);
        long lReturn = RegSaveKey(cHKey,lpFileName,NULL);
        if( ERROR_SUCCESS == lReturn ){
            return true;
        }
        return false;
    }

    BOOL Op::RestoreKey(LPCTSTR lpFileName)
    {
        assert(cHKey);
        assert(lpFileName);
        long lReturn = RegRestoreKey(cHKey,lpFileName,0);
        if(ERROR_SUCCESS == lReturn){
            return true;
        }
        return false;
    }

    BOOL Op::Read(LPCTSTR lpValueName, std::string* lpVal)
    {
        assert(cHKey);
        assert(lpValueName);
        assert(lpVal);
        DWORD dwType;
        DWORD dwSize=200;
        char szString[2048];
        memset(szString, 0, 2048 * sizeof(char));
        long lReturn = RegQueryValueEx( cHKey, lpValueName, NULL, &dwType, (BYTE *)szString, &dwSize );
        if(ERROR_SUCCESS == lReturn){
            *lpVal = szString;
            return true;
        }
        return false;
    }

    BOOL Op::Read(LPCTSTR lpValueName, DWORD* pdwVal)
    {
        assert(cHKey);
        assert(lpValueName);
        assert(pdwVal);
        DWORD dwType;
        DWORD dwSize=sizeof(DWORD);
        DWORD dwDest;
        long lReturn = RegQueryValueEx(cHKey, lpValueName, NULL, &dwType, (BYTE *)&dwDest, &dwSize );
        if(ERROR_SUCCESS == lReturn){
            *pdwVal = dwDest;
            return true;
        }
        return false;
    }

    BOOL Op::Read(LPCTSTR lpValueName, int* pnVal)
    {
        assert(cHKey);
        assert(lpValueName);
        assert(pnVal);
        DWORD dwType;
        DWORD dwSize=sizeof(DWORD);
        DWORD dwDest;
        long lReturn = RegQueryValueEx(cHKey, lpValueName, NULL, &dwType, (BYTE *)&dwDest, &dwSize );
        if(ERROR_SUCCESS == lReturn){
            *pnVal=(int)dwDest;
            return true;
        }
        return false;
    }

    BOOL Op::Write(LPCTSTR lpValueName, LPCTSTR lpValue)
    {
        assert(cHKey);
        assert(lpValueName);
        assert(lpValue);
        long lReturn = RegSetValueEx(cHKey, lpValueName, 0L, REG_SZ, (const BYTE *) lpValue, strlen(lpValue)+1 );
        if( ERROR_SUCCESS == lReturn )
        {
            return true;
        }
        return false;
    }

    BOOL Op::Write(LPCTSTR lpSubKey, DWORD dwVal)
    {
        assert(cHKey);
        assert(lpSubKey);
        long lReturn = RegSetValueEx(cHKey, lpSubKey, 0L, REG_DWORD, (const BYTE *) &dwVal, sizeof(DWORD) );
        if(ERROR_SUCCESS == lReturn){
            return true;
        }
        return false;
    }

    BOOL Op::Write(LPCTSTR lpSubKey, int nVal)
    {
        assert(cHKey);
        assert(lpSubKey);
        DWORD dwValue;
        dwValue=(DWORD)nVal;
        long lReturn = RegSetValueEx( cHKey, lpSubKey, 0L, REG_DWORD, (const BYTE *) &dwValue, sizeof(DWORD) );
        if( ERROR_SUCCESS == lReturn )
        {
            return true;
        }
        return false;
    }
}

#endif