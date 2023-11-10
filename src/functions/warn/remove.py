import discord

from .access_list_files import get_warnlist, str_warnlist

def warn_remove(user: discord.User):
    userId: int = user.id

    warned_users = get_warnlist()

    if userId in warned_users:
        warned_users[userId] -= 1
        if warned_users[userId] == 0:
            warned_users.pop(userId)
        ret = f"{user.global_name} a été sage, un avertissement a été retiré."
    else :
        ret = f"{user.global_name} est sage au quotidien, il n'a pas d'avertissements à retirer."

    str_warnlist()

    return ret