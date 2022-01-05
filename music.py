from random import choice
import discord
from discord.ext import commands, tasks
import yt_dlp
import os

client = commands.bot
status = ["Studying!", "HOW LONG IS THIS GOING TO TAKE!"]


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
             await ctx.send(f"**joining {voice_channel}**")
        else:
             await ctx.voice_client.move_to(voice_channel)
             await ctx.send("**we movin to {voice_channel}**")
    
    @commands.command() #commands to make the bot disconnect from a discord voice channel
    async def leave(self, ctx):
        voice_channel = ctx.author.voice.channel
        await ctx.voice_client.disconnect()
        await ctx.send(f"**Adios {voice_channel}**")

    @commands.command() #commands to make the bot play music 
    async def play(self, ctx, url):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command") 
            return

        YDL_OPTION = {'format': "bestaudio",'postprocessors': [{ 'key':"FFmpegExtractAudio", 'preferredcodec': "mp3", 'preferredquality' : "192"}],}
        vc = ctx.voice_client

        with yt_dlp.YoutubeDL(YDL_OPTION) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")        
        vc.play(discord.FFmpegPCMAudio("song.mp3"))
        await ctx.send(f"**now playing** `{url}`")
                        
    @commands.command() #commands to make the bot pause the music
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused music")
    
    @commands.command() #commands to make the bot resume the music
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resume music")

    @commands.command() #commands to make the bot stop the music
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.send("Stopped music")

    @tasks.loop(seconds=20)
    async def change_status():
        await client.change_presence(activity=discord.Game(choice(status)))
        
def setup(client):
    client.add_cog((music)(client))