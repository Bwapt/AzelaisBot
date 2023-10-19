from typing import Literal, Optional

import discord
from discord.ext import commands
import configparser
import asyncio

from commands.server import Server
from commands.modpack import Modpack
from commands.warn import Warn
from commands.misc import Misc

# CONFIG

config = configparser.ConfigParser()
config.read('src/config/config.ini')

DISCORD_TOKEN = config['TOKEN']['discord_token']

intents = discord.Intents.default()
intents.message_content = True

class AzelaisBot(commands.Bot):
    async def setup_hook(self) -> None:
        await asyncio.gather(bot.add_cog(Server(bot)), bot.add_cog(Modpack(bot)), bot.add_cog(Warn(bot)), bot.add_cog(Misc(bot)))

bot = AzelaisBot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("AzelaisBot has successfuly started !")


@bot.event
async def on_message(message):
    print(f"{message.author} : {message.content}")
    await bot.process_commands(message)

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

# RUN

bot.run(token=DISCORD_TOKEN)