import discord

from .access_list_files import get_warnlist

async def warn_list():
    user: discord.User
    ret = ""

    warned_users = get_warnlist()

    for user in warned_users:
        user = discord.Client.fetch_user(user_id=user)
        ret += f"- {user.global_name} = {warned_users[user.id]}"
    
    return ret