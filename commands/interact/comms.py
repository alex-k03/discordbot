from discord.ext import commands
import time
#this is for the bot to make communications with the user
class comms(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect(timeout=60.0, reconnect=True)
        return channel

    @commands.command(pass_contex=True)
    async def leave(self, ctx):
        for x in self.bot.voice_clients:
            if(x.guild == ctx.message.guild):
                return await x.disconnect()

    @commands.command(pass_contex=True)
    async def spam(self, ctx, n):
        channel = ctx.message.author.voice.channel
        count = 0
        n = int(n)
        if n > 15:
            n = 15
        if n < 1:
            n = 1
        while count < n:
            await channel.connect(timeout=60.0, reconnect=True)
            for x in self.bot.voice_clients:
                if(x.guild == ctx.message.guild):
                    await x.disconnect()
            time.sleep(0.3)
            count += 1

def setup(bot):
    bot.add_cog(comms(bot))
