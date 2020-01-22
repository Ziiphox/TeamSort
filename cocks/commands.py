import discord
from cocks import preferences
from cocks import help_command



async def ping(msg, bot, cmd): #The message object from discord, the client object from discord, the cut up message without the prefix
#Docstrings in functions in this file repersent what to display in the help command. 
#First line is a very short description for when viewing all commands,
#second line is more descriptive and used when viewing help for a single command,
#third line is the "default permission" of the command.
    """
Ping! Pong!
Simply responds with Pong!
0
    """
    await msg.channel.send("Pong!")
    preferences.check_command_columns()

async def setprefix(msg, bot, cmd):
    """
Set my prefix
Set the prefix you want me to listen out for. I will always respond to !help
2
    """
    if not (len(cmd) == 2):
        await msg.channel.send("You need to set a prefix. Example: !setprefix `$`")
    elif (len(cmd[1]) > 5):
        await msg.channel.send("Prefix is too long. Use a shorter pefix. Example: `!` `##` `abc`")
    else:
        await preferences.set_guild_prefix(msg.guild.id, cmd[1])
        await msg.channel.send(f'Changed prefix to {cmd[1]}')

async def help(msg, bot, cmd):
    """
Help command
Shows the commands you can access. Use !help [command] to see more in-depth explination.
0
    """
    if (len(cmd) == 2):
        await msg.channel.send(embed = help_command.find_command(cmd[1]))
    else:
        await msg.channel.send(embed = help_command.construct_embed(msg.guild.id))

# for later
# permission levels:
# 0 Everyone
# 1 has admin perms
# 2 is guild owner
#
# Need function in preferences.py that takes function_name, guild_id, user_permission_level and returns true if the command is allowed to be used by the user
#
#