import githubExplorer
import urllib
import re

def DownloadExpressHost_LiteLoaderBDS(version="latest"):
    if (version == "latest"):
        LiteLoaderBDS = githubExplorer.Repositoriy("LiteLDev/LiteLoaderBDS")
        urllib.urlretrieve(LiteLoaderBDS.GetReleases_latest, "a3b1c-liteLoaderBDS-latest")#TODO:value<a3b1c-liteLoaderBDS-latest> => Must work as a logicPath.
    else:
        pass

'''
str(response.json()["assets"]["name"])
def GetExpressHost_BedrockDedicatedSever_lastVersion():
    website = requests.get("https://www.minecraft.net/en-us/download/server/bedrock")
    print(website.text)
    #print(re.match("http.*?\\.zip",website.text))
    
def GetExpressHost_BedrockDedicatedServer(version):
https://minecraft.azureedge.net/bin-win/bedrock-server-1.18.12.01.zip
    

'''
DownloadExpressHost_LiteLoaderBDS()
#https://github.com/LiteLDev/LiteLoaderBDS/releases/download/2.1.3/LiteLoader-2.1.3.zip