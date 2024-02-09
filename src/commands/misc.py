import discord
from discord.ext import commands
from discord import app_commands

import asyncio

from functions.misc.help import *
from functions.misc.twitch import *

from misc.permissions import * 

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    

    ######## TWITCH ########

    twitch_group = app_commands.Group(name="twitch", description="Commandes basiques concernant Twitch")

    @is_bwapt()
    @twitch_group.command(name="add", description="Ajoute un Streamer")
    async def add(self, interaction: discord.Interaction, url: str) -> None:
        
        await interaction.response.defer()
        add = await twitch_add(url=url)

        await interaction.followup.send(content=add)
    
    @is_bwapt()
    @twitch_group.command(name="remove", description="Retire un Streamer")
    async def remove(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("")
    
    @is_bwapt()
    @twitch_group.command(name="list", description="Affiche la liste des Streamers")
    async def list(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")
    
    @is_bwapt()
    @twitch_group.command(name="notifications", description="Active ou désactive les notifications pour un membre")
    async def notifications(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")
    

    ######## YOUTUBE ########

    youtube_group = app_commands.Group(name="youtube", description="Commandes basiques concernant Youtube")

    @is_bwapt()
    @youtube_group.command(name="add", description="Donne le lien vers la chaîne YouTube d'un membre")
    async def add(self, interaction: discord.Interaction) -> None:
        
        await interaction.response.send_message("")
    
    @is_bwapt()
    @youtube_group.command(name="remove", description="Donne le lien vers la chaîne YouTube d'un membre")
    async def remove(self, interaction: discord.Interaction) -> None:
        
        await interaction.response.send_message("")
    
    @is_bwapt()
    @youtube_group.command(name="list", description="Donne le lien vers la chaîne YouTube d'un membre")
    async def list(self, interaction: discord.Interaction) -> None:
        
        await interaction.response.send_message("")
    
    @is_bwapt()
    @youtube_group.command(name="notifications", description="Donne le lien vers la chaîne YouTube d'un membre")
    async def notifications(self, interaction: discord.Interaction) -> None:
        
        await interaction.response.send_message("")


    ######## STAFF ########

    @is_bwapt()
    @app_commands.command(name="staff", description="Donne une description d'un membre du staff")
    async def staff(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")
    

    ######## HELP ########

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
        

    
    