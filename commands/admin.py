from discord.ext import commands

class admin():

    def __init__(self, bot):
        self.bot = bot

    #adds this method to commands as a command
    @commands.command(pass_context = True)
    async def bothelp(ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title = "",
                             desc = "A pussy destroying mad lad. COMMANDS:",
                             colour = discord.Colour.yellow())
        embed.set_author(name = "Your Nan", icon_url = "https://cdn.discordapp.com/attachments/258630960017309696/484431520669630477/images.png")
        embed.add_field(name = "$greeting", value = "Says hello because you're a lonely fucker.\n", inline = True)
        embed.add_field(name = "$rolldie", value = "Generates a random die roll\n", inline = False)
        embed.add_field(name = "$commandhelp", value = "give you help\n", inline = True)
        embed.add_field(name = "$timedate", value = "Outputs the exact time and date.\n", inline = False)
        embed.add_field(name = "$doashit", value = " It's in the name.\n", inline = False)
        embed.add_field(name = "$time", value = "Gives the time.\n", inline = True)

        await bot.send_message(channel, embed = embed)

def setup(bot):
    bot.add_cog(admin(bot))
