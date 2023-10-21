import discord
from discord.ext import commands
from discord import app_commands

from functions.misc.help import command_groups
from functions.misc.help import server_commands
from functions.misc.help import modpack_commands
from functions.misc.help import warn_commands
from functions.misc.help import misc_commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="staff", description="Donne une description d'un membre du staff")
    async def staff(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")

    @app_commands.command(name="twitch", description="Donne le lien vers la chaîne Twitch d'un membre")
    async def twitch(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")

    @app_commands.command(name="youtube", description="Donne le lien vers la chaîne YouTube d'un membre")
    async def youtube(self, interaction: discord.Interaction) -> None:
        
        await interaction.response.send_message("")
    
    @app_commands.command(name="help", description="Affiche la liste des commandes")
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title="Notification Serveur", description=command_groups, color=0x5dade2)
        await interaction.response.send_message("")

    
    