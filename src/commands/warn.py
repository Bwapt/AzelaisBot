import discord
from discord.ext import commands
from discord import app_commands

from functions.warn.add import warn_add
from functions.warn.banlist import warn_banlist
from functions.warn.remove import warn_remove
from functions.warn.show import warn_show
from functions.warn.list import warn_list
from functions.warn.ban import warn_ban
from functions.warn.kick import warn_kick
from functions.warn.unban import warn_unban, unban_autocomplete

from misc.permissions import *

class Warn(commands.GroupCog, name = "warn"):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    @is_bwapt()
    @app_commands.command(name="add", description="Ajouter un avertissement à un membre")
    async def add(self, interaction: discord.Interaction, user: discord.User) -> None:
        add = warn_add(user=user)
        embed = discord.Embed(title="Ajout d'un avertissement", description=add, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @is_bwapt()
    @app_commands.command(name="remove", description="Retirer un avertissement à un membre")
    async def remove(self, interaction: discord.Interaction, user: discord.User) -> None:
        remove = warn_remove(user=user)
        embed = discord.Embed(title="Retrait d'un avertissement", description=remove, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @is_bwapt()
    @app_commands.command(name="show", description="Afficher les avertissements d'un membre")
    async def show(self, interaction: discord.Interaction, user: discord.User) -> None:
        show = warn_show(user=user)
        embed = discord.Embed(title="Affichage des avertissements d'un membre", description=show, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @is_bwapt()
    @app_commands.command(name="list", description="Afficher la liste des avertissements")
    async def list(self, interaction: discord.Interaction) -> None:
        list = await warn_list(interaction=interaction)
        embed = discord.Embed(title="Affichage de la liste des avertissements", description=list, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    @is_bwapt()
    @app_commands.command(name="banlist", description="Afficher la liste des avertissements")
    async def banlist(self, interaction: discord.Interaction) -> None:
        list = await warn_banlist(interaction=interaction)
        embed = discord.Embed(title="Affichage de la liste des membres bannis", description=list, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="ban", description="Bannir un membre")
    async def ban(self, interaction: discord.Interaction, user: discord.User, reason: str) -> None:
        ban = await warn_ban(user=user, reason=reason, interaction=interaction)
        embed = discord.Embed(title="Bannissement d'un membre", description=ban, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="unban", description="Unbannir un membre")
    @app_commands.autocomplete(user=unban_autocomplete)
    async def unban(self, interaction: discord.Interaction, user: str, reason: str) -> None:
        unban = await warn_unban(user=user, reason=reason, interaction=interaction)
        embed = discord.Embed(title="Notification Serveur", description=unban, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)

    @is_bwapt()
    @app_commands.command(name="kick", description="Kick un membre")
    async def kick(self, interaction: discord.Interaction, user: discord.User, reason: str) -> None:
        kick = await warn_kick(user=user, reason=reason, interaction=interaction)
        embed = discord.Embed(title="Expulsion d'un membre", description=kick, color=0x2ecc71)
        await interaction.response.send_message(embed=embed)
    
    
