import sys
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("{0.user} is ready to serve.".format(bot))
    await bot.change_presence(activity=discord.Game(name="/help"))

bot.run(TOKEN)


print(sys.version)
