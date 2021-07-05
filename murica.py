import os
from typing import ContextManager
import discord
import random
import re
from discord import activity
from discord.activity import CustomActivity
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    chnl=guild.system_channel
    await chnl.send(f'{bot.user.name} is here to liberate your oil')
    

@bot.event
async def on_message(message):
    await message.add_reaction('🇺🇸')

    if message.author == bot.user or message.content.startswith('$'):
        await bot.process_commands(message)
        return
    
    # if not '🇺🇸' in message.content:
    #     await message.reply('Pretty cringe ngl. You dropped this :flag_us:')

    communism=re.compile(r'communi|commi',re.I)
    america=re.compile(r'america|United States',re.I)
    fireworks=re.compile(r'firework',re.I)
    guns=re.compile(r'gun',re.I)

    if communism.search(message.content):
        await message.channel.send(file=discord.File(r'E:/Memes/communism1.gif'))

    if america.search(message.content):
        await message.channel.send('History began on July 4, 1776. Everything before that was a mistake.')

    if fireworks.search(message.content):
        await message.channel.send(file=discord.File(r'E:/Memes/fireworks.gif'))

    if guns.search(message.content):
        await message.channel.send(file=discord.File(r'E:/Memes/guns.gif'))

    await bot.process_commands(message)


@bot.command(name='liberty')
async def liberty(ctx):
    await ctx.send(file=discord.File(r'E:/Memes/Give-me-Liberty-or-Give-me-Death.jpg'))

@bot.command(name='freedom', help='gives a random quote from a Founding Father')
async def freedom(ctx):
    founding_father_quotes = ['"Always stand on principle...even if you stand alone." - John Adams', 
    '"If you want something you\'ve never had, you must be willing to do something you\'ve never done." - Thomas Jefferson',
    '"Well done is better than well said." - Benjamin Franklin',
    '"The circulation of confidence is better than the circulation of money." - James Madison',
    '"It is better to offer no excuse than a bad one." - George Washington',
    '"Distrust naturally creates distrust, and by nothing is good will and kind conduct more speedily changed." - John Jay',
    '"To succeed, jump as quickly at opportunities as you do at conclusions." - Benjamin Franklin',
    '"Do you want to know who you are? Don\'t ask. Act! Action will delineate and define you." - Thomas Jefferson',
    '"Learn to think continentally." - Alexander Hamilton',
    '"Dost thou love life? Then do not squander time, for that is the stuff life is made of." - Benjamin Franklin',
    '"Nothing can stop the man with the right mental attitude from achieving his goal; nothing on earth can help the man with the wrong mental attitude." - Thomas Jefferson',
    '"Ambition must be made to counteract ambition." - James Madison',
    '"Without continual growth and progress, such words as improvement, achievement, and success have no meaning." - Benjamin Franklin',
    '"Whenever you do something, act as if all the world were watching." - Thomas Jefferson',
    '"The advancement and diffusion of knowledge is the only guardian of true liberty." - James Madison',
    '"Tell me and I forget. Teach me and I remember. Involve me and I learn." - Benjamin Franklin',
    '"The people are the only legitimate fountain of power." - James Madison',
    '"Those who own the country ought to govern it." - John Jay',
    '"Either write something worth reading or do something worth writing." - Benjamin Franklin',
    '"Truth will ultimately prevail where there is pains to bring it to light." - George Washington',
    '"Never leave that till tomorrow which you can do today." - Benjamin Franklin',
    '"Real firmness is good for anything; strut is good for nothing." - Alexander Hamilton',
    '"Energy and persistence conquer all things." - Benjamin Franklin',]

    response = random.choice(founding_father_quotes)
    await ctx.send(response)

@bot.command(name='independence')
async def independence(ctx):
    declaration = ["In Congress, July 4, 1776\nThe unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.\n\nWe hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.--Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government.","The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world.\n\n\tHe has refused his Assent to Laws, the most wholesome and necessary for the public good.\n\n\tHe has forbidden his Governors to pass Laws of immediate and pressing importance, unless suspended in their operation till his Assent should be obtained; and when so suspended, he has utterly neglected to attend to them.\n\n\tHe has refused to pass other Laws for the accommodation of large districts of people, unless those people would relinquish the right of Representation in the Legislature, a right inestimable to them and formidable to tyrants only.\n\n\tHe has called together legislative bodies at places unusual, uncomfortable, and distant from the depository of their public Records, for the sole purpose of fatiguing them into compliance with his measures.\n\n\tHe has dissolved Representative Houses repeatedly, for opposing with manly firmness his invasions on the rights of the people.\n\n\tHe has refused for a long time, after such dissolutions, to cause others to be elected; whereby the Legislative powers, incapable of Annihilation, have returned to the People at large for their exercise; the State remaining in the mean time exposed to all the dangers of invasion from without, and convulsions within.\n\n\tHe has endeavoured to prevent the population of these States; for that purpose obstructing the Laws for Naturalization of Foreigners; refusing to pass others to encourage their migrations hither, and raising the conditions of new Appropriations of Lands.\n\n\tHe has obstructed the Administration of Justice, by refusing his Assent to Laws for establishing Judiciary powers.\n\n\tHe has made Judges dependent on his Will alone, for the tenure of their offices, and the amount and payment of their salaries.","\n\n\tHe has erected a multitude of New Offices, and sent hither swarms of Officers to harrass our people, and eat out their substance.\n\n\tHe has kept among us, in times of peace, Standing Armies without the Consent of our legislatures.\n\n\tHe has affected to render the Military independent of and superior to the Civil power.\n\n\tHe has combined with others to subject us to a jurisdiction foreign to our constitution, and unacknowledged by our laws; giving his Assent to their Acts of pretended Legislation:\n\n\tFor Quartering large bodies of armed troops among us:\n\n\tFor protecting them, by a mock Trial, from punishment for any Murders which they should commit on the Inhabitants of these States:\n\n\tFor cutting off our Trade with all parts of the world:\n\n\tFor imposing Taxes on us without our Consent:\n\n\tFor depriving us in many cases, of the benefits of Trial by Jury:\n\n\tFor transporting us beyond Seas to be tried for pretended offences\n\n\tFor abolishing the free System of English Laws in a neighbouring Province, establishing therein an Arbitrary government, and enlarging its Boundaries so as to render it at once an example and fit instrument for introducing the same absolute rule into these Colonies:","\n\n\tFor taking away our Charters, abolishing our most valuable Laws, and altering fundamentally the Forms of our Governments:\n\n\tFor suspending our own Legislatures, and declaring themselves invested with power to legislate for us in all cases whatsoever.\n\n\tHe has abdicated Government here, by declaring us out of his Protection and waging War against us.\n\n\tHe has plundered our seas, ravaged our Coasts, burnt our towns, and destroyed the lives of our people.\n\n\tHe is at this time transporting large Armies of foreign Mercenaries to compleat the works of death, desolation and tyranny, already begun with circumstances of Cruelty & perfidy scarcely paralleled in the most barbarous ages, and totally unworthy the Head of a civilized nation.\n\n\tHe has constrained our fellow Citizens taken Captive on the high Seas to bear Arms against their Country, to become the executioners of their friends and Brethren, or to fall themselves by their Hands.\n\n\tHe has excited domestic insurrections amongst us, and has endeavoured to bring on the inhabitants of our frontiers, the merciless Indian Savages, whose known rule of warfare, is an undistinguished destruction of all ages, sexes and conditions.","\n\n\tIn every stage of these Oppressions We have Petitioned for Redress in the most humble terms: Our repeated Petitions have been answered only by repeated injury. A Prince whose character is thus marked by every act which may define a Tyrant, is unfit to be the ruler of a free people.\n\n\tNor have We been wanting in attentions to our Brittish brethren. We have warned them from time to time of attempts by their legislature to extend an unwarrantable jurisdiction over us. We have reminded them of the circumstances of our emigration and settlement here. We have appealed to their native justice and magnanimity, and we have conjured them by the ties of our common kindred to disavow these usurpations, which, would inevitably interrupt our connections and correspondence. They too have been deaf to the voice of justice and of consanguinity. We must, therefore, acquiesce in the necessity, which denounces our Separation, and hold them, as we hold the rest of mankind, Enemies in War, in Peace Friends.\n\nWe, therefore, the Representatives of the united States of America, in General Congress, Assembled, appealing to the Supreme Judge of the world for the rectitude of our intentions, do, in the Name, and by Authority of the good People of these Colonies, solemnly publish and declare, That these United Colonies are, and of Right ought to be Free and Independent States; that they are Absolved from all Allegiance to the British Crown, and that all political connection between them and the State of Great Britain, is and ought to be totally dissolved; and that as Free and Independent States, they have full Power to levy War, conclude Peace, contract Alliances, establish Commerce, and to do all other Acts and Things which Independent States may of right do. And for the support of this Declaration, with a firm reliance on the protection of divine Providence, we mutually pledge to each other our Lives, our Fortunes and our sacred Honor."]
    for paragraph in declaration:
        await ctx.send(paragraph)

# @bot.command(name='watchlist')
# async def watchlist(ctx):
#     msg1 = ctx.message.reference.message_id
#     messages = await ctx.channel.history(limit=20).flatten()
#     for msg in messages:
#         if msg.id == msg1:
#             user1=msg.author
#             member1=ctx.guild.get_member(user1.id)
#             role1 = discord.utils.get(ctx.guild.roles, name="CIA Watchlist")
#             role2 = discord.utils.get(ctx.guild.roles, name="gamer")
#             await member1.add_roles(role1)
#             await member1.remove_roles(role2)
#             await ctx.channel.send(f'{member1.name} has been added to a CIA watchlist. Kinda sus')
#             break

# @bot.command(name='list')
# async def list(ctx):
#     members = await ctx.guild.fetch_members().flatten()
#     for member in members:
#         print(member.name)
#         print(member.id)

bot.run(TOKEN)