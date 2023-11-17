import discord

from .access_list_files import get_warnlist

async def warn_list(interaction: discord.Interaction):
    user: discord.User
    ret = ""

    warned_users = get_warnlist()

    for user in warned_users:
        user = interaction.client.get_user(user)
        ret += f"- {user.global_name} = {warned_users[user.id]}"
    
    return ret