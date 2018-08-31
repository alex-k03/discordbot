import discord
from discord.ext import commands
import asyncio

#overwrites the help function to make it more suited to the application

class help():

    #pagination, with index-1 based pages.
    def __init__(self):

        self.bot = bot

    @commands.command(pass_context = True)
    async def help(self, ctx):

        embed = discord.Embed(title = "",
                             desc = "A pussy destroying mad lad. COMMANDS:",
                             color = discord.Colour(0xFFFF00))
        embed.set_author(name = "Your Nan", icon_url = "https://cdn.discordapp.com/attachments/258630960017309696/484431520669630477/images.png")
        embed.add_field(name = "-greeting", value = "Says hello because you're a lonely fucker.\n", inline = True)
        embed.add_field(name = "-rolldie", value = "Generates a random die roll\n", inline = False)
        embed.add_field(name = "-bothelp", value = "give you help\n", inline = True)
        embed.add_field(name = "-timedate", value = "Outputs the exact time and date.\n", inline = False)
        embed.add_field(name = "-doashit", value = " It's in the name.\n", inline = False)
        embed.add_field(name = "-time", value = "Gives the time.\n", inline = True)
        await ctx.send(embed = embed)

        await msg.add_reaction(u"\u2B05")
        await msg.add_reaction(u"\u27A1")


def setup(bot):
    bot.agg_cog(help(bot))
