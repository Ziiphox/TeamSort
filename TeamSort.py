import discord
import json
import types

from cocks import commands
from cocks import preferences

with open("data/config.json") as json_file:
  config = json.load(json_file)

print(f'Loading Discord.py v{discord.__version__}')
bot = discord.Client()



@bot.event
async def on_ready():
    print(f'Online as {bot.user.name}#{bot.user.discriminator}!')
    if (bot.user.name != config["bot_name"]): #Change bot_name in config file to change bot's name on next start up. May run in to ratelimit issues if done too often.
        print(f'Name change detected!')
        await bot.user.edit(username=config["bot_name"])



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



#only mostly stolen lol
functions = get_functions(commands)
switch = {function.__name__: function for function in get_functions(commands)}



@bot.event
async def on_message(message):
    #big spaghetti block for testing if the guild exists and changing the prefix
    if (preferences.get_guild_prefix(message.guild.id)):
        if (message.content.lower() == f'{config["default_prefix"]}help'): #In case you forget the bot's prefix.
            await commands.help(message, bot, message.content.lower()[len(config["default_prefix"]):].split())
            return
        
        if not (message.content.startswith(preferences.get_guild_prefix(message.guild.id))): #Return if message doesn't start with guild prefix
            print(preferences.get_guild_prefix(message.guild.id))
            return
        
        func_name = message.content.lower()[len(preferences.get_guild_prefix(message.guild.id)):].split()
    else:
        await preferences.setup_guild(message.guild.id)
        if not (message.content.startswith(config["default_prefix"])):
            return
        func_name = message.content.lower()[len(config["default_prefix"]):].split()

    if func_name[0] in switch:
         await switch[func_name[0]](message, bot, func_name)



bot.run(config["token"]) #must be last function in file 