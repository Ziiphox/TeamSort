import sqlite3
import json
from os import path

if (path.exists("data/guilds.db")):
    guilds = sqlite3.connect("data/guilds.db")
    db = guilds.cursor()
else:
    guilds = sqlite3.connect("data/guilds.db")
    db = guilds.cursor()
    print("Guild preferences database does not exist. Creating now!")
    db.execute('''CREATE TABLE guilds
                  (id text, prefix text, PRIMARY KEY (id) )''')
    guilds.commit()

with open("data/config.json") as json_file:
  config = json.load(json_file)



def get_guild_prefix(id):
    db.execute(f'SELECT prefix FROM guilds WHERE id={id}')
    return db.fetchone()

async def setup_guild(id):
    db.execute(f'INSERT INTO guilds VALUES ({id}, \'{config["default_prefix"]}\')')
    guilds.commit()

async def set_guild_prefix(id, prefix):
    db.execute(f'UPDATE guilds SET prefix=\'{prefix}\' WHERE id={id}')
    guilds.commit()