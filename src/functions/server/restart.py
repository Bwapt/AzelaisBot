import aiohttp
import json

async def server_restart(token, server_code):
    url = "https://rest.minestrator.com/api/v1/server/action"
    data = {
        "hashsupport": f"{server_code}",
        "action": "restart"
    }

    headers = {
        "Authorization": f"{token}",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
            if response.status == 200:
                response = json.loads(await response.text())
                print(response)
                if 'logged' == False in response or "error" in response:
                    return "Le serveur a eu un problème au redémarrage"
                else :
                    return "Le serveur redémarre !"
            else:
                return "Le serveur a eu un problème au redémarrage"


