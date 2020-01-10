from cocks import preferences



async def ping(msg, bot, cmd): #The message object from discord, the client object from discord, the cut up message without the prefix
    """
Ping! Pong!
Simply responds with Pong!
    """
    await msg.channel.send("Pong!")

async def setprefix(msg, bot, cmd):
    """
Set my prefix
Set the prefix you want me to listen out for. I will always respond to !help
    """
    print

# permission levels:
# 0 Everyone
# 1 has admin perms
# 2 is guild owner
#
# Need function in preferences.py that takes function_name, guild_id, user_permission_level and returns true if the command is allowed to be used by the user
#
#