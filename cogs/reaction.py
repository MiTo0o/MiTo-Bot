import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
import random

shook = ["cat_shook.jpeg",
         "dog_shock_1.gif",
         "dog_shock_2.gif",
         "dog_shock_3.gif",
         "dog_shock_4.gif",
         "dog_shock_5.gif",
         "dog_shock_6.gif",
         "dog_you_what.gif",
         ]


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

    @cog_ext.cog_slash(name="shook")
    #    options=[
    #        create_option(
    #            name="random",
    #            description="random gif/pic",
    #        )
    #    ])
    async def shook(self, ctx: SlashContext):
        await ctx.message.delete()
        pic_gif = "res/img/reee_action/" + random.choice(shook)
        if ctx.message.reference is not None:
            message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        # reply to a specific message with its id
            print(pic_gif)
            await message.reply(file=discord.File(pic_gif))
        else:
            print(pic_gif)
            await ctx.send(file=discord.File(pic_gif))


def setup(bot):
    bot.add_cog(Reaction(bot))
