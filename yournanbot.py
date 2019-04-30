#legacy bot, last version compatible with windows
import discord
from discord.ext import commands
#from discord.voice_client import VoiceClient
import asyncio
import platform
import os
import time
import youtube_dl

print(os.getcwd())
bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

players = {}
try:
    f = open('key.txt', 'r')
except:
    f = open('key.rtf', 'r')
TOKEN = f.read()
TOKEN = TOKEN.strip()

extensions = ['commands.owner.admin', 'commands.interact.comms', 'commands.help.help', 'commands.interact.text-commands', 'commands.interact.times', 'commands.owner.priv', 'commands.owner.standard']

@bot.event
async def on_ready():
    game = discord.Game("type -help")
    await bot.change_presence(status=discord.Status.invisible, activity=game)
    print("Running on " + bot.user.name)
    print("With ID " + str(bot.user.id))

#@bot.event
#async def on_member_join():
#    ctx.send('Welcome', discord.Member)

@bot.command()
async def load(extension):
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print('Loaded {}'.format(extension))

        except Exception as e:
            print('{} cannot be loaded. [{}]'.format(extension, e))

@bot.command(pass_context = True)
async def move(ctx, a, b):
    for x in ctx.message.guild.members:
        if x.id == int(a):
            for c in ctx.message.guild.channels:
                if c.id == int(b):
                    channelafk = c
            try:
                await x.move_to(channelafk,reason=None)
            except:
                pass

@bot.command(pass_context = True)
async def play(ctx):
    #server = ctx.message.guild
    #voice_client = bot.guild_voice_client_in(server)
    ##player = await voice_client.creates_ytdl_player(url)
    #players[server.id] = player
    #player.start()
    channel = ctx.message.author.voice.channel
    voice = await channel.connect(timeout=60.0, reconnect=True)
    voice.play(discord.FFmpegPCMAudio('ringtone.mp3'), after=lambda e: print('done', e))

async def spamplayloop(ctx):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect(timeout=60.0, reconnect=True)
    voice.play(discord.FFmpegPCMAudio('ringtone.mp3'), after=lambda e: print('done', e))
    time.sleep(5)
    for x in bot.voice_clients:
        if(x.guild == ctx.message.guild):
            return await x.disconnect()

@bot.command(pass_context = True)
async def spamplay(ctx):
    #server = ctx.message.guild
    #voice_client = bot.guild_voice_client_in(server)
    #player = await voice_client.creates_ytdl_player(url)
    #players[server.id] = player
    #player.start()
    count = 0
    while count != 10:
        await spamplayloop(ctx)
        count = count + 1

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



bot.run(TOKEN)
