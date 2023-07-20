#!/usr/bin/env python3
#pylint: skip-file

from itertools import chain
import modrinth

class ModrinthCmd:
    def __init__(self, mod) -> None :
        mod = mod.replace(" ", "-")

        self.mod = ModrinthCmd.setMod(self, mod)
        if self.mod == None:
            return
        ModrinthCmd.setProject(self, self.mod)


    def setMod(self, mod):
        searchmod = modrinth.Projects.Search(mod)
        is_mod_correct = False
        
        i = 0
        while(i < len(searchmod.hits) and is_mod_correct != True):
            if (mod == searchmod.hits[i].slug):
                ret = mod
                is_mod_correct = True
            i = i + 1

        if (is_mod_correct != True):
            try:
                ret = searchmod.hits[0].slug
            except IndexError:
                ret = None
        
        return ret

    def setProject(self, mod):
        self.project : modrinth.Projects.ModrinthProject = modrinth.Projects.ModrinthProject(mod)

    def getModName(self):
        name = self.project.name

        return name

    def getModeSlug(self):
        slug = self.project.slug

        return slug


# modLink()
    def getModURL(self):
        url = "https://modrinth.com/mod/" + self.mod

        return url


# modSearchList()
    def getModList(self) -> list:
        mod_list = []

        mods = modrinth.Projects.Search(self.mod)

        for i in range (len(mods.hits)):
            mod_result = []
            mod_result.append(mods.hits[i].name)
            mod_result.append(mods.hits[i].slug)
            mod_list.append(mod_result)
        
        print(mod_list)
        return mod_list


# modLatestVersion()
    def getModLatestVersion(self) -> str :
        mc_ver = ModrinthCmd(self.mod).getModVersionList().pop()
        
        return mc_ver


# modVersionList()
    def getModVersionList(self) -> list :
        mc_ver = []
        mc_ver_tocheck = []
        official_mc_ver = []
        non_official_mc_ver = []
        isofficial = False

        for i in range (len(self.project.versions)):
            project_ver = self.project.versions[i]
            mc_ver.append(modrinth.Versions.ModrinthVersion(self.project, project_ver).gameVersions)

        mc_ver = list(dict.fromkeys(list(chain.from_iterable(mc_ver))))
        for i in range (len(mc_ver)):
            mc_ver_tocheck.append(mc_ver[i].split('.'))
            isofficial = True

            for j in range (len(mc_ver_tocheck[i])):
                if(mc_ver_tocheck[i][j].isnumeric() == True):
                    mc_ver_tocheck[i][j] = int(mc_ver_tocheck[i][j])
                else:
                    isofficial = False

            if(isofficial == True):
                official_mc_ver.append(mc_ver_tocheck[i])
            else:
                non_official_mc_ver.append(mc_ver_tocheck[i])
                
            official_mc_ver.sort()

        for i in range(len(official_mc_ver)):
            official_mc_ver[i] = '.'.join(map(str, official_mc_ver[i]))

        return official_mc_ver


# modLoader()
    def getModLoader(self) -> str:
        mc_loader = []
        
        for i in range (len(self.project.versions)):
            project_ver = self.project.versions[i]
            mc_loader.append(modrinth.Versions.ModrinthVersion(self.project, project_ver).loaders)
        
        mc_loader = list(dict.fromkeys(list(chain.from_iterable(mc_loader))))

        return mc_loader


# modDescription()
    def getModDesc(self):
        desc = self.project.desc

        return desc

# modDownload()
    def getModDownload(self, game_version):
        for i in range (len(self.project.versions)):
            version = self.project.getVersion(self.project.versions[i])
            for j in range (len(version.gameVersions)):
                if version.gameVersions[j] == game_version:
                    print(self.project.versions[i])


