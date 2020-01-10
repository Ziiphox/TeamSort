import discord
from cocks import commands


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


def construct_embed():
    embed = discord.Embed(title="Commands help", color=0x405ecf)

    for function in get_functions(commands):
        function_name = function.__name__
        function_description = function.__doc__.split("\n")
        embed.add_field(name=function_name, value=function_description[0])

        return embed
