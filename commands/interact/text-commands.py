from discord.ext import commands

class text-commands():

    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def greeting(ctx):
        await bot.say("Hello! :shake:")

    @bot.command(pass_context=True)
    async def rolldie(ctx):
        await bot.say(random.randint(1,6))

def setup(bot):
    bot.add_cog(text-commands(bot))