from typing import Optional
import discord

async def modpack_install_launcher_selection(interaction: discord.Interaction):

    embed = discord.Embed(title="Installation du modpack",
                          description="Bienvenue dans l'aide d'installation du Modpack de la AzazelCompany.",  
                          color=0x2ecc71)
    
    embed.add_field(name="Quel launcher souhaitez-vous utiliser ?", 
                    value="- <:prismlauncher:1185190456393486427> Prism Launcher (recommandé)\n- <:curseforge:1185192542090821713> CurseForge")

    view = Launcher_Selection_Button()

    await interaction.response.send_message(embed=embed, view=view)

async def modpack_install_prismlaucher(interaction: discord.Interaction, state: int):
    thumbnail = "https://i.ibb.co/Rp2CVXH/prismlauncher.png"
    view = Selection_Button()

    match state:
        case 0:
            embed = discord.Embed(title="Etape 1 : Installation de Prism Launcher", 
                                  description="Dans un premier temps, télécharge et installe Prism Launcher.")
            
            embed.add_field(name="https://prismlauncher.org/download/", 
                            value="Cela te redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url=thumbnail)
            
            await interaction.response.send_message(embed=embed, view=view)
        
        case 1:
            embed = discord.Embed(title="Etape 2 : Connexion à ton compte Mojang/Microsoft", 
                                  description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="https://prismlauncher.org/download/", 
                            value="Cela vous redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url=thumbnail)
            
            await interaction.response.send_message(embed=embed, view=view)

async def modpack_install_curseforge(interaction: discord.Interaction, state: int):
    thumbnail = "https://i.ibb.co/Hg7Cb2d/curseforge2.png"
    view = Selection_Button()   

    match state:
        case 0:
            embed = discord.Embed(title="Etape 1 : Installation de CurseForge", 
                                  description="Dans un premier temps, télécharge et installe CurseForge.")
            
            embed.add_field(name="https://www.curseforge.com/download/app", 
                            value="Cela te redirigera vers la page de CurseForge.")
            
            embed.set_thumbnail(url=thumbnail)

            await interaction.response.send_message(embed=embed, view=view)

        case 1:
            embed = discord.Embed(title="Etape 2 : Connecter ton compte Mojang/Microsoft", 
                                  description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="https://www.curseforge.com/download/app", 
                            value="Cela vous redirigera vers la page de CurseForge.")
            
            embed.set_thumbnail(url=thumbnail)

            await interaction.response.send_message(embed=embed, view=view)


class Launcher_Selection_Button(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(emoji="<:prismlauncher:1185190456393486427>", label="Prism Launcher", style=discord.ButtonStyle.blurple)
    async def prism_launcher(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        await modpack_install_prismlaucher(interaction=interaction, state=0)

    @discord.ui.button(emoji="<:curseforge:1185192542090821713>", label="CurseForge", style=discord.ButtonStyle.blurple)
    async def curseforge(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        await modpack_install_curseforge(interaction=interaction, state=0)
        


class Selection_Button(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.state = 0
    
    @discord.ui.button(label="Continuer", style=discord.ButtonStyle.success)
    async def continuer(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        self.state += 1

        await modpack_install_prismlaucher(interaction=interaction, state=self.state)
    
    @discord.ui.button(label="Demander de l'aide", style=discord.ButtonStyle.secondary)
    async def aide(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message("Hey <@405746739199344670> ! On a besoin de toi ici !")
    
    @discord.ui.button(label="Annuler", style=discord.ButtonStyle.danger)
    async def annuler(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        self.state = 0

        embed = discord.Embed(title="Annulation de la procédure", description="On espère avoir pu t'aider !")

        await interaction.response.send_message(embed=embed)