import discord
from discord.ext import commands
#from discord.voice_client import VoiceClient
import asyncio
import random
from datetime import datetime
from time import strftime

from commands.owner import admin

bot = commands.Bot(command_prefix='-')

extensions = ['commands.owner.admin', 'commands.interact.comms', 'commands.owner.standard', 'commands.help.help']

@bot.event
async def on_ready():
    print("Running on " + bot.user.name)
    print("With ID " + str(bot.user.id))

@bot.command(pass_context=True)
async def greeting(ctx):
    await bot.say("Hello! :shake:")

@bot.command(pass_context=True)
async def rolldie(ctx):
    await bot.say(random.randint(1,6))

@bot.command(pass_context=True)
async def timedate(ctx):
    await bot.say(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@bot.command(pass_context =True)
async def doashit(ctx):
    await bot.say(":poop:" * 100)

#@bot.command(pass_context = True)
#async def join(ctx):
#    channel = ctx.message.author.voice_channel
#    await bot.join_voice_channel(channel)

#@bot.command(pass_context = True)
#async def leave(ctx):
#    for x in bot.voice_clients:
#        if(x.server == ctx.message.server):
#            return await x.disconnect()


@bot.command(pass_context = True)
async def doggo(ctx):
    await bot.say("https://giphy.com/gifs/dog-shiba-inu-typing-mCRJDo24UvJMA")

@bot.command()
async def load(extension):
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print('Loaded {}'.format(extension))

        except Exception as e:
            print('{} cannot be loaded. [{}]'.format(extension, e))

@bot.command()
async def unload(extension):
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print('Unloaded {}'.format(extension))

        except Exception as e:
            print('{} cannot be loaded. [{}]'.format(extension, e))

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)

        except Exception as e:
            print('{} cannot be loaded. [{}]'.format(extension, e))





@bot.command(pass_context=True)
async def time(ctx):
    hour = int(datetime.now().strftime('%H'))
    minutes = int(datetime.now().strftime('%M'))

    if hour > 12:
        hour = hour - 12

    if minutes < 7:
        a = ' '
    elif minutes > 7 and minutes < 12:
        a = ' ten past '
    elif minutes > 13 and minutes < 22:
        a = ' quarter past '
    elif minutes > 23 and minutes < 42:
        a = ' half past '
    elif minutes > 43 and minutes < 47:
        a = ' quarter to '
        hour = hour + 1
    elif minutes > 48 and minutes < 55:
        a = ' ten to '
        hour = hour + 1
    else:
        a = ' '
        hour = hour + 1

    await bot.say("It is" + str(a) + str(hour))



bot.run("NDg0MzE5Mzk5NzE3ODk2MjEy.DmhzIA.ZK_oq9SCy3hHXGEQZnzCWoGVbRU")
