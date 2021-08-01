import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="Ping")
    async def ping(self, ctx):
        await ctx.send("🏓 Pong!")


def setup(bot):
    bot.add_cog(Misc(bot))
