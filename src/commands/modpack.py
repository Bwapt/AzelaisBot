import discord
from discord.ext import commands
from discord import app_commands

class Modpack(commands.GroupCog, name = "modpack"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @app_commands.command(name="link")
    async def link(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="desc")
    async def desc(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="install")
    async def install(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="modlist")
    async def modlist(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="help")
    async def help(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)