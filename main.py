from random import choice
import discord 
from discord.ext import commands, tasks

from commands_cog import commands_cog #importing the cog

client = commands.Bot(command_prefix="-", intents = discord.Intents.all()) #initiate the bot command prefix to "-" and letting the user to use every commands
status = ["Studying!", "HOW LONG IS THIS GOING TO TAKE!"] #sets of status

client.add_cog(commands_cog(client)) #registering the class with the Bot

@client.event #when the bot is online it will activate the change_status function and print out "Bot is online"
async def on_ready():
    change_status.start()
    print("Bot is online!")

@tasks.loop(seconds=20) #changes the status the bot every 20 seconds by random
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
   
TOKEN = "couldn't be posted publically :/" 
client.run(TOKEN)#the token is used for connecting the Bot (it couldn't be posted publically since token are basically a password for the bot account) 