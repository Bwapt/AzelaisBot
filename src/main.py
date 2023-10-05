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

    @servgroup.child
    @lightbulb.command('stop', 'Stop the server')

    @servgroup.child
    @lightbulb.command('restart', 'Restart the server')

    @servgroup.child
    @lightbulb.command('status', 'Get the server status')

    @servgroup.child
    @lightbulb.command('statistic', 'Get the server statistic')

    @servgroup.child
    @lightbulb.command('ram', 'Get the server ram usage')

    @servgroup.child
    @lightbulb.command('cpu', 'Get the server cpu usage')

    @servgroup.child
    @lightbulb.command('disk', 'Get the server disk usage')

    @servgroup.child
    @lightbulb.command('tps', 'Get the server tps')

    @servgroup.child
    @lightbulb.command('players', 'Get the server players')

    @servgroup.child
    @lightbulb.command('down', 'Check if the server is down')

    @servgroup.child
    @lightbulb.command('help', 'Get information about the commands')


    # Group: modpack

    @bot.command
    @lightbulb.command('modpack', 'Modpack Group')
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def modpackgroup(ctx):
        pass

    @modpackgroup.child
    @lightbulb.command('link', 'Get the modpack link')

    @modpackgroup.child
    @lightbulb.command('description', 'Get the modpack description')

    @modpackgroup.child
    @lightbulb.command('modlist', 'Get the modpack modlist')

    @modpackgroup.child
    @lightbulb.command('install', 'Get the procedure to install the modpack')

    @modpackgroup.child
    @lightbulb.command('help', 'Get information about the commands')

    # Command: staff

    @bot.command
    @lightbulb.command('staff', 'Get a description of the staff')

    # Group: warn

    @bot.command
    @lightbulb.command('warn', 'Warn Group')
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def warngroup(ctx):
        pass

    @warngroup.child
    @lightbulb.command('add', 'Add a warning to a player')

    @warngroup.child
    @lightbulb.command('remove', 'Remove a warning to a player')

    @warngroup.child
    @lightbulb.command('list', 'Get the list of warnings of a player')

    @warngroup.child
    @lightbulb.command('clear', 'Clear the warnings of a player')

    @warngroup.child
    @lightbulb.command('ban', 'Ban a player')

    @warngroup.child
    @lightbulb.command('help', 'Get information about the commands')

    bot.run()



if __name__ == '__main__':
    runbot()