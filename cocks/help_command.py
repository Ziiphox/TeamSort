import types
import discord
from cocks import commands
from cocks import preferences


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


def construct_embed(guild_id):
    embed = discord.Embed(title="Commands help", color=0x405ecf)

    for function in get_functions(commands):
        function_name = function.__name__
        function_description = function.__doc__.split("\n")
        embed.add_field(name=f'**{function_name}**', value=function_description[1])
    embed.set_footer(text=f'My prefix is {preferences.get_guild_prefix(guild_id)[0]}')
    return embed


def find_command(command):
    embed = discord.Embed(title="Command help", color=0x405ecf)

    for function in get_functions(commands):
        if (function.__name__ == command):
            function_description = function.__doc__.split("\n")
            embed.add_field(name=f'**{function.__name__}**', value=function_description[2])
            return embed
    #only gets here if command is not recognized
    embed.add_field(name='**Command not found**', value=f'Could not find the command `{command}`. Check your spelling')
    return embed