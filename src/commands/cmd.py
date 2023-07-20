#!/usr/bin/env python3
#pylint: skip-file

# import curseforge_cmd
from commands.modrinth.modrinth_cmd import ModrinthCmd
from commands.misc.help import ModHelp

def modURL(mod):
    mods = ModrinthCmd(mod)

    if(mods == None):
        ret = errorMessage()
    else:
        ret = "Here is the URL of the **" + mods.getModName() + "** webpage :\n" + mods.getModURL()

    return ret

# mod()

def modSearchList(mod):
    mods = ModrinthCmd(mod)

    if(mods == None):
        ret = errorMessage()
    else:
        ret = "Here is a list of mods for the research **" + mod + "** :\n"

        modList = mods.getModList()

        for i in range (len(modList)):
            ret = ret + "- **" + modList[i][0] + "** : (" + modList[i][1] + ")\n"


    return ret

def modLatestVersion(mod):
    mods = ModrinthCmd(mod)

    if(mods == None):
        ret = errorMessage()
    else:
        ret = "The last version of **" + mods.getModName() + "** is : " + mods.getModLatestVersion()
    
    return ret

def modVersionList(mod):
    mods = ModrinthCmd(mod)

    if(mods == None):
        ret = errorMessage()
    else:
        ret = "Here is a list of every available versions of **" + mods.getModName() + "** :\n"
   
        versionList = mods.getModVersionList()
   
        for i in range (len(versionList)):
            ret = ret + "- " + versionList[i] + "\n"

    return ret

# modListLatestVersion()
def modListLatestVersion(modList):
    ret = "Here is a list of the latest version available of each mods listed :\n"

    for i in range (len(modList)):
        mods = ModrinthCmd(modList[i])
        if(mods.mod == None):
            ret = ret + "- **" + modList[i] + "** : " + errorMessage()
        else:
            ret = ret + "- **" + mods.getModName() + "** : " + mods.getModLatestVersion() + "\n"
        print(modList[i])
    return ret

# modLoader()
def modLoader(mod):
    mods = ModrinthCmd(mod)
    if(mods == None):
            ret = errorMessage()
    else:
        ret = "Here is a list of available loaders for **" + mods.getModName() + "**\n"

        loaders = mods.getModLoader()
    
        for i in range (len(loaders)):
            ret = ret + "- " + loaders[i] + "\n"
    
    return ret

# modDescription()
def modDesc(mod):
    mods = ModrinthCmd(mod)
    if(mods == None):
            ret = errorMessage()
    else:
        ret = "Here is a short description of **" + mods.getModName() + "** :\n" + mods.getModDesc()
    
    return ret

# modDownload()
def modDownload(mod, game_version):
    mods = ModrinthCmd(mod)
    if(mods == None):
            ret = errorMessage()
    else:
        print(mods.getModDownload(game_version))


def modHelp(cmd):
    match cmd:
        case "search":
            ret = ModHelp.search()
        case "url":
            ret = ModHelp.url()
        case "lastversion":
            ret = ModHelp.lastversion()
        case "versionlist":
            ret = ModHelp.versionlist()
        case "loader":
            ret = ModHelp.loader()
        case "listlastversion":
            ret = ModHelp.listlastversion()
        case "desc":
            ret = ModHelp.desc()
        
    
    return ret


def errorMessage():
    return "Sorry, the mod you are seeking for is not in our database. Please try something else.\n"