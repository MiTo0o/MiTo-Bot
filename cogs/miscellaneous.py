import discord
from discord.ext import commands
import time
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import PIL


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):

        message = await ctx.send("🏓 Pong!")

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command(name="Banaynay")
    async def Banaynay(self, ctx):
        await ctx.send(file=discord.File('res/img/animoles/BaNayNay1.jpeg'))

    @commands.command(name="sb")
    async def sb(self, ctx, *, user: discord.Member = None):
        if not user:
            user = ctx.author
        response = requests.get(user.avatar_url)
        url = Image.open(BytesIO(response.content)).convert('RGBA')
        url.thumbnail([200, 200], PIL.Image.ANTIALIAS)
        # if not user:
        #     user = ctx.author
        # if user.is_avatar_animated():
        #     url = user.avatar_url_as(format="gif")
        # if not user.is_avatar_animated():
        #     url = user.avatar_url_as(static_format="png")

        gif_file = "res/gifs/salt_bae_loop.gif"
        salt_bae = Image.open(gif_file, 'r')

        if salt_bae.is_animated:
            frames = []

            for num in range(salt_bae.n_frames):
                salt_bae.seek(num)
                text_img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
                text_img.paste(salt_bae, (0, 0))
                text_img.paste(url, (65, 312), mask=url)
                frames.append(text_img)

            frames[0].save('out.gif',
                           save_all=True,
                           append_images=frames[1:],
                           duration=100,
                           loop=0)
            await ctx.send(file=discord.File('out.gif'))


def setup(bot):
    bot.add_cog(Misc(bot))
