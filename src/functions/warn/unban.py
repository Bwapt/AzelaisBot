import discord
from discord import app_commands

from functions.warn.access_list_files import get_banlist, str_banlist

async def warn_unban(interaction: discord.Interaction, user: str, reason: str):

    userId = user # Weird due to incompat between userId and autocomplete

    banlist = get_banlist()

    try:
        user = await interaction.client.fetch_user(userId)
    except:
        return f"L'utilisateur {user} n'a pas été trouvé."
    
    banlist.pop(str(userId))

    await interaction.guild.unban(user=user, reason=reason)

    str_banlist(banlist)

    return f"{user.global_name} a été débanni pour *{reason}*. On te donne une nouvelle chance. C'est ta dernière."




async def unban_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    user_list = []
    user: discord.User

    banlist = get_banlist()

    for userId in banlist:
        user = await interaction.client.fetch_user(userId)
        user_list.append(user.global_name)

    return [
        app_commands.Choice(name=user, value=userId)
        for user in user_list if current.lower() in user.lower()
    ]