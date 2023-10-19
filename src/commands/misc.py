import discord
from discord.ext import commands
from discord import app_commands

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="staff")
    async def staff(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")

    @app_commands.command(name="twitch")
    async def twitch(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")

    @app_commands.command(name="help")
    async def help(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message("")
    
    