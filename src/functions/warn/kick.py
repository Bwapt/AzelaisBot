import discord

async def warn_kick(user: discord.User, reason: str, interaction: discord.Interaction):

    await interaction.guild.kick(user=user, reason=reason)
    
    return f"{user.global_name} a été kick pour *{reason}*. J'espère qu'il apprendra de ses erreurs."