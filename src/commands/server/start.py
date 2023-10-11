import aiohttp

async def start_server(token):
    url = "https://rest.minestrator.com/api/v1/server/action"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "action": "start"
    }

    async with aiohttp.ClientSession as session:
        async with session.post(url, headers, params) as response:
            if response.status == 200:
                return "Le serveur a démarré !"
            else:
                return "Le serveur a eu un problème au démarrage"


