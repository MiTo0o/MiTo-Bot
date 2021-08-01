import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class SendImg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="fc1")
    async def fc1(self, ctx: SlashContext):
        await ctx.send(file=discord.File('res/img/blursed/face_swap_1.jpeg'))

    @cog_ext.cog_slash(name="catsmile")
    async def catsmile(self, ctx: SlashContext):
        await ctx.send(file=discord.File('res/gifs/cat_smile_nod.gif'))

    @cog_ext.cog_subcommand(name="turt")
    async def turt(self, ctx: SlashContext):
        await ctx.send(file=discord.File('res/img/blursed/turtle_in_horse_nose.jpeg'))

    @cog_ext.cog_subcommand(name="confusion")
    async def confusion(self, ctx: SlashContext):
        await ctx.send(file=discord.File('res/img/reee_action/confusion_1.jpeg'))


def setup(bot):
    bot.add_cog(SendImg(bot))
