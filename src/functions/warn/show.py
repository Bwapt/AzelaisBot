import discord

from .access_list_files import get_warnlist

def warn_show(user: discord.User):
    userId : str = str(user.id)

    warned_users = get_warnlist()

    if userId in warned_users:

        ret = f"{user.global_name} a {warned_users[userId]} avertissements."
    else :
        ret = f"{user.global_name} est sage, il n'a pas d'avertissements."

    return ret