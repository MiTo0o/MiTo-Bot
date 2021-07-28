import discord
from discord.ext import commands
import time
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


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

    @commands.command(name="thic_boi")
    async def thic_boi(self, ctx):
        voice_channel = ctx.author.voice.channel
        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('res/audio/DAM_BOI_HE_THICC.mp3'))
            while vc.is_playing():
                time.sleep(.1)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()

    @commands.command(name="sheesh")
    async def sheesh(self, ctx):
        voice_channel = ctx.author.voice.channel
        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('res/audio/old_man_sheesh.mp3'))
            while vc.is_playing():
                time.sleep(.1)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()

    @commands.command(name="Banaynay")
    async def Banaynay(self, ctx):
        await ctx.send(file=discord.File('res/img/animoles/BaNayNay1.jpeg'))

    @commands.command(name="sb")
    async def sb(self, ctx, *, user: discord.Member = None):
        if not user:
            user = ctx.author
        response = requests.get(user.avatar_url)
        url = Image.open(BytesIO(response.content)).convert('RGBA')
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
                text_img.paste(url, (0, 0), mask=url)
                frames.append(text_img)

            frames[0].save('out.gif',
                           save_all=True,
                           append_images=frames[1:],
                           duration=100,
                           loop=0)
            await ctx.send(file=discord.File('out.gif'))


def setup(bot):
    bot.add_cog(Misc(bot))
