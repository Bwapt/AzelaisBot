import aiohttp
import json

async def modpack_link(modpackId: str):
    url = f"https://www.modpackindex.com/api/v1/modpack/{modpackId}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                response = json.loads(await response.text())
                link = response['data']['url']
                
    return link