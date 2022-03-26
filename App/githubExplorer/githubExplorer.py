import requests

class Repositoriy:
    class Release:
        def __init__(self,structDict):
            self.url = structDict[0]["url"]
            self.id = structDict[0][id]
            self.tagName = structDict["tag_name"]
            self.assets_name = structDict["assets"][0]["name"]
            '''
            StructDict example:
            {
            "url": "https://api.github.com/repos/LiteLDev/LiteLoaderBDS/releases/60800270",#line
            "assets_url": "https://api.github.com/repos/LiteLDev/LiteLoaderBDS/releases/60800270/assets",
            "upload_url": "https://uploads.github.com/repos/LiteLDev/LiteLoaderBDS/releases/60800270/assets{?name,label}",
            "html_url": "https://github.com/LiteLDev/LiteLoaderBDS/releases/tag/2.1.3",
            "id": 60800270,#line
            "author": {
              "login": "github-actions[bot]",
              "id": 41898282,
              "node_id": "MDM6Qm90NDE4OTgyODI=",
              "avatar_url": "https://avatars.githubusercontent.com/in/15368?v=4",
              "gravatar_id": "",
              "url": "https://api.github.com/users/github-actions%5Bbot%5D",
              "html_url": "https://github.com/apps/github-actions",
              "followers_url": "https://api.github.com/users/github-actions%5Bbot%5D/followers",
              "following_url": "https://api.github.com/users/github-actions%5Bbot%5D/following{/other_user}",
              "gists_url": "https://api.github.com/users/github-actions%5Bbot%5D/gists{/gist_id}",
              "starred_url": "https://api.github.com/users/github-actions%5Bbot%5D/starred{/owner}{/repo}",
              "subscriptions_url": "https://api.github.com/users/github-actions%5Bbot%5D/subscriptions",
              "organizations_url": "https://api.github.com/users/github-actions%5Bbot%5D/orgs",
              "repos_url": "https://api.github.com/users/github-actions%5Bbot%5D/repos",
              "events_url": "https://api.github.com/users/github-actions%5Bbot%5D/events{/privacy}",
              "received_events_url": "https://api.github.com/users/github-actions%5Bbot%5D/received_events",
              "type": "Bot",
              "site_admin": false
            },
            "node_id": "RE_kwDOE-B7kM4Dn70O",
            "tag_name": "2.1.3",#line
            "target_commitish": "main",
            "name": " LiteLoaderBDS 2.1.3 - BugFix version",
            "draft": false,
            "prerelease": false,
            "created_at": "2022-03-02T13:30:59Z",
            "published_at": "2022-03-02T13:44:58Z",
            "assets": [
              {
                "url": "https://api.github.com/repos/LiteLDev/LiteLoaderBDS/releases/assets/58337948",
                "id": 58337948,
                "node_id": "RA_kwDOE-B7kM4Deiqc",
                "name": "LiteLoader-2.1.3.zip",#line
                "label": "",
                "uploader": {
                  "login": "github-actions[bot]",
                  "id": 41898282,
                  "node_id": "MDM6Qm90NDE4OTgyODI=",
                  "avatar_url": "https://avatars.githubusercontent.com/in/15368?v=4",
                  "gravatar_id": "",
                  "url": "https://api.github.com/users/github-actions%5Bbot%5D",
                  "html_url": "https://github.com/apps/github-actions",
                  "followers_url": "https://api.github.com/users/github-actions%5Bbot%5D/followers",
                  "following_url": "https://api.github.com/users/github-actions%5Bbot%5D/following{/other_user}",
                  "gists_url": "https://api.github.com/users/github-actions%5Bbot%5D/gists{/gist_id}",
                  "starred_url": "https://api.github.com/users/github-actions%5Bbot%5D/starred{/owner}{/repo}",
                  "subscriptions_url": "https://api.github.com/users/github-actions%5Bbot%5D/subscriptions",
                  "organizations_url": "https://api.github.com/users/github-actions%5Bbot%5D/orgs",
                  "repos_url": "https://api.github.com/users/github-actions%5Bbot%5D/repos",
                  "events_url": "https://api.github.com/users/github-actions%5Bbot%5D/events{/privacy}",
                  "received_events_url": "https://api.github.com/users/github-actions%5Bbot%5D/received_events",
                  "type": "Bot",
                  "site_admin": false
                },
                "content_type": "application/zip",
                "state": "uploaded",
                "size": 17912917,
                "download_count": 1203,
                "created_at": "2022-03-02T13:44:59Z",
                "updated_at": "2022-03-02T13:45:01Z",
                "browser_download_url": "https://github.com/LiteLDev/LiteLoaderBDS/releases/download/2.1.3/LiteLoader-2.1.3.zip"
              },
              {
                "url": "https://api.github.com/repos/LiteLDev/LiteLoaderBDS/releases/assets/58337947",
                "id": 58337947,
                "node_id": "RA_kwDOE-B7kM4Deiqb",
                "name": "PDB.zip",
                "label": "",
                "uploader": {
                  "login": "github-actions[bot]",
                  "id": 41898282,
                  "node_id": "MDM6Qm90NDE4OTgyODI=",
                  "avatar_url": "https://avatars.githubusercontent.com/in/15368?v=4",
                  "gravatar_id": "",
                  "url": "https://api.github.com/users/github-actions%5Bbot%5D",
                  "html_url": "https://github.com/apps/github-actions",
                  "followers_url": "https://api.github.com/users/github-actions%5Bbot%5D/followers",
                  "following_url": "https://api.github.com/users/github-actions%5Bbot%5D/following{/other_user}",
                  "gists_url": "https://api.github.com/users/github-actions%5Bbot%5D/gists{/gist_id}",
                  "starred_url": "https://api.github.com/users/github-actions%5Bbot%5D/starred{/owner}{/repo}",
                  "subscriptions_url": "https://api.github.com/users/github-actions%5Bbot%5D/subscriptions",
                  "organizations_url": "https://api.github.com/users/github-actions%5Bbot%5D/orgs",
                  "repos_url": "https://api.github.com/users/github-actions%5Bbot%5D/repos",
                  "events_url": "https://api.github.com/users/github-actions%5Bbot%5D/events{/privacy}",
                  "received_events_url": "https://api.github.com/users/github-actions%5Bbot%5D/received_events",
                  "type": "Bot",
                  "site_admin": false
                },
                "content_type": "application/zip",
                "state": "uploaded",
                "size": 27020567,
                "download_count": 103,
                "created_at": "2022-03-02T13:44:59Z",
                "updated_at": "2022-03-02T13:45:01Z",
                "browser_download_url": "https://github.com/LiteLDev/LiteLoaderBDS/releases/download/2.1.3/PDB.zip"
              }
            ],
            "tarball_url": "https://api.github.com/repos/LiteLDev/LiteLoaderBDS/tarball/2.1.3",
            "zipball_url": "https://api.github.com/repos/LiteLDev/LiteLoaderBDS/zipball/2.1.3",
            "body": "This is a bug fix update, fix several problems that may cause crash. Please update as soon as possible\r\n## [New features]\r\n- New dynamic command registration interface (DynamicCommandAPI)\r\n- New text encoding conversion interface (I18nAPI)\r\n- Added built-in OutputFilter regex output filtering function\r\n- Added addons automatic installation, management and query commands\r\n- Added CompoundTag::toPrettySNBT beautification output interface\r\n- Provided support for NetworkNBT format\r\n- Provide comment support for all json interfaces of scripting engine\r\n- Added a symbol cache switch for PrintCurrentStackTraceback\r\n- Upgraded the included LLMoney version\r\n## [Bug fixes]\r\n- Repair the problem of incorrect content of some packet classes\r\n- Repair the problems of StructureTemplate class.\r\n- Repair the problem of error reporting in hot management command\r\n- Add lock to Logger to solve the problem of probable collapse of service when multi-threaded output\r\n- The script engine fixes the problem that the database cannot be closed.\r\n- Scripting engine fixes the problem of repeated loading of ll.require\r\n- Scripting engine fixes the problem that some object data is not updated after setNbt\r\n- Scripting engine fixes missing onLiquidFlow event dimension\r\n- Scripting engine fixes item.clone\r\n- Scripting engine provides binary interface for base64 conversion\r\n- Scripting engine fixes possible problems with TimeTask, adds security checks\r\n- Scripting engine adds engine validity checks for multiple callbacks, improving stability\r\n- Scripting engine fixes the problem that V8 output abnormal information triggers debugger and causes crash.\r\n- Fix some problems of SymDBHelper in SDK.\r\n- Provide UTF8 conversion for most of the output, to avoid the crash caused by local encoding\r\n- Repair the problem of crashing caused by inputting full-angle characters in the background",
            "reactions": {
              "url": "https://api.github.com/repos/LiteLDev/LiteLoaderBDS/releases/60800270/reactions",
              "total_count": 2,
              "+1": 2,
              "-1": 0,
              "laugh": 0,
              "hooray": 0,
              "confused": 0,
              "heart": 0,
              "rocket": 0,
              "eyes": 0
            }
          }
            '''
    def __init__(self,name):
        self.name = name

    def GetReleases_latest(self):
        releaseLatest_data = requests.get("https://api.github.com/repos/" + self.name + "/releases/latest")
        releaseLatest = self.Release(releaseLatest_data.json())
        return "https://github.com/" + self.name + "releases/download/" + releaseLatest.tagName + "/" + releaseLatest.assets_name