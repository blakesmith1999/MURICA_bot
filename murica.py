import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    guild = discord.utilis.get(bot.guilds, name=GUILD)
    chnl=guild.system_channel
    await chnl.send(f'{bot.user.name} is here to liberate your oil')

@bot.event
async def on_message(message):
    await message.add_reaction(':flag_us:')

@bot.command(name='freedom', help='gives a random quote from a Founding Father')
async def freedom(ctx):
    founding_father_quotes = ['1. "Always stand on principle...even if you stand alone." - John Adams', 
    '2. "If you want something you\'ve never had, you must be willing to do something you\'ve never done." - Thomas Jefferson',
    '3. "Well done is better than well said." - Benjamin Franklin',
    '4. "The circulation of confidence is better than the circulation of money." - James Madison',
    '5. "It is better to offer no excuse than a bad one." - George Washington',
    '6. "Distrust naturally creates distrust, and by nothing is good will and kind conduct more speedily changed." - John Jay',
    '7. "To succeed, jump as quickly at opportunities as you do at conclusions." - Benjamin Franklin',
    '8. "Do you want to know who you are? Don\'t ask. Act! Action will delineate and define you." - Thomas Jefferson',
    '9. "Learn to think continentally." - Alexander Hamilton',
    '10. "Dost thou love life? Then do not squander time, for that is the stuff life is made of." - Benjamin Franklin',
    '11. "Nothing can stop the man with the right mental attitude from achieving his goal; nothing on earth can help the man with the wrong mental attitude." - Thomas Jefferson',
    '12. "Ambition must be made to counteract ambition." - James Madison',
    '13. "Without continual growth and progress, such words as improvement, achievement, and success have no meaning." - Benjamin Franklin',
    '14. "Whenever you do something, act as if all the world were watching." - Thomas Jefferson',
    '15. "The advancement and diffusion of knowledge is the only guardian of true liberty." - James Madison',
    '16. "Tell me and I forget. Teach me and I remember. Involve me and I learn." - Benjamin Franklin',
    '17. "The people are the only legitimate fountain of power." - James Madison',
    '18. "Those who own the country ought to govern it." - John Jay',
    '19. "Either write something worth reading or do something worth writing." - Benjamin Franklin',
    '20. "Truth will ultimately prevail where there is pains to bring it to light." - George Washington',
    '21. "Never leave that till tomorrow which you can do today." - Benjamin Franklin',
    '22. "Real firmness is good for anything; strut is good for nothing." - Alexander Hamilton',
    '23. "Energy and persistence conquer all things." - Benjamin Franklin',]

    response = random.choice(founding_father_quotes)
    await ctx.send(response)

    
@bot.command(name='restart')
async def restart(ctx):
    await ctx.close()
    await ctx.clear()
    await ctx.start()

bot.run(TOKEN)