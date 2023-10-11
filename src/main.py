import discord
from discord.ext import commands
import configparser

from commands.server.start import start_server

# CONFIG

config = configparser.ConfigParser()
config.read('src/config/config.ini')

DISCORD_TOKEN = config['TOKEN']['discord_token']
token = config['TOKEN']['minestrator_token']

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

# COMMANDS

@bot.command(name="start")
async def start(ctx):
    print("HHAGHAAHHAHGAHAHGAAHGahgAHGAA")
    response = await start_server(token)
    await ctx.send(response)

# RUN

bot.run(token=DISCORD_TOKEN)