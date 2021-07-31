import discord
from discord.ext import commands


class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command("wheeze")
    async def wheeze(self, ctx):
        name = ctx.message.author.display_name
        await ctx.message.delete()
        if ctx.message.reference is not None:
            message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            # reply to a specific message with its id
            await message.reply(name)
        else:
            await ctx.send(name)


def setup(bot):
    bot.add_cog(Reaction(bot))
