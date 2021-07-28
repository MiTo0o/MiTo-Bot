import discord
from discord.ext import commands
import time


class Soundboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(name="fantastic")
    async def fantastic(self, ctx):
        voice_channel = ctx.author.voice.channel
        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('res/audio/IT_IS_FANTASTIC.mp3'))
            while vc.is_playing():
                time.sleep(.1)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Soundboard(bot))
