from discord.ext import commands

#this is for the bot to make communications with the user
class comms():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await bot.join_voice_channel(channel)

    @commands.command(pass_context = True)
    async def leave(ctx):
        for x in bot.voice_clients:
            if(x.server == ctx.message.server):
                return await x.disconnect()


def setup(bot):
    bot.add_cog(comms(bot))
