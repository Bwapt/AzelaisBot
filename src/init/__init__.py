#!/usr/bin/env python3
#pylint: skip-file

from lightbulb import BotApp
from modrinth import Users
from cursepy import CurseClient
from init.config.tokens import *

def modrinth_init():
    Users.ModrinthUser(USER)
    Users.AuthenticatedUser(token=GIT_TOKEN)

def curseforge_init():
    CurseClient(CF_TOKEN)

def bot_init():
    modrinth_init()
    curseforge_init()
    return BotApp(token=DISCORD_TOKEN, default_enabled_guilds=DISCORD_ID)
