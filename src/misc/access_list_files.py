import json

# Warn

def get_warnlist() -> dict:
    warnlist = {}
    js: dict = {}
    with open('src/data/warnlist.txt', 'r') as f:
        warnlist = f.read()
        if bool(warnlist):
            js = json.loads(warnlist)
            
    return js

def str_warnlist(warnlist: dict):
    with open('src/data/warnlist.txt', 'w') as f:
        f.write(json.dumps(warnlist))

# Ban

def get_banlist() -> dict:
    banlist = {}
    js: dict = {}
    with open('src/data/banlist.txt', 'r') as f:
        banlist = f.read()
        if bool(banlist):
            js = json.loads(banlist)

    return js

def str_banlist(banlist: dict):
    with open('src/data/banlist.txt', 'w') as f:
        f.write(json.dumps(banlist))

# Twitch

def get_streamers() -> dict:
    streamers = {}
    js: dict = {}
    with open('src/data/streamers.txt', 'r') as f:
        streamers = f.read()
        if bool(streamers):
            js = json.loads(streamers)

    return js

def str_streamers(streamers: dict):
    with open('src/data/streamers.txt', 'w') as f:
        f.write(json.dumps(streamers))

# Youtube

def get_youtubers() -> dict:
    youtubers = {}
    js: dict = {}
    with open('src/data/youtubers.txt', 'r') as f:
        youtubers = f.read()
        if bool(youtubers):
            js = json.loads(youtubers)

    return js

def str_youtubers(youtubers: dict):
    with open('src/data/youtubers.txt', 'w') as f:
        f.write(json.dumps(youtubers))