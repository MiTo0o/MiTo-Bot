import sys
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("{0.user} is ready to serve.".format(bot))
    await bot.change_presence(activity=discord.Game(name="/help"))

bot.run("ODY1NzE3OTc4NTk5MTI5MTI5.YPIEsg.AidnV2UpDZffgU9nwLz1br4CghE")


print(sys.version)
