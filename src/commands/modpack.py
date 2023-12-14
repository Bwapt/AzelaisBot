import discord
from discord.ext import commands
from discord import app_commands
import configparser

from functions.modpack.desc import modpack_desc
from functions.modpack.link import modpack_link
from functions.modpack.modlist import modpack_modlist

from misc.permissions import *

config = configparser.ConfigParser()
config.read('src/config/config.ini')

MODPACK_ID = config['ID']['modpack_id']

class Modpack(commands.GroupCog, name = "modpack"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @is_bwapt()
    @app_commands.command(name="link", description="Obtenir le lien vers la page CurseForge du modpack")
    async def link(self, interaction: discord.Interaction) -> None:
        link = await modpack_link(MODPACK_ID)

        embed = discord.Embed(title="Lien du modpack", description=link, color=0x2ecc71)

        await interaction.response.send_message(embed=embed)
    
    @is_bwapt()
    @app_commands.command(name="desc", description="Obtenir la description du modpack")
    async def desc(self, interaction: discord.Interaction) -> None:
        title, url, thumbnail, desc, authors, versions, categories, last_update = await modpack_desc(MODPACK_ID)

        embed = discord.Embed(title=title, description=desc, url=url, color=0x2ecc71)
        embed.set_thumbnail(url=thumbnail)
        embed.add_field(name="Auteurs", value=authors)
        embed.add_field(name="Versions", value=versions)
        embed.add_field(name="Catégories", value=categories)
        embed.set_footer(text=f"Dernière mise-à-jour : {last_update}")
        embed.set_image(url="https://i.ibb.co/wwrNDXw/IP.webp")

        await interaction.response.send_message(embed=embed)
    
    @is_bwapt()
    @app_commands.command(name="install", description="Affiche le guide d'installation du modpack")
    async def install(self, interaction: discord.Interaction) -> None:
        response = ''

        embed = discord.Embed(title="Installation du modpack", description=response,  color=0x2ecc71)

        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="modlist", description="Affiche la liste des mods du modpack")
    async def modlist(self, interaction: discord.Interaction) -> None:
        modlist = await modpack_modlist(MODPACK_ID)

        embed = discord.Embed(title="Listes des mods du modpack", description=modlist, color=0x2ecc71)

        await interaction.response.send_message(embed=embed)