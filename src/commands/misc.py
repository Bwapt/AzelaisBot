import discord
from discord.ext import commands
from discord import app_commands

import asyncio

from functions.misc.help import *

from misc.permissions import * 

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @is_bwapt()
    @app_commands.command(name="staff", description="Donne une description d'un membre du staff")
    async def staff(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")

    @is_bwapt()
    @app_commands.command(name="twitch", description="Donne le lien vers la chaîne Twitch d'un membre")
    async def twitch(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")

    @is_bwapt()
    @app_commands.command(name="youtube", description="Donne le lien vers la chaîne YouTube d'un membre")
    async def youtube(self, interaction: discord.Interaction) -> None:
        
        await interaction.response.send_message("")
    
    @is_bwapt()
    @app_commands.command(name="help", description="Affiche la liste des commandes")
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title="Notification Serveur", description=command_groups, color=0x5dade2)
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()
        asyncio.gather(
            message.add_reaction("1️⃣"),
            message.add_reaction("2️⃣"),
            message.add_reaction("3️⃣"),
            message.add_reaction("4️⃣")
        )
        

    
    