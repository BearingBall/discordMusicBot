import discord
from discord.ext import commands

from ..RegisterService import RegisterService as rs
from ..MusicCore import IMusicRequestHandler
from .botUtils import BotUtils

from asyncio import sleep

class MusicBot():
    def __init__(self, handler: IMusicRequestHandler):
        self.handler = handler

        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=rs.RegisterService().GetPrefix(), intents=intents)

        @self.bot.event
        async def on_ready():
            print("Music bot available")

        @self.bot.command(name="alive?")
        async def ping(ctx):
            await ctx.send("yeah...")

        @self.bot.command(name="play")
        async def play(ctx, args):

            print("Asked play command from", ctx.author)
            voiceClient = await BotUtils.connectUserVoiceChannel(ctx)
            print("Connecting success")

            audio = await handler.getSound(args)

            if (audio is not None):
                voiceClient.play(audio)

                while voiceClient.is_playing():
                    await sleep(1)

            else:
                print("Audio handler failure")

            print("Disconnecting...")
            await voiceClient.disconnect()
            
    def run(self):
        self.bot.run(rs.RegisterService().GetToken())



    

