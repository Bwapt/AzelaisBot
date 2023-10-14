import discord
from discord.ext import commands
import configparser

from commands.server.start import server_start
from commands.server.stop import server_stop
from commands.server.restart import server_restart
from commands.server.status import server_status
from commands.server.ram import server_ram
from commands.server.cpu import server_cpu
from commands.server.disk import server_disk
from commands.server.players import server_players

# CONFIG

config = configparser.ConfigParser()
config.read('src/config/config.ini')

DISCORD_TOKEN = config['TOKEN']['discord_token']
MINESTRATOR_TOKEN = config['TOKEN']['minestrator_token']
SERVER_CODE = config['CODE_SUPPORT']['server_code']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("AzelaisBot has successfuly started !")

@bot.event
async def on_message(message):
    print(f"{message.author} : {message.content}")
    await bot.process_commands(message)

# SERVER

@bot.command(name="start")
async def start(ctx):
    response = await server_start(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

@bot.command(name="stop")
async def stop(ctx):
    response = await server_stop(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

@bot.command(name="restart")
async def restart(ctx):
    response = await server_restart(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

@bot.command(name="status")
async def status(ctx):
    response = await server_status(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

@bot.command(name="ram")
async def ram(ctx):
    response = await server_ram(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

@bot.command(name="cpu")
async def cpu(ctx):
    response = await server_cpu(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

@bot.command(name="disk")
async def disk(ctx):
    response = await server_disk(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

@bot.command(name="players")
async def players(ctx):
    response = await server_players(MINESTRATOR_TOKEN, SERVER_CODE)
    await ctx.send(response)

# MODPACK

# WARN

# MISC

# RUN

bot.run(token=DISCORD_TOKEN)