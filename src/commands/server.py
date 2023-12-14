import discord
from discord.ext import commands
from discord import app_commands
import configparser


from functions.server.start import server_start
from functions.server.stop import server_stop
from functions.server.restart import server_restart
from functions.server.status import server_status
from functions.server.ram import server_ram
from functions.server.cpu import server_cpu
from functions.server.disk import server_disk
from functions.server.players import server_players

from misc.permissions import *

config = configparser.ConfigParser()
config.read('src/config/config.ini')

MINESTRATOR_TOKEN = config['TOKEN']['minestrator_token']
SERVER_CODE = config['CODE_SUPPORT']['server_code']

class Server(commands.GroupCog, name = "server"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @is_bwapt()
    @app_commands.command(name="start", description="Démarrer le serveur")
    async def start(self, interaction: discord.Interaction) -> None:
        response = await server_start(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Démarrage du serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="stop", description="Arrêter le serveur")
    async def stop(self, interaction: discord.Interaction) -> None:
        response = await server_stop(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Arrêt du serveur", description=response, color=0xff0000)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="restart", description="Redémarrer le serveur")
    async def restart(self, interaction: discord.Interaction) -> None:
        response = await server_restart(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Redémarrage du serveur", description=response, color=0xf1c40f)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="status", description="Voir le status du serveur")
    async def status(self, interaction: discord.Interaction) -> None:
        response = await server_status(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Status du serveur", description=response, color=0x5dade2)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="ram", description="Voir l'utilisation de la RAM")
    async def ram(self, interaction: discord.Interaction) -> None:
        response = await server_ram(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Utilisation de la RAM", description=response, color=0x5dade2)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="cpu", description="Voir l'utilisation du CPU")
    async def cpu(self, interaction: discord.Interaction) -> None:
        response = await server_cpu(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Utilisation du CPU", description=response, color=0x5dade2)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="disk", description="Voir l'utilisation du disque dur")
    async def disk(self, interaction: discord.Interaction) -> None:
        response = await server_disk(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Utilisation du Disque", description=response, color=0x5dade2)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="players", description="Voir les joueurs connectés")
    async def players(self, interaction: discord.Interaction) -> None:
        response = await server_players(MINESTRATOR_TOKEN, SERVER_CODE)
        embed = discord.Embed(title="Nombre de joueurs connectés", description=response, color=0x5dade2)
        await interaction.response.send_message(embed=embed)
