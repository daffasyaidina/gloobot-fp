from random import choice
import discord
from discord.ext import commands
import yt_dlp
import os


YDL_OPTION = {
        'format': "bestaudio",
        'postprocessors': [{ 
        'key':"FFmpegExtractAudio", 
        'preferredcodec': "mp3",
         'preferredquality' : "192"}],
         } #the music format

class commands_cog(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(name = "join", help = "This command makes the gloobot join a channel") #commands to make the bot join a discord voice channel
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Bro, you're not in the channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
             await voice_channel.connect()
             await ctx.send(f"**joining** `{voice_channel}`")
        else:
             await ctx.voice_client.move_to(voice_channel)
             await ctx.send(f"**we movin to** `{voice_channel}`")
    
    @commands.command(name = "leave", help = "This command makes gloobot to leave the channel") #commands to make the bot disconnect from a discord voice channel
    async def leave(self, ctx):
        voice_channel = ctx.author.voice.channel
        await ctx.voice_client.disconnect()
        await ctx.send(f"**Adios** `{voice_channel}`")

    @commands.command(name = "play" , help = "to use this command type -play *url*") #commands to make the bot play music 
    async def play(self, ctx, url):
        song_there = os.path.isfile("song.mp3") 
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError: #since the Bot doesn't have queue system the user need to wait for the music to finish or use the stop command
            await ctx.send("Wait for the current playing music to end or use the 'stop' command") 
            return

        vc = ctx.voice_client

        with yt_dlp.YoutubeDL(YDL_OPTION) as ydl: #downloading the music from youtube to the local machine
            ydl.download([url])
        for file in os.listdir("./"): #changes the music file name to "song.mp3"
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
                source = discord.FFmpegPCMAudio("song.mp3")      
        vc.play(source)
        await ctx.send(f"**now playing** `{url}`")
                      
    @commands.command(name = "pause", help = "This command pause the music gloobot is playing") #commands to make the bot pause the music
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused music")
 
    @commands.command(name = "resume", help = "This command resumed the song that are being paused") #commands to make the bot resume the music
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resume music")

    @commands.command(name = "stop", help = "stop the music that is playing") #commands to make the bot stop the music
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.send("Stopped music")

    @commands.command(name = "happy", help = "use this command to send a happy gif") #the command will send an happy gif :)
    async def happy(self, ctx):
        gif = [
        "https://tenor.com/view/yay-anime-girl-kawaii-gif-18081573",
        "https://tenor.com/view/black-clover-anime-guy-chico-asta-gif-19791391",
        "https://tenor.com/view/anime-excited-happy-smile-gif-15060821",
        "https://tenor.com/view/adachi-anime-happy-happy-gif-19233583",
        "https://tenor.com/view/anime-happy-anime-excited-gif-19679255",
        "https://tenor.com/view/anime-yay-happy-excited-yeah-gif-9528804",
        "https://tenor.com/view/anime-happy-excited-gif-13451198",
        "https://tenor.com/view/chika-chika-dance-anime-anime-dance-dance-gif-13973731",
        "https://tenor.com/view/chi-chis-sweet-home-comfy-kitty-cute-gif-16140552",
        "https://tenor.com/view/anime-happy-cute-excited-gif-12057651",
        "https://tenor.com/view/happy-japanese-anime-excited-gif-9596035",
        "https://tenor.com/view/komi-komi-san-komi-interested-komi-neko-mimi-komi-cat-ear-gif-22007033",
        "https://tenor.com/view/komi-san-komi-shouko-komi-shouko-komi-cant-communicate-gif-21525381",
        ]
        await ctx.send("`someone is feeling good`")
        await ctx.send(choice(gif))

    @commands.command(name = "sleepy" , help = "use this command if you feel sleepy") #sleepy gif cause i need some sleep
    async def sleepy(self, ctx):
        gif = [
        "https://tenor.com/view/sleepy-sleep-anime-anime-sleep-anime-sleepy-gif-24142121",
        "https://tenor.com/view/willcore-kon-anime-girl-sleepy-gif-24035077",
        "https://tenor.com/view/sleepy-nichijou-tired-yawn-wipe-eyes-gif-16309858",
        "https://tenor.com/view/kanna-kawai-tired-sleep-sleepy-gif-15961742",
        "https://tenor.com/view/tired-anime-kawaii-blue-hair-sigh-gif-17714309",
        "https://tenor.com/view/yawn-tired-anime-manga-japanese-manga-gif-9525859",
        "https://tenor.com/view/sleeping-anime-my-hero-academia-eraserhead-shota-aizawa-gif-16604988",
        "https://tenor.com/view/tired-kon-anime-yawn-sleepy-gif-17415905",
        "https://tenor.com/view/gintoki-no-sleep-sleepy-gif-12592776",
        "https://tenor.com/view/anime-girl-sleepy-gif-22569001",
        "https://tenor.com/view/umaru-sleeping-sleep-anime-gif-12007584",
        "https://tenor.com/view/nadeshiko-laid-back-camp-anime-sleepy-gif-12003890"
        ]
        responses = ["***YAWN*** i need to slee-", "*strech-strech*"]
        await ctx.send(choice(responses))
        await ctx.send(choice(gif))
    
    @commands.command(name = "sad", help = "sends a sad gif T_T") #sends an sad anime gif T_T
    async def sad(self, ctx):
        gif = [
        "https://tenor.com/view/anime-crying-sad-gif-14210687",
        "https://tenor.com/view/crying-cute-anime-sad-tears-gif-16038248",
        "https://tenor.com/view/sorry-crying-anime-sad-gif-15171171",
        "https://tenor.com/view/trash-disappointed-no-sad-bye-gif-5005980",
        "https://tenor.com/view/anime-cry-sad-gif-14080503",
        "https://tenor.com/view/anime-girl-sad-cry-tears-gif-17100832",
        "https://tenor.com/view/llorar1-cry-sad-tears-anime-gif-5648908",
        "https://tenor.com/view/anime-gif-19105479",
        "https://tenor.com/view/aqua-aqua-crying-crying-gif-21481711",
        "https://tenor.com/view/deku-cry-tears-anime-izuku-midoriya-gif-14926648",
        "https://tenor.com/view/hunter-x-hunter-gon-freecs-sad-crying-tears-gif-16729297",
        "https://tenor.com/view/sorry-crying-anime-sad-the-demon-girl-next-door-gif-15005984",
        "https://tenor.com/view/anime-cry-wataten-crying-gif-13356071",
        "https://tenor.com/view/anime-hitori-bocchi-no-marumaru-seikatsu-crying-sad-gif-14016926",
        "https://tenor.com/view/komi-komi-san-komi-cry-komi-san-cry-gif-24002547",
        "https://tenor.com/view/anime-sad-anime-pout-anime-sorry-horimya-hori-gif-20710638",
        ]
        responses = ["someone is not feeling so good...","**pat** *there there...*"]
        await ctx.send(choice(responses))
        await ctx.send(choice(gif))

    @commands.command(name = "pout" , help = "send a pouting gif")
    async def pout(self, ctx):
        gif = [
        "https://tenor.com/view/komi-komi-san-pout-anime-anime-pout-gif-23453143",
        "https://tenor.com/view/anime-raphtalia-mad-pouty-gif-16985978",
        "https://tenor.com/view/pout-anime-pout-sad-cute-gif-17524621",
        "https://tenor.com/view/pout-hmph-anime-girl-kawaii-gif-17549065",
        "https://tenor.com/view/anime-angry-mad-gif-14108774",
        "https://tenor.com/view/wataten-watashi-ni-tenshi-ga-maiorita-pout-hinata-anime-gif-16058457",
        "https://tenor.com/view/nagatoro-hayase-nagatoro-nagatoro-pout-pout-pouting-gif-22127015",
        "https://tenor.com/view/anime-pouting-grumpy-gif-13451362",
        "https://tenor.com/view/raphtalia-anime-pouting-gif-14210688",
        "https://tenor.com/view/anime-gif-12942766",
        "https://tenor.com/view/answer-me-the-quintessential-quintuplets-5toubun-no-hanayome-gif-21661590",
        ]
        await ctx.send("oh uh someone is mad...")
        await ctx.send(choice(gif))
    
    

