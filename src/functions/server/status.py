import aiohttp
import json

async def server_status(token, server_code):
    url = f"https://rest.minestrator.com/api/v1/server/ressources/{server_code}"

    headers = {
        "Authorization": f"{token}",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                response = json.loads(await response.text())
                print(response)
                data = response['data'][0]
                if data['status'] == 'on':
                    return "Le serveur est allumé"
                elif data['status'] == 'starting':
                    return "Le serveur est en cours de démarrage"
                else :
                    return "Le serveur est éteint"
            else:
                return "Les informations du serveur n'ont pas pu être récupérées."


