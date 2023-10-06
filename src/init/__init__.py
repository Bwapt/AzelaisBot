#!/usr/bin/env python3
#pylint: skip-file

from lightbulb import BotApp
from init.config.tokens import *

def bot_init():
    return BotApp(token=DISCORD_TOKEN, default_enabled_guilds=DISCORD_ID)
