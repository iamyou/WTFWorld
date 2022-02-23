#define DLLEXPORT extern "C" __declspec(dllexport)
#include <string>

namespace folderPoint{
    int logicLayer = 3;
    int logicLayerChar = logicLayer * 2;
    char *concreteTailChar[logicLayer];
    concreteTail[0] = "OdysseyWorld";
    std::string concreteTop ="C:";
    std::string concreteTail;
    std::string concretePath;
}

DLLEXPORT char filePath(char logicPath[folderPoint::logicLayerChar]) {
    switch (logicPath[1]) {
        case 1: {
            folderPoint::concreteTailChar[1] = 'character';
            break;
        }
        case 2: {
            folderPoint::concreteTailChar[1] = 'environment';
            break;
        }
        case 3: {
            folderPoint::concreteTailChar[1] = 'resource';
            break;
        }
    }
    for (int i=0;i < folderPoint::logicLayer;i++) {
        folderPoint::concreteTail += "\\" + folderPoint::concreteTailChar[i];
    }
    folderPoint::concretePath = folderPoint::concreteTop + "\\" + folderPoint::concreteTail;
    return folderPoint::concretePath;
}