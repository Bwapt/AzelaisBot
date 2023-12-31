import discord

from misc.access_list_files import get_warnlist

async def warn_list(interaction: discord.Interaction):
    user: discord.User
    ret = ""

    warned_users = get_warnlist()

    if warned_users:
        for userId in warned_users:

            user = await interaction.client.fetch_user(userId)

            ret += f"- {user.global_name} = {warned_users[str(user.id)]}"
    else:
        ret = "Tout le monde est sage. Personne n'a d'avertissements."
        
    return ret