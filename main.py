import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import youtube_dl

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

extensions = [
    "cogs.miscellaneous",
    "cogs.soundboard",
    "cogs.img_manip"
]
if __name__ == "__main__":
    for ext in extensions:
        bot.load_extension(ext)
bot.run(TOKEN)
