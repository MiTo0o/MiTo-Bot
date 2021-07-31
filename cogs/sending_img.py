import discord
from discord.ext import commands


class SendImg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fc1")
    async def fc1(self, ctx):
        await ctx.send(file=discord.File('res/img/blursed/face_swap1.jpeg'))

    @commands.command(name="catsmile")
    async def catsmile(self, ctx):
        await ctx.send(file=discord.File('res/gifs/cat_smile_nod.gif'))

    @commands.command(name="turt")
    async def turt(self, ctx):
        await ctx.send(file=discord.File('res/img/blursed/turtle_in_horse_nose.jpeg'))

    @commands.command(name="confusion")
    async def confusion(self, ctx):
        await ctx.send(file=discord.File('res/img/reee_action/confusion_1.jped'))


def setup(bot):
    bot.add_cog(SendImg(bot))
