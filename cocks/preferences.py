import sqlite3
from os import path
if (path.exists("data/guilds.db")):
    guilds = sqlite3.connect("data/guilds.db")
    db = guilds.cursor()
else:
    guilds = sqlite3.connect("data/guilds.db")
    db = guilds.cursor()
    print("Guild preferences database does not exist. Creating now!")
    db.execute('''CREATE TABLE guilds (id, prefix, PRIMARY KEY (id) )''')

async def get_guild_prefix(id):
    print