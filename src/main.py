#!/usr/bin/env python3
#pylint: skip-file


from init.__init__ import bot_init
import commands.cmd as cmd
import hikari as hk
import lightbulb


def runbot():
    bot = bot_init()

    @bot.listen(hk.StartedEvent)
    async def on_started(event):
        print("Bot has started !")



#######################################################################
############################ COMMANDS #################################
#######################################################################

    # Group: server

    @bot.command
    @lightbulb.command('server', 'Server Group')
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def servgroup(ctx):
        pass

    @servgroup.child
    @lightbulb.command('start', 'Start the server')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def start(ctx):
        return 0

    @servgroup.child
    @lightbulb.command('stop', 'Stop the server')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def stop(ctx):
        return 0

    @servgroup.child
    @lightbulb.command('restart', 'Restart the server')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def restart(ctx):
        return 0

    @servgroup.child
    @lightbulb.command('status', 'Get the server status')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def status(ctx):
        return 0

    @servgroup.child
    @lightbulb.command('stats', 'Get the server statistic')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def stats(ctx):
        return 0
    
    @servgroup.child
    @lightbulb.command('ram', 'Get the server ram usage')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def ram(ctx):
        return 0
    
    @servgroup.child
    @lightbulb.command('cpu', 'Get the server cpu usage')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def cpu(ctx):
        return 0
    
    @servgroup.child
    @lightbulb.command('disk', 'Get the server disk usage')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def disk(ctx):
        return 0
    
    @servgroup.child
    @lightbulb.command('tps', 'Get the server tps')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def tps(ctx):
        return 0
    
    @servgroup.child
    @lightbulb.command('players', 'Get the server players')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def players(ctx):
        return 0
    
    @servgroup.child
    @lightbulb.command('down', 'Check if the server is down')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def down(ctx):
        return 0
    
    @servgroup.child
    @lightbulb.command('help', 'Get information about the commands')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def help(ctx):
        return 0

    # Group: modpack

    @bot.command
    @lightbulb.command('modpack', 'Modpack Group')
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def modpackgroup(ctx):
        pass

    @modpackgroup.child
    @lightbulb.command('link', 'Get the modpack link')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def link(ctx):
        return 0
    
    @modpackgroup.child
    @lightbulb.command('desc', 'Get the modpack description')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def desc(ctx):
        return 0
    
    @modpackgroup.child
    @lightbulb.command('modlist', 'Get the modpack modlist')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def modlist(ctx):
        return 0
    
    @modpackgroup.child
    @lightbulb.command('install', 'Get the procedure to install the modpack')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def install(ctx):
        return 0
    
    @modpackgroup.child
    @lightbulb.command('help', 'Get information about the commands')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def help(ctx):
        return 0
    
    # Command: staff

    @bot.command
    @lightbulb.command('staff', 'Get a description of the staff')
    async def staff(ctx):
        return 0

    # Group: warn

    @bot.command
    @lightbulb.command('warn', 'Warn Group')
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def warngroup(ctx):
        pass

    @warngroup.child
    @lightbulb.command('add', 'Add a warning to a player')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def add(ctx):
        return 0

    @warngroup.child
    @lightbulb.command('remove', 'Remove a warning to a player')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def remove(ctx):
        return 0

    @warngroup.child
    @lightbulb.command('list', 'Get the list of warnings of a player')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def list(ctx):
        return 0

    @warngroup.child
    @lightbulb.command('clear', 'Clear the warnings of a player')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def clear(ctx):
        return 0

    @warngroup.child
    @lightbulb.command('ban', 'Ban a player')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def ban(ctx):
        return 0

    @warngroup.child
    @lightbulb.command('help', 'Get information about the commands')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def help(ctx):
        return 0

    bot.run()



if __name__ == '__main__':
    runbot()