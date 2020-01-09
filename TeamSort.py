import discord
import json

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


@bot.event
async def on_message(message):
    if (test[message.content]):
        test[message.content]()


bot.run(config["token"])