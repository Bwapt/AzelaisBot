import json
import aiohttp
import discord
from twitchAPI import twitch
import configparser

config = configparser.ConfigParser()
config.read('src/config/config.ini')

CLIENT_ID = config['TWITCH']['client_id']
CLIENT_SECRET = config['TWITCH']['client_secret']

async def twitch_add(url: str):

    token = get_token()

    user = url.rsplit('/', 1)[0]
    print(user)

    userID = await get_userID(user=user, token=token)

    return

async def twitch_remove():

    return

async def twitch_list():
    
    return

async def twitch_list():

    return

async def get_userID(user: str, token: str):
    
    url = f'https://api.twitch.tv/helix/users?login={user}'
    ret = None

    headers = {
    'Authorization':f'Bearer {token}',
    'Client-Id':f'{CLIENT_ID}'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers) as response:
            if response.status == 200:
                response_json = await response.json()
                print(response_json)
                userID = response_json['data'][0]['id']
                print(userID)
                ret = userID
            else :
                ret = "Ce compte n'existe pas."

    return ret

async def get_token():

    url = 'https://id.twitch.tv/oauth2/token'
    ret = None

    params = {
        'client_id':CLIENT_ID,
        'client_secret':CLIENT_SECRET,
        'grant_type':'client_credentials'}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=params) as response:
            if response.status == 200:
                response_json = await response.json()
                print(response_json)
                token = response_json['access_token']
                print(token)
                ret = token
            else :
                ret = "Une erreur à eu lieu lors de la récupération du token."

    return ret