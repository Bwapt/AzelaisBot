class ModHelp:
    def search():
        ret =   ("- /mod search <mod> :\n"
                 "\n"
                 "This command allows the user to search for a mod.\n"
                 "It uses as argument a string called <mod> and provide to the user a list of mods.\n" 
                 "\n"
                 "To get better results, it is highly recommended to search directly with the slug of the mod.\n"
                 "\n"
                 "Example :\n"
                 "\n"
                 "/mod search **create-fabric**\n"
                 "is prefered as\n"
                 "/mod search **Create Fabric**")
 
        return ret 
    
    def url():
        ret =   ("- /mod url <mod> :\n"
                 "\n"
                 "This command return to the user the Modrinth Website URL of the provided mod.\n"
                 "It uses as argument a string called <mod> and provide to the user an URL as a string.\n" 
                 "\n"
                 "To get better results, it is highly recommended to search directly with the slug of the mod.\n"
                 "\n"
                 "Example :\n"
                 "\n"
                 "/mod url **create-fabric**\n"
                 "is prefered as\n"
                 "/mod url **Create Fabric**")
 
        return ret
    
    def lastversion():
        ret =   ("- /mod lastversion <mod> :\n"
                 "\n"
                 "This command return to the user the latest available game version of the provided mod.\n"
                 "It uses as argument a string called <mod> and provide to the user a game version as a string.\n" 
                 "\n"
                 "To get better results, it is highly recommended to search directly with the slug of the mod.\n"
                 "\n"
                 "Example :\n"
                 "\n"
                 "/mod lastversion **create-fabric**\n"
                 "is prefered as\n"
                 "/mod lastversion **Create Fabric**")
 
        return ret
    
    def versionlist():
        ret =   ("- /mod versionlist <mod> :\n"
                 "\n"
                 "This command return to the user a list of every available game version of the provided mod.\n"
                 "It uses as argument a string called <mod> and provide to the user a list of game versions.\n" 
                 "\n"
                 "To get better results, it is highly recommended to search directly with the slug of the mod.\n"
                 "\n"
                 "Example :\n"
                 "\n"
                 "/mod versionlist **create-fabric**\n"
                 "is prefered as\n"
                 "/mod versionlist **Create Fabric**")
 
        return ret
    
    def loader():
        ret =   ("- /mod loader <mod> :\n"
                 "\n"
                 "This command return to the user a list of every available loader for the provided mod.\n"
                 "It uses as argument a string called <mod> and provide to the user a list of loaders.\n" 
                 "\n"
                 "To get better results, it is highly recommended to search directly with the slug of the mod.\n"
                 "\n"
                 "Example :\n"
                 "\n"
                 "/mod loader **create-fabric**\n"
                 "is prefered as\n"
                 "/mod loader **Create Fabric**")
 
        return ret
    
    def listlastversion():
        ret =   ("- /mod listlastversion <file> :\n"
                 "\n"
                 "This command return to the user the latest available game version of a provided list of mods.\n"
                 "It uses as argument a file called <file> and provide to the user a list of game versions.\n" 
                 "\n"
                 "To get better results, it is highly recommended to search directly with the slug of the mod.\n"
                 "\n"
                 "Example :\n"
                 "\n"
                 "**create-fabric**\n"
                 "**immersiveportals**\n"
                 "**xaeros-minimap-fair**\n"
                 "is prefered as\n"
                 "**Create Fabric**\n"
                 "**Immersive Portals**\n"
                 "**Xaeros Minimap Fair**")
 
        return ret

    def desc():
        ret =   ("- /mod desc <mod> :\n"
                 "\n"
                 "This command return to the user a short description of the provided mod.\n"
                 "It uses as argument a string called <mod> and provide to the user a description as a string.\n" 
                 "\n"
                 "To get better results, it is highly recommended to search directly with the slug of the mod.\n"
                 "\n"
                 "Example :\n"
                 "\n"
                 "/mod desc **create-fabric**\n"
                 "is prefered as\n"
                 "/mod desc **Create Fabric**")
 
        return ret
