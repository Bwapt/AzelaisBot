import discord
import configparser

config = configparser.ConfigParser()
config.read('src/config.ini')
print(config.sections())
DISCORD_TOKEN = config['TOKEN']

bot = discord.Client()

@bot.event
async def on_ready():
    print("AzelaisBot has successfuly started !")

bot.run(token=DISCORD_TOKEN)