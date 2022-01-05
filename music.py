import discord
from discord.ext import commands
import youtube_dl


class music(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command() #commands to make the bot join a discord voice channel
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Bro, you're not in the channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
             await voice_channel.connect()
             await ctx.send("wait up holmes, joining the channel")
        else:
             await ctx.voice_client.move_to(voice_channel)
             await ctx.send("we movin")
    
    @commands.command() #commands to make the bot disconnect from a discord voice channel
    async def leave(self, ctx): 
        await ctx.voice_client.disconnect()
        await ctx.send("Adios")

    @commands.command() #commands to make the bot play music 
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': 'vn'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download = False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS) #string to play audio
            vc.play(source) 

    @commands.command() #commands to make the bot pause the music
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused music")
    
    @commands.command() #commands to make the bot resume the music
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resume music")


def setup(client):
    client.add_cog((music)(client))
