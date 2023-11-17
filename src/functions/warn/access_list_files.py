import json

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