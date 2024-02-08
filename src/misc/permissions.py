import discord

def is_bwapt():
    def predicate(interaction: discord.Interaction) -> bool:

        return interaction.user.id == 405746739199344670
    
    return discord.app_commands.check(predicate)

# Organisation / Developpeur / Support
def can_manage_server():
    def predicate(interaction: discord.Interaction) -> bool:
        
        return (    interaction.user.get_role(905149886272516137) 
                or  interaction.user.get_role(1131996499648204820) 
                or  interaction.user.get_role(905152238324953098))
    
    return discord.app_commands.check(predicate)