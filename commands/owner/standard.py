from discord.ext import commands
import discord

class standard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(standard(bot))
