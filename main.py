# Imports
import discord
import datetime
import random

import os
from discord.ext import commands
from datetime import datetime, timedelta

client = commands.Bot(command_prefix='.')

# path to images for pxg
pxg_screen_path = r".\pxg_image\\"



# print in console when bot is ready
@client.event
async def on_ready():
    print("Bot is ready.")


# check bot ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping {round(client.latency * 1000)} ms')


# print a list of pxg commands
@client.command()
async def pxg(ctx):
    await ctx.send(f'adventurerE, adventurerD, adventurerC, adventurerB, adventurerA, professorE, professorD, professorC,\
 professorA, stamina (hh:mm), boost (number_of_boost actual_boost wanted_boost) ')


# count a number of stones required to boost pokemon "tabela boost" is on this webside:
# https://wiki.pokexgames.com/index.php/Tabela_de_Boost/pl#Boost_30
@client.command()
async def boost(ctx, number, level=0, max_boost=50):
    stone = 1
    boost_cost = 1
    stone_used = 1
    stone_acquired = 1

    for i in range(1, max_boost):
        if i % int(number) == 0:
            stone = stone + 1

        boost_cost = boost_cost + stone

    for i in range(1, level):
        if i % int(number) == 0:
            stone_used = stone_used + 1

        stone_acquired = stone_acquired + stone_used

    if level == 0:
        stone_acquired = 0

    response = boost_cost - stone_acquired
    await ctx.send(f'You need: {int(response)} stones')


@client.command(aliases=['adventurere', 'ae', 'AE', 'aE'])
async def adventurerE(ctx):
    await ctx.send(file=discord.File(pxg_screen_path + 'advE.png'))


@client.command(aliases=['adventurerd', 'ad', 'AD', 'aD'])
async def adventurerD(ctx):
    await ctx.send(file=discord.File(pxg_screen_path + 'advD.png'))


@client.command(aliases=['adventurerc', 'ac', 'AC', 'aC'])
async def adventurerC(ctx):
    await ctx.send(file=discord.File(pxg_screen_path + 'advC.png'))


@client.command(aliases=['AdventurerB', 'ab', 'AB', 'aB'])
async def adventurerB(ctx):
    await ctx.send(file=discord.File(pxg_screen_path + 'advB.png'))


@client.command(aliases=['AdventurerA', 'adventurera', 'aa', 'AA', 'aA'])
async def adventurerA(ctx):
    sslist = 'advA1.png', 'advA2.png', 'advA3.png'
    for ss in sslist:
        await ctx.send(file=discord.File(pxg_screen_path + ss))


@client.command(aliases=['profesorE', 'profesore', 'professore', 'pe', 'pE'])
async def professorE(ctx):
    sslist = 'pE.png'
    await ctx.send(file=discord.File(pxg_screen_path + sslist))


@client.command(aliases=['profesorD', 'profesord', 'professord', 'pD', 'pd'])
async def professorD(ctx):
    sslist = 'pD1.png', 'pD2.png', 'pD3.png'
    for ss in sslist:
        await ctx.send(file=discord.File(pxg_screen_path + ss))


@client.command(aliases=['profesorC', 'professorc', 'profesorc', 'pc', 'pC'])
async def professorC(ctx):
    sslist = 'pC1.png', 'pC2.png', 'pC3.png'
    for ss in sslist:
        await ctx.send(file=discord.File(pxg_screen_path + ss))


@client.command(aliases=['profesorB', 'professorb', 'profesorb', 'pB', 'pb'])
async def professorB(ctx):
    sslist = 'pB1.png', 'pB2.png', 'pB3.png', 'pB4.png'
    for ss in sslist:
        await ctx.send(file=discord.File(pxg_screen_path + ss))


@client.command(aliases=['profesorA', 'profesora', 'professora', 'pa', 'pA'])
async def professorA(ctx):
    sslist = 'pA1.png', 'pA2.png', 'pA3.png', 'pA4.png', 'pA5'
    for ss in sslist:
        await ctx.send(file=discord.File(pxg_screen_path + ss))


@client.command(aliases=['stylistC', 'stylistc', 'stylistac', 'sc', 'sC'])
async def stylistaC(ctx):
    sslist = 'StylistaC1.png', 'StylistaC2.png', 'StylistaC3.png', 'StylistaC4.png', 'StylistaC5', 'StylistaC6', \
             'StylistaC7'
    for ss in sslist:
        await ctx.send(file=discord.File(pxg_screen_path + ss))


# count when your stamina will be full
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

#client.login(process.env.TOKEN)
client.run(os.getenv("token"))
