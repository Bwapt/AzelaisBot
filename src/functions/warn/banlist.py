import discord

from .access_list_files import get_banlist

async def warn_banlist(interaction: discord.Interaction):
    ret = ""

    banned_users = get_banlist()

    #user = await interaction.client.fetch_user(405746739199344670)

    for userId in banned_users.keys():
        user = await interaction.client.fetch_user(405746739199344670)
        ret += f"- {user.global_name} = {banned_users[user.id]}"
    
    return ret