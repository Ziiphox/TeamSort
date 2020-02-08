import sqlite3
import json
from os import path
from cocks import commands
from cocks import tools

with open("data/config.json") as json_file:
  config = json.load(json_file)




def get_guild_prefix(id):
    db.execute(f'SELECT prefix FROM guilds WHERE id={id}')
    prefix = db.fetchone()
    if not (prefix == None):
        return prefix[0]
    else:
        return False

async def setup_guild(id):
    db.execute(f'INSERT INTO guilds VALUES ({id}, \'{config["default_prefix"]}\')')
#    db.execute(f'INSERT INTO commands VALUES ({id})')
    guilds.commit()

async def set_guild_prefix(id, prefix):
    db.execute(f'UPDATE guilds SET prefix=\'{prefix}\' WHERE id={id}')
    guilds.commit()


#                    |
# Admin-y type tools |
#                    V

def add_command_column(name):
    db.execute(f'ALTER TABLE commands ADD {name} real')
    print(f'Adding {name} column to commands table')

def remove_command_column(name):
    db.execute(f'ALTER TABLE commands DROP COLUMN {name}')
    print(f'Removing {name} column from commands table')

def check_command_columns():
    db.execute('PRAGMA table_info(commands)')
    columns = db.fetchall()
    # Compares function name to all column names in commands table, if any of them match then compare the next function name..
    for function in tools.get_functions(commands):
        if not (any(function.__name__ == column[1] for column in columns)):
            add_command_column(function.__name__)
    guilds.commit()



if (path.exists("data/data.db")):
    guilds = sqlite3.connect("data/data.db")
    db = guilds.cursor()
else:
    guilds = sqlite3.connect("data/data.db")
    db = guilds.cursor()
    print("Guild data database does not exist. Creating now!")
    db.execute('CREATE TABLE guilds (id text, prefix text, PRIMARY KEY (id) )')
    db.execute('CREATE TABLE commands (id text, PRIMARY KEY (id) )')
    guilds.commit()