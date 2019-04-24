import discord
from discord.ext import commands
import asyncio

#overwrites the help function to make it more suited to the application
class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #adds this method to commands as a command
    @commands.group(pass_context = True)
    async def help(self, ctx):

        page = 1

        embed = discord.Embed(title = "Your Nan Help Page - Page " + str(page), color = discord.Colour(0x00FFFA))
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/258630960017309696/484431520669630477/images.png")
        embed.add_field(name = "-", value = "--------------------------", inline = True)
        embed.add_field(name = "-greeting", value = "Greets the user.\n", inline = True)
        embed.add_field(name = "-rolldie", value = "Generates a random die roll.\n", inline = False)
        embed.add_field(name = "-help", value = "Can give you help.\n", inline = True)
        embed.add_field(name = "-timedate", value = "Outputs the exact time and date.\n", inline = False)
        embed.add_field(name = "-doashit", value = " It's in the name.\n", inline = False)
        embed.add_field(name = "-time", value = "Gives the time.\n", inline = True)

        message = await ctx.send(embed = embed)
        await message.add_reaction(u"\u2B05")
        await message.add_reaction(u"\u27A1")

    @help.command(aliases=['page2', 'music'])
    async def musichelp(self, ctx):

        embed = discord.Embed(title = "Music-Help", description = "")





def setup(bot):
    bot.add_cog(help(bot))
