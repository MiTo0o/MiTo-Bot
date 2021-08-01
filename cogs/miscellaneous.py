import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="Ping")
    async def ping(self, ctx):
        await ctx.send("🏓 Pong!")

    @cog_ext.cog_slash(name="BaNayNay")
    async def _BaNayNay(self, ctx: SlashContext):
        await ctx.send(file=discord.File('res/img/animoles/BaNayNay1.jpeg'))


def setup(bot):
    bot.add_cog(Misc(bot))
