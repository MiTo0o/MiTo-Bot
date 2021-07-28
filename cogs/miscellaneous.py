import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):

        message = await ctx.send("🏓 Pong!")

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command(name="Banaynay")
    async def Banaynay(self, ctx):
        await ctx.send(file=discord.File('res/img/animoles/BaNayNay1.jpeg'))


def setup(bot):
    bot.add_cog(Misc(bot))
