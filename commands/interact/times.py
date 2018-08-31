from discord.ext import commands
import discord
from datetime import datetime
from time import strftime

class time():

    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def timedate(self, ctx):
        await ctx.send(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    @bot.command(pass_context=True)
    async def time(self, ctx):
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

        await ctx.send("It is" + str(a) + str(hour))

def setup(bot):
    bot.add_cog(time(bot))
