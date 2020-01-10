import discord
from cocks import commands


async def construct_embed():
    embed = discord.Embed(title="Commands help", color=0x405ecf)
    for func_name in dir(commands):
            func_desc = func_name.__doc__.split("\n")
            embed.add_field(name=func_name, value=func_desc[0])
    return embed