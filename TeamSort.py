import discord
import json

from cocks import commands
from cocks import preferences
from cocks import tools

with open("data/config.json") as json_file:
  config = json.load(json_file)

print(f'Loading Discord.py v{discord.__version__}')
bot = discord.Client()



@bot.event
async def on_ready():
    print(f'Online as {bot.user.name}#{bot.user.discriminator}!')
    preferences.check_command_columns()
    if (bot.user.name != config["bot_name"]): # Change bot_name in config file to change bot's name on next start up. May run in to ratelimit issues if done too often.
        print(f'Name change detected!')
        await bot.user.edit(username=config["bot_name"])



# saving a list of all function / command names in commands file
switch = {function.__name__: function for function in tools.get_functions(commands)}



@bot.event
async def on_message(message):
    # big spaghetti block for testing if the guild exists and changing the prefix
    if (preferences.get_guild_prefix(message.guild.id)):

        # In case you forget the bot's prefix.
        if (message.content.lower() == f'{config["default_prefix"]}help'): 
            await commands.help(message, bot, message.content.lower()[len(config["default_prefix"]):].split())
            return
        
        # Return if message doesn't start with guild prefix
        if not (message.content.startswith(preferences.get_guild_prefix(message.guild.id))):
            return
        
        command = message.content.lower()[len(preferences.get_guild_prefix(message.guild.id)):].split()
    else:
        await preferences.setup_guild(message.guild.id)
        if not (message.content.startswith(config["default_prefix"])):
            return
        command = message.content.lower()[len(config["default_prefix"]):].split()

    if command[0] in switch:
         await switch[command[0]](message, bot, command)



bot.run(config["token"]) #must be last function in file 