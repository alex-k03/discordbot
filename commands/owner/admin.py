import discord
from discord.ext import commands
import discord

class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.Member):
        if ctx.message.author.guild_permissions.kick_members or ctx.message.author.guild_permissions.administrator:
            await ctx.message.guild.kick(user)
        else:
            await ctx.send("You don't have permissions you prick")

def setup(bot):
    bot.add_cog(admin(bot))
