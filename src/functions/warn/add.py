import discord

from .access_list_files import get_warnlist, str_warnlist

def warn_add(user: discord.User):
    userId: str = str(user.id)
    
    warned_users = get_warnlist()

    if userId in warned_users:
        warned_users[userId] += 1
    else :
        warned_users[userId] = 1

    str_warnlist(warned_users)

    return f"{user.global_name}, tu n'as pas été sage, je te mets un avertissement. Attention à ton comportement."