import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from discord_slash import SlashCommand

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print("{0.user} is ready to serve.".format(bot))
    await bot.change_presence(activity=discord.Game(name="/help"))


extensions = [
    "cogs.miscellaneous",
    "cogs.soundboard",
    "cogs.img_manip",
    "cogs.reaction",
    "cogs.sending_img"
]
if __name__ == "__main__":
    for ext in extensions:
        bot.load_extension(ext)

bot.run(TOKEN)
