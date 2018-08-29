import discord
from discord.ext import commands
import asyncio
import random
from datetime import datetime
from time import strftime

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("Running on " + bot.user.name)
    print("With ID " + bot.user.id)

@bot.command(pass_context=True)
async def commandhelp(ctx):
    await bot.say("Available commands: \n greeting \n doashit \n rolldie \n timedate \n time")

@bot.command(pass_context=True)
async def greeting(ctx):
    await bot.say("Hello!")

@bot.command(pass_context=True)
async def rolldie(ctx):
    await bot.say(random.randint(1,6))

@bot.command(pass_context=True)
async def timedate(ctx):
    await bot.say(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@bot.command(pass_context =True)
async def doashit(ctx):
    await bot.say(":poop:" * 100)

@bot.command(pass_context=True)
async def time(ctx):
    hour = int(datetime.now().strftime('%H'))
    minutes = int(datetime.now().strftime('%M'))

    if hour > 12:
        hour = hour - 12

    if minutes > 7 and minutes < 12:
        a = ' ten past '
    elif minutes > 13 and minutes < 22:
        a = ' quarter past '
    elif minutes > 23 and minutes < 42:
        a = ' half past '
    elif minutes > 43 and minutes < 47:
        a = ' quarter to '
        hour = hour + 1
    elif minutes > 48 and minutes < 59:
        a = ' ten to '
        hour = hour + 1
    else:
        a = ''

    await bot.say("It is" + str(a) + str(hour))

bot.run("TOKEN")
