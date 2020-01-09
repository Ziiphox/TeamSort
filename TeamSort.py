import discord
import json
import types

from cocks import test

with open("config.json") as json_file:
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



functions = get_functions(test)
switch = {function.__name__: function for function in get_functions(test)}
prefix = config["default_prefix"]

@bot.event
async def on_message(message):
    if not (message.content.startswith(config["default_prefix"])):
        return
    func_name = message.content.lower()[len(prefix):].split()
    if func_name[0] in switch:
         await switch[func_name[0]](message, bot)


bot.run(config["token"])