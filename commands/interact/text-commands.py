from discord.ext import commands

class text_commands():

    def __init__(self, bot):
        self.bot = bot

<<<<<<< HEAD
    @bot.command(pass_context=True)
    async def greeting(ctx):
        await ctx.send("Hello! :shake:")

    @bot.command(pass_context=True)
    async def rolldie(ctx):
        await ctx.send(random.randint(1,6))
=======
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
>>>>>>> b9698f88f0cbe673dae8531f58efbb4ffeb6215a

def setup(bot):
    bot.add_cog(text_commands(bot))
