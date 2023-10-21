import discord
from discord.ext import commands
from discord import app_commands

class Modpack(commands.GroupCog, name = "modpack"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @app_commands.command(name="link", description="Obtenir le lien vers la page CurseForge du modpack")
    async def link(self, interaction: discord.Interaction) -> None:
        link = '[Clique ici pour accéder au modpack du serveur](https://www.curseforge.com/minecraft/modpacks/azazelcompany-modpack)'
        embed = discord.Embed(title="Notification Serveur", description=link, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="desc", description="Obtenir la description du modpack")
    async def desc(self, interaction: discord.Interaction) -> None:
        desc = ''
        embed = discord.Embed(title="Notification Serveur", description=desc, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="install", description="Affiche le guide d'installation du modpack")
    async def install(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="modlist", description="Affiche la liste des mods du modpack")
    async def modlist(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)