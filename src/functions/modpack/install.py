import discord


async def modpack_install_launcher_selection(interaction: discord.Interaction):

    embed = discord.Embed(title="Installation du modpack",
                          description="Bienvenue dans l'aide d'installation du Modpack de la AzazelCompany.",  
                          color=0x2ecc71)
    
    embed.add_field(name="Quel launcher souhaitez-vous utiliser ?", 
                    value="""
                        - <:prismlauncher:1185190456393486427> Prism Launcher (recommandé)\n
                        - <:curseforge:1185192542090821713> CurseForge\n
                        - <:grass:1221768262195351562> Sans Launcher""")

    view = Launcher_Selection_Button() 

    await interaction.response.send_message(embed=embed, view=view)


async def modpack_install_prismlaucher(interaction: discord.Interaction, state: int):
    view = Prism_Selection_Button()

    match state:
        case 0:
            embed = discord.Embed(title="Etape 1 : Installation de Prism Launcher", 
                                  description="Dans un premier temps, télécharge et installe Prism Launcher.")
            
            embed.add_field(name="https://prismlauncher.org/download/", 
                            value="Cela te redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")
            
            await interaction.response.send_message(embed=embed, view=view)
        
        case 1:
            embed = discord.Embed(title="Etape 2 :", 
                                  description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="", 
                            value="Cela vous redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url="")
            
            await interaction.response.send_message(embed=embed, view=view)
        
        case 2:
            embed = discord.Embed(title="Etape 3 :", 
                                  description="Prism Launcher est installé ! Tu peux maintenant télécharger le modpack.")
            
            embed.add_field(name="", 
                            value="Cela vous redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url="")
            
            await interaction.response.send_message(embed=embed, view=view)
        
        case 3:
            embed = discord.Embed(title="Etape 4 :", 
                                  description="Une fois le modpack téléchargé, il va falloir l'importer dans Prism Launcher.")
            
            embed.add_field(name="", 
                            value="Cela vous redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url="")
            
            await interaction.response.send_message(embed=embed, view=view)
        
        case 4:
            embed = discord.Embed(title="Etape 5 :", 
                                  description="Prism Launcher est installé et le modpack est importé ! Tu peux maintenant jouer !")
            
            embed.add_field(name="", 
                            value="Cela vous redirigera vers la page de Prism Launcher.")
            
            embed.set_thumbnail(url="")
            
            await interaction.response.send_message(embed=embed, view=view)


async def modpack_install_curseforge(interaction: discord.Interaction, state: int):
    view = CurseForge_Selection_Button()   

    match state:
        case 0:
            embed = discord.Embed(title="Etape 1 : Installation de CurseForge", 
                                  description="Dans un premier temps, télécharge et installe CurseForge.")
            
            embed.add_field(name="https://www.curseforge.com/download/app", 
                            value="Cela te redirigera vers la page de CurseForge.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 1:
            embed = discord.Embed(title="Etape 2 : Installation du Modpack AzazelCompany", 
                                  description="On va maintenant installer le Modpack AzazelCompany.")
            
            embed.add_field(name="Clique sur l'icône Minecraft", 
                            value="Cela va automatiquement t'installer le nécessaire pour jouer à tes instances de Minecraft.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 2:
            embed = discord.Embed(title="Etape 2 : Installation du modpack", 
                                  description="On va maintenant installer le Modpack AzazelCompany.")
            
            embed.add_field(name="'Recherche AzazelCompany' dans la barre de recherche en haut de la page, et clique sur le bouton 'Installer'.", 
                            value="Cela va t'installer une instance du Modpack AzazelCompany.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 3:
            embed = discord.Embed(title="Etape 2 : Installation du modpack",
                                  description="On va maintenant installer le Modpack AzazelCompany.")
            
            embed.add_field(name="Reviens sur la page d'accueil, et clique sur le bouton 'Jouer' de l'instance AzazelCompany.",
                            value="Cela va lancer le jeu avec le Modpack AzazelCompany.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)
        
        case 4:
            embed = discord.Embed(title="Etape 3 : Connexion du compte Mojang/Microsoft",
                                    description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="Clique sur le bouton 'Compte Microsoft' eau centre de la page.",
                            value="Cela va te rediriger vers la page de connexion de ton compte Microsoft.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 5:
            embed = discord.Embed(title="Etape 3 : Connexion du compte Mojang/Microsoft",
                                  description="On va maintenant connecter ton compte Minecraft.")
            
            embed.add_field(name="Connecte-toi avec ton compte Microsoft.",
                            value="Renseigne tes informations de connexion (email/mot de passe) pour pouvoir connecter ton compte Microsoft.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 6:
            embed = discord.Embed(title="Etape 4 : Lancement du jeu",
                                    description="On va maintenant lancer le jeu.")
            
            embed.add_field(name="Clique sur le bouton 'Jouer' en bas de la page.",
                            value="On est à la fin ! Cela va lancer le jeu avec le Modpack AzazelCompany.")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")
            await interaction.response.send_message(embed=embed, view=view)

async def modpack_install_no_launcher(interaction: discord.Interaction, state: int):
    view = NoLauncher_Selection_Button()   

    match state:
        case 0:
            embed = discord.Embed(title="Etape 1 : Installation de Fabric", 
                                  description="Dans un premier temps, téléchargons et installons Fabric.")
            
            embed.add_field(name="",
                            value="")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 1:
            embed = discord.Embed(title="Etape 1 : Installation de Fabric", 
                                  description="Choisis la version 1.15.7 pour la version de Fabric.")
            
            embed.add_field(name="",
                            value="")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 0:
            embed = discord.Embed(title="Etape 2 : Installation du Modpack AzazelCompany", 
                                  description="Dans un premier temps, téléchargons le Modpack AzazelCompany.")
            
            embed.add_field(name="", 
                            value="")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)

        case 1:
            embed = discord.Embed(title="Etape 2 : Installation du Modpack AzazelCompany", 
                                  description="Ensuite, essayon d'accéder à ton dossier .minecraft.")
            
            embed.add_field(name="Appuie sur les touches 'Windows + R', tape '%appdata%' et Valide.", 
                            value="")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)
        
        case 2:
            embed = discord.Embed(title="Etape 2 : Installation du Modpack AzazelCompany", 
                                  description="Maintenant, déplaçons le Modpack AzazelCompany dans le dossier .minecraft.")
            
            embed.add_field(name="Va dans le dossier .minecraft, déplace ton dossier mods.zip dedans et dezip-le, un dossier mods devrait apparaître. N'oubli pas de supprimer le dossier mods.zip !", 
                            value="")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

            await interaction.response.send_message(embed=embed, view=view)
        
        case 3:
            embed = discord.Embed(title="Etape 2 : Installation du Modpack AzazelCompany", 
                                  description="Si tout s'est bien déroulé, tu peux maintenant lancer le jeu !")
            
            embed.add_field(name="Ferme ta fenêtre .minecraft, et lance Minecraft !", 
                            value="")
            
            embed.set_thumbnail(url="")

            embed.set_image(url="")

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
    
    @discord.ui.button(emoji="<:grass:1221768262195351562>", label="Sans Launcher", style=discord.ButtonStyle.blurple)
    async def no_launcher(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        await modpack_install_no_launcher(interaction=interaction, state=0)
        


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

class NoLauncher_Selection_Button(discord.ui.View):

    state = 0

    def __init__(self):
        super().__init__()
        self.state
    
    @discord.ui.button(label="Continuer", style=discord.ButtonStyle.success)
    async def continuer(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        NoLauncher_Selection_Button.state += 1

        await modpack_install_no_launcher(interaction=interaction, state=self.state)
    
    @discord.ui.button(label="Demander de l'aide", style=discord.ButtonStyle.secondary)
    async def aide(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message("Hey <@405746739199344670> ! On a besoin de toi ici !")
    
    @discord.ui.button(label="Annuler", style=discord.ButtonStyle.danger)
    async def annuler(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.message.delete()

        NoLauncher_Selection_Button.state = 0

        embed = discord.Embed(title="Annulation de la procédure", description="On espère avoir pu t'aider !")

        await interaction.response.send_message(embed=embed)

