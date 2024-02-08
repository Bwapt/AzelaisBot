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
    view = Prism_Selection_Button()

    match state:
        case 0:
            embed = discord.Embed(title="Etape 1 : Installation de Prism Launcher", 
                                  description="Dans un premier temps, télécharge et installe Prism Launcher.")
            
            embed.add_field(name="https://prismlauncher.org/download/", 
                            value="Cela te redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/0YQqY5Q/0-website.png")
            
            await interaction.response.send_message(embed=embed, view=view)
        
        case 1:
            embed = discord.Embed(title="Etape 2 :", 
                                  description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="https://prismlauncher.org/download/", 
                            value="Cela vous redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url=thumbnail)
            
            await interaction.response.send_message(embed=embed, view=view)


async def modpack_install_curseforge(interaction: discord.Interaction, state: int):
    thumbnail = "https://i.ibb.co/Hg7Cb2d/curseforge2.png"
    view = CurseForge_Selection_Button()   

    match state:
        case 0:
            embed = discord.Embed(title="Etape 1 : Installation de CurseForge", 
                                  description="Dans un premier temps, télécharge et installe CurseForge.")
            
            embed.add_field(name="https://www.curseforge.com/download/app", 
                            value="Cela te redirigera vers la page de CurseForge.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/HrMm708/0-website.png")

            await interaction.response.send_message(embed=embed, view=view)

        case 1:
            embed = discord.Embed(title="Etape 2 : Installation du Modpack AzazelCompany", 
                                  description="On va maintenant installer le Modpack AzazelCompany.")
            
            embed.add_field(name="Clique sur l'icône Minecraft", 
                            value="Cela va automatiquement t'installer le nécessaire pour jouer à tes instances de Minecraft.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/zJRwM71/1-launcher.png")

            await interaction.response.send_message(embed=embed, view=view)

        case 2:
            embed = discord.Embed(title="Etape 2 : Installation du modpack", 
                                  description="On va maintenant installer le Modpack AzazelCompany.")
            
            embed.add_field(name="'Recherche AzazelCompany' dans la barre de recherche en haut de la page, et clique sur le bouton 'Installer'.", 
                            value="Cela va t'installer une instance du Modpack AzazelCompany.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/5rNPQDg/2-launcher.png")

            await interaction.response.send_message(embed=embed, view=view)

        case 3:
            embed = discord.Embed(title="Etape 2 : Installation du modpack",
                                  description="On va maintenant installer le Modpack AzazelCompany.")
            
            embed.add_field(name="Reviens sur la page d'accueil, et clique sur le bouton 'Jouer' de l'instance AzazelCompany.",
                            value="Cela va lancer le jeu avec le Modpack AzazelCompany.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/37yHMh0/3-launcher.png")

            await interaction.response.send_message(embed=embed, view=view)
        
        case 4:
            embed = discord.Embed(title="Etape 3 : Connexion du compte Mojang/Microsoft",
                                    description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="Clique sur le bouton 'Compte Microsoft' eau centre de la page.",
                            value="Cela va te rediriger vers la page de connexion de ton compte Microsoft.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/TTFTkff/4-launcher.png")

            await interaction.response.send_message(embed=embed, view=view)

        case 5:
            embed = discord.Embed(title="Etape 3 : Connexion du compte Mojang/Microsoft",
                                  description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="Connecte-toi avec ton compte Microsoft.",
                            value="Renseigne tes informations de connexion (email/mot de passe) pour pouvoir connecter ton compte Microsoft.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/JrhQYzg/5-launcher.png")

            await interaction.response.send_message(embed=embed, view=view)

        case 6:
            embed = discord.Embed(title="Etape 4 : Lancement du jeu",
                                    description="On va maintenant lancer le jeu.")
            
            embed.add_field(name="Clique sur le bouton 'Jouer' en bas de la page.",
                            value="On est à la fin ! Cela va lancer le jeu avec le Modpack AzazelCompany.")
            
            embed.set_thumbnail(url=thumbnail)

            embed.set_image(url="https://i.ibb.co/fk2J5LL/6-launcher.png")

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
        


class Prism_Selection_Button(discord.ui.View):

    state = 0

    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label="Continuer", style=discord.ButtonStyle.success)
    async def continuer(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        Prism_Selection_Button.state += 1

        await modpack_install_prismlaucher(interaction=interaction, state=self.state)
    
    @discord.ui.button(label="Demander de l'aide", style=discord.ButtonStyle.secondary)
    async def aide(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message("Hey <@405746739199344670> ! On a besoin de toi ici !")
    
    @discord.ui.button(label="Annuler", style=discord.ButtonStyle.danger)
    async def annuler(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        Prism_Selection_Button.state = 0

        embed = discord.Embed(title="Annulation de la procédure", description="On espère avoir pu t'aider !")

        await interaction.response.send_message(embed=embed)


class CurseForge_Selection_Button(discord.ui.View):

    state = 0

    def __init__(self):
        super().__init__()
        self.state
    
    @discord.ui.button(label="Continuer", style=discord.ButtonStyle.success)
    async def continuer(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        CurseForge_Selection_Button.state += 1

        await modpack_install_curseforge(interaction=interaction, state=self.state)
    
    @discord.ui.button(label="Demander de l'aide", style=discord.ButtonStyle.secondary)
    async def aide(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message("Hey <@405746739199344670> ! On a besoin de toi ici !")
    
    @discord.ui.button(label="Annuler", style=discord.ButtonStyle.danger)
    async def annuler(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        CurseForge_Selection_Button.state = 0

        embed = discord.Embed(title="Annulation de la procédure", description="On espère avoir pu t'aider !")

        await interaction.response.send_message(embed=embed)