import discord
from discord.ext import commands
#from discord.voice_client import VoiceClient
import asyncio
import os

bot = commands.Bot(command_prefix='-')

players = {}

if os.system == 'windows':
    my_file = open("..\\key.txt", "r")
else:
    print("macOS")
    my_file = open("..\\key.rtf", "r")
TOKEN = my_file.read()
my_file.close()

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
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.creates_ytdl_player(url)
    players[server.id] = player

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
