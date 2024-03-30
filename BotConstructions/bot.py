import discord
from discord.ext import commands
import RegisterService.RegisterService as rs

class MusicBot():
    def __init__(self):

        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=rs.RegisterService().GetPrefix(), intents=intents)

        @self.bot.event
        async def on_ready():
            print("Music bot available")

        @self.bot.command(name="ping")
        async def ping(ctx):
            await ctx.send("pong")
        
    def run(self):
        self.bot.run(rs.RegisterService().GetToken())



    

