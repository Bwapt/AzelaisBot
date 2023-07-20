#!/usr/bin/env python3
#pylint: skip-file


from init.__init__ import bot_init
import commands.cmd as cmd
import hikari as hk
import lightbulb





def runbot():
    bot = bot_init()

#    commands.modVersionList("gravestones")
#    commands.modLatestVersion("gravestones")
#    commands.modLoader("gravestones")
#    commands.modSearchList("gravestones")
#    commands.modLink("gravestones")
#    commands.modDescription("gravestones")
#    commands.modListLatestVersion(modList)

    @bot.listen(hk.StartedEvent)
    async def on_started(event):
        print("Bot has started !")



#######################################################################
############################ COMMANDS #################################
#######################################################################


    @bot.command
    @lightbulb.set_max_concurrency(1, lightbulb.GlobalBucket)
    @lightbulb.command('mod', 'Azelais Group')
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def modgroup(ctx):
        pass

 
    #   /mod search <mod>   #
    
    @modgroup.child
#    @lightbulb.option("loader", "the loader you want to check", type=str, required=False)
    @lightbulb.option("mod", "the mod to check", type=str)
    @lightbulb.command('search', 'search the mod')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def search(ctx):
        resp = await ctx.respond("Please wait...")
        result = cmd.modSearchList(ctx.options.mod)
        print(result)
        message = await resp.message()
        await message.edit(result)

    #   /mod url <mod>   #

    @modgroup.child
    @lightbulb.option("mod", "the mod to check", type=str)
    @lightbulb.command('url', 'the url of the website page of the mod')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def url(ctx):
        resp = await ctx.respond("Please wait...")
        result = cmd.modURL(ctx.options.mod)
        print(result)
        message = await resp.message()
        await message.edit(result)

    #   /mod lastversion <mod>  #

    @modgroup.child
#    @lightbulb.option("loader", "the loader you want to check", type=str, required=False)
    @lightbulb.option("mod", "the mod to check", type=str)
    @lightbulb.command('lastversion', 'get the last version of the mod')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def lastversion(ctx):
        resp = await ctx.respond("Please wait...")
        result = cmd.modLatestVersion(ctx.options.mod)
        print(result)
        message = await resp.message()
        await message.edit(result)
    

    #   /mod versionlist <mod>  #

    @modgroup.child
#    @lightbulb.option("loader", "the loader you want to check", type=str, required=False)
    @lightbulb.option("mod", "the mod to check", type=str)
    @lightbulb.command('versionlist', 'get a list of versions of the mod')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def versionlist(ctx):
        resp = await ctx.respond("Please wait...")
        result = cmd.modVersionList(ctx.options.mod)
        print(result)
        message = await resp.message()
        await message.edit(result)


    #   /mod loader <mod>   #

    @modgroup.child
    @lightbulb.option("mod", "the mod to check", type=str)
    @lightbulb.command('loader', 'get a list of available loaders for the mod')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def loader(ctx):
        resp = await ctx.respond("Please wait...")
        result = cmd.modLoader(ctx.options.mod)
        print(result)
        message = await resp.message()
        await message.edit(result)


    #   /mod listlastversion <file>  #

    @modgroup.child
#    @lightbulb.option("loader", "the loader you want to check", type=str, required=False)
    @lightbulb.option("file", "the file to check", type=hk.Attachment)
    @lightbulb.command('listlastversion', 'get the last version of a list of mods')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def modlist(ctx):
        resp = await ctx.respond("Please wait...")
        message = await resp.message()
        async with ctx.options.file.stream() as stream:
            Webdata = await stream.read()

            data = Webdata.decode("utf-8")
        
            list = data.split("\n")
            list.remove('')
            
            result = cmd.modListLatestVersion(list)
            print(result)

        await message.edit(result)


    #   /mod description <mod>  #

    @modgroup.child
    @lightbulb.option("mod", "the mod to check", type=str)
    @lightbulb.command('desc', 'get a short description of the mod')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def desc(ctx):
        resp = await ctx.respond("Please wait...")
        result = cmd.modDesc(ctx.options.mod)
        print(result)
        message = await resp.message()
        await message.edit(result)

    @modgroup.child
    @lightbulb.option("command", "the command to check", type=str, choices=("search", "url", "lastversion", "versionlist", "loader", "listlastversion", "desc"))
    @lightbulb.command("help", "get help for a command")
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def help(ctx):
        resp = await ctx.respond("Please wait...")
        result = cmd.modHelp(ctx.options.command)
        print(result)
        message = await resp.message()
        await message.edit(result)

    #   /mod download <mod> #

#    @modgroup.child
#    @lightbulb.option("loader", "the loader you want to check", type=str, required=False)
#    @lightbulb.option("game_version", "the game version of the mod", type=str)
#    @lightbulb.option("mod", "the mod to check", type=str)
#    @lightbulb.command('download', 'get the url of the mod requested')
#    @lightbulb.implements(lightbulb.SlashSubCommand)
#    async def download(ctx):
#        await ctx.respond("Please wait...")
#        result = commands.modDownload(ctx.options.mod, ctx.options.game_version)
#        print(result)
#        await ctx.respond(result)



    bot.run()



if __name__ == '__main__':
    runbot()