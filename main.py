
from discord_slash import cog_ext, SlashContext
from discord import Embed
import discord
from discord import CategoryChannel, Client, Intents
from discord.utils import get
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix=".")
# slash = SlashCommand(bot)


@bot.event
async def on_ready():
    print("{0.user} is ready to serve.".format(bot))
    await bot.change_presence(activity=discord.Game(name="/help"))


@bot.command()
async def q5(ctx):
    await ctx.send("@here QUEUE STARTING IN 5 MINUTES")


bot.run(TOKEN)
