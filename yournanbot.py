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

@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)

@bot.command(pass_context = True)
async def leave(ctx):
    for x in bot.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()


@bot.command(pass_context = True)
async def doggo(ctx):
    await bot.say("https://giphy.com/gifs/dog-shiba-inu-typing-mCRJDo24UvJMA")


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

@bot.command(pass_context=True)
async def bothelp(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(title = "",
                         desc = "A pussy destroying mad lad. COMMANDS:",
                         colour = discord.Colour.red())
    embed.set_author(name = "Your Nan", icon_url = "https://cdn.discordapp.com/attachments/258630960017309696/484431520669630477/images.png")
    embed.add_field(name = "- greeting", value = "Says hello because you're a lonely fucker.\n", inline = True)
    embed.add_field(name = "- rolldie", value = "Generates a random die roll\n", inline = False)
    embed.add_field(name = "- commandhelp", value = "give you help\n", inline = True)
    embed.add_field(name = "- timedate", value = "Outputs the exact time and date.\n", inline = False)
    embed.add_field(name = "- doashit", value = " It's in the name.\n", inline = False)
    embed.add_field(name = "- time", value = "Gives the time.\n", inline = True)

    await bot.send_message(channel, embed = embed)

bot.run("NDg0MzE5Mzk5NzE3ODk2MjEy.DmhzIA.ZK_oq9SCy3hHXGEQZnzCWoGVbRU")
