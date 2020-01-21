import sqlite3
import json
import types
from os import path
from cocks import commands


#STOLEN CODE LOL
def get_functions(library):
    # Getting a list of all the functions
    # that nunchi bot supports for a
    # message event.
    functions = []

    for attr_name in dir(library):
        # Getting one of the objects that message_actions 
        # has declared.
        library_object = getattr(library, attr_name)

        # Checking whether is a function defined
        # inside message_actions or if it belongs
        # to a library that was imported.
        if isinstance(library_object, types.FunctionType):
            functions.append(library_object)
    
    return functions




if (path.exists("data/data.db")):
    guilds = sqlite3.connect("data/data.db")
    db = guilds.cursor()
else:
    guilds = sqlite3.connect("data/data.db")
    db = guilds.cursor()
    print("Guild data database does not exist. Creating now!")
    db.execute('CREATE TABLE guilds (id text, prefix text, PRIMARY KEY (id) )')
    
    temp_query = "CREAT TABLE commands (id text"
    for function in get_functions(commands):
        temp_query+= f', {function.__name__} number'
    temp_query+= ", PRIMARY KEY (id) )"

    guilds.commit()

with open("data/config.json") as json_file:
  config = json.load(json_file)



def get_guild_prefix(id):
    db.execute(f'SELECT prefix FROM guilds WHERE id={id}')
    if (db.fetchone()):
        return db.fetchone()[0]
    else:
        return False

async def setup_guild(id):
    db.execute(f'INSERT INTO guilds VALUES ({id}, \'{config["default_prefix"]}\')')
#    db.execute(f'INSERT INTO commands VALUES ({id})')
    guilds.commit()

async def set_guild_prefix(id, prefix):
    db.execute(f'UPDATE guilds SET prefix=\'{prefix}\' WHERE id={id}')
    guilds.commit()


    #Add table "command_premissions"
    #guild-ID | help | changeprefix | ect
    #123465.. | 0    | 2            | 0-2
    #
    #
    #