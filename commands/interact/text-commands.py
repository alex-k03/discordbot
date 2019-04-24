from discord.ext import commands
import random

class text_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def greeting(self, ctx):
        await ctx.send("Hello! :shake:")

    @commands.command(pass_context=True)
    async def rolldie(self, ctx):
        await ctx.send(random.randint(1,6))

    @commands.command(pass_context =True)
    async def doashit(self, ctx):
        await ctx.send(":poop:" * 100)

    @commands.command(pass_context = True)
    async def doggo(self, ctx):
        await ctx.send("https://giphy.com/gifs/dog-shiba-inu-typing-mCRJDo24UvJMA")

def setup(bot):
    bot.add_cog(text_commands(bot))
