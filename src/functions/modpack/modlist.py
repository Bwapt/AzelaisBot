import aiohttp
import json

async def modpack_modlist(modpackId: str):
    url = f"https://www.modpackindex.com/api/v1/modpack/{modpackId}/mods"
    modlist = {}
    ret = ""

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                response = json.loads(await response.text())
                data = response['data']

                for mods in data:
                    modlist[mods['name']] = mods['url']
    
    modlist = dict(sorted(modlist.items()))
    
    for mod in modlist.keys():
        ret += f"- [{mod}]({modlist[mod]})\n"
        
    return ret