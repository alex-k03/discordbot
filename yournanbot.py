import discord
from discord.ext import commands
from discord.ext import Bot
import asyncio
import time


bot = commands.bot(command.prefix='#')

#when the bot is ready this will run
@bot.event
async def on_ready():
    print("Running on", bot.user.name)
    print("With ID", bot.user.id)

bot.run("NDg0MzE5Mzk5NzE3ODk2MjEy.DmgSLw.JQMm6f6mFV4zydIKjimi7FgQq6I")
