import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

# import os
# from dotenv import load_dotenv
# from discord.ext import commands

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# bot = commands.Bot(command_prefix='$')

# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} is here for your oil')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user.name:
#         return
#     await message.add_reaction(':flag_us:')

# @bot.command(name='restart')
# async def restart(ctx):
#     await ctx.close()
#     await ctx.clear()
#     await ctx.start()

# bot.run(TOKEN)