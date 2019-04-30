import discord
from discord.ext import commands
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Your Nan')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

class response(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_contex=True)
    async def talk(self, ctx, *, arg1):
        await ctx.send(chatbot.get_response(str(arg1)))

def setup(bot):
    bot.add_cog(response(bot))
