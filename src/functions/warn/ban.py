import discord

from misc.access_list_files import get_banlist, str_banlist

async def warn_ban(user: discord.User, reason: str, interaction: discord.Interaction):
    userId: int = user.id
    
    banlist = get_banlist()

    banlist[userId] = reason

    await interaction.guild.ban(user=user,reason=reason, delete_message_days=0)

    str_banlist(banlist)

    return f"{user.global_name} a été banni pour : *{reason}*. Au plaisir de ne jamais le revoir."