import discord

from functions.warn.access_list_files import get_banlist, str_banlist

async def warn_unban(user: discord.User, reason: str, interaction: discord.Interaction):
    userId: int = str(user.id)

    banlist = get_banlist()

    banlist.pop(userId)

    await interaction.guild.unban(user=user, reason=reason)

    str_banlist(banlist)

    return f"{user.global_name} a été débanni pour *{reason}*. On te donne une nouvelle chance. C'est ta dernière."