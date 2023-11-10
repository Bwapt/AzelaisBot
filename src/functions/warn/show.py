import discord

from .access_list_files import get_warnlist

def warn_show(user: discord.User):

    warned_users = get_warnlist()

    if user in warned_users:
        ret = f"{user.global_name} a {warned_users[user.id]} avertissements."
    else :
        ret = f"{user.global_name} est sage, il n'a pas d'avertissements."
    
    return ret