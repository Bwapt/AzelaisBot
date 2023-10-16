import discord
from discord.ext import commands
from discord import app_commands

class Warn(commands.GroupCog, name = "warn"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @app_commands.command(name="add")
    async def add(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="remove")
    async def remove(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="show")
    async def show(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ban")
    async def ban(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="help")
    async def help(self, interaction: discord.Interaction) -> None:
        response = ''
        embed = discord.Embed(title="Notification Serveur", description=response, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)