import aiohttp
import json

async def server_start(token, server_code):
    url = "https://rest.minestrator.com/api/v1/server/action"
    data = {
        "hashsupport": f"{server_code}",
        "action": "start"
    }

    headers = {
        "Authorization": f"{token}",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
            if response.status == 200:
                response = json.loads(await response.text())
                print(response)
                if "error" in response:
                    return "Le serveur a eu un problème au démarrage"
                else :
                    return "Démarrage du serveur !"
            else:
                return "Le serveur a eu un problème au démarrage"


