import discord

from .access_list_files import get_banlist

async def warn_banlist():
    user: discord.User
    ret = ""

    banned_users = get_banlist()

    for user in banned_users:
        user = await discord.Client.fetch_user(user_id=user)
        ret += f"- {user.global_name} = {banned_users[user.id]}"
    
    return ret