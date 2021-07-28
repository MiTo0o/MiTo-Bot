import discord
from discord.ext import commands
import time


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
    async def sb(self, ctx):
        await ctx.send(file=discord.File('res/img/animoles/BaNayNay1.jpeg'))


def setup(bot):
    bot.add_cog(Misc(bot))
