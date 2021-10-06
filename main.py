# Imports
import discord
import datetime
import random
import os

from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime, timedelta

client = commands.Bot(command_prefix='.')

# load the file that contain the bot token
load_dotenv()

# path to images for pxg
pxg_screen_path = r".\pxg_image\\"

# dictionary that contain names of images for professions
profession_dict = {
    "sc": ['StylistaC1.png', 'StylistaC2.png', 'StylistaC3.png', 'StylistaC4.png', 'StylistaC5.png', 'StylistaC6.png',
           'StylistaC7.png'],
    "pa": ['pA1.png', 'pA2.png', 'pA3.png', 'pA4.png', 'pA5'],
    "pb": ['pB1.png', 'pB2.png', 'pB3.png', 'pB4.png'],
    "pc": ['pC1.png', 'pC2.png', 'pC3.png'],
    "pd": ['pD1.png', 'pD2.png', 'pD3.png'],
    "pe": ['pE.png'],
    "aa": ['advA1.png', 'advA2.png', 'advA3.png'],
    "ab": ['advB.png'],
    "ac": ['advC.png'],
    "ad": ['advD.png'],
    "ae": ['advE.png']}

# print in console when bot is ready
@client.event
async def on_ready():
    print("Bot is ready.")


# check bot ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping {round(client.latency * 1000)} ms')


# print a list of available commands commands
@client.command()
async def pxg(ctx):
    await ctx.send(f'stamina (hh:mm), boost (number_of_boost actual_boost wanted_boost),\n'
                   f'prof (first letter of profession)(profession level A-E)\n'
                   f'   available profession: adventurer, professor, stylist (only C for now)')


# count a number of stones required to boost pokemon "tabela boost" is on this webside:
# https://wiki.pokexgames.com/index.php/Tabela_de_Boost/pl#Boost_30
@client.command()
async def boost(ctx, number, level=0, max_boost=50):
    stone = 1
    boost_cost = 1
    stone_acquired = 0

    for i in range(1, max_boost):
        if i % int(number) == 0:
            stone = stone + 1

        if i == level:
            stone_acquired = boost_cost

        boost_cost = boost_cost + stone

    await ctx.send(f'You will need: {int(boost_cost - stone_acquired)} stones to boost your pokemon from +{level} to '
                   f'+{max_boost}')

@client.command()
async def prof(ctx, profession):
    ss_list = profession_dict.get(profession)
    for ss in ss_list:
        await ctx.send(file=discord.File(pxg_screen_path + ss))

# count when your stamina will be full(56:00)
@client.command(aliases=['S', 's', 'stamina'])
async def Stamina(ctx, *, time):
    stamina_count = timedelta(hours=00, minutes=00)
    hour, minute = time.split(':')
    current_time = datetime.today()

    if int(hour) > 56 or int(hour) < 0 or int(minute) > 60 or int(minute) < 0:
        await ctx.send(f'Invalid value')
        return 0

    if int(hour) <= 54:
        stamina_count = 2 * (timedelta(hours=54, minutes=00) - timedelta(hours=int(hour), minutes=int(minute)))
        stamina_count_boosted = 6 * (timedelta(hours=56, minutes=00) - timedelta(hours=54, minutes=0))
    else:
        stamina_count_boosted = 6 * (timedelta(hours=56, minutes=00) - timedelta(hours=int(hour), minutes=int(minute)))

    response = current_time + stamina_count + stamina_count_boosted
    response = response.strftime('%d/%m %H:%M')
    await ctx.send(f'Full stamina will be available at: {response}')

# a command to rolling dice
@client.command()
async def roll(ctx, dice):
    d, number = dice.split("d")
    for i in range(0, int(d)):
        responses = random.randint(1, int(number))
        await ctx.send(f'rolled {responses}')

client.run(os.getenv('BOT_TOKEN'))
