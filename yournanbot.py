import discord
from discord.ext import commands
#from discord.voice_client import VoiceClient
import asyncio
import platform
import os

print(os.getcwd())
bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

players = {}
if platform.system() == 'Windows':
    f = open('key.txt', 'r')
else:
    f = open('key.rtf', 'r')
TOKEN = f.read()
TOKEN = TOKEN.strip()

extensions = ['commands.owner.admin', 'commands.interact.comms', 'commands.help.help', 'commands.interact.text-commands', 'commands.interact.times', 'commands.owner.priv', 'commands.owner.standard']

@bot.event
async def on_ready():
    print("Running on " + bot.user.name)
    print("With ID " + str(bot.user.id))

@bot.event
async def on_member_join():
    ctx.send('Welcome', discord.Member)

@bot.command()
async def load(extension):
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print('Loaded {}'.format(extension))

        except Exception as e:
            print('{} cannot be loaded. [{}]'.format(extension, e))

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
