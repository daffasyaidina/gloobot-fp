import discord
from discord.ext import commands
import music

cogs = [music]


client = commands.Bot(command_prefix="-", intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

TOKEN = "OTIzOTMxMjc1MTQyNzg3MDcy.YcXMDQ.0fDCXX3zhsNg4uIMT9uYFVzCTDE"
client.run(TOKEN)
 
