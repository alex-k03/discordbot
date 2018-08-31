from discord.ext import commands
#this is for the bot to make communications with the user
class comms():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        if ctx.message.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect(timeout=60.0, reconnect=True)

    @commands.command(pass_contex=True)
    async def leave(self, ctx):
        for x in self.bot.voice_clients:
            if(x.guild == ctx.message.guild):
                return await x.disconnect()

def setup(bot):
    bot.add_cog(comms(bot))
