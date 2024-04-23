import discord
from discord.ext import commands

from ..RegisterService import RegisterService as rs
from ..MusicCore.MusicManager import MusicManager
from ..MusicCore.MusicPlayers.DiscordMusicPlayer import DiscordMusicPlayer
from .botUtils import BotUtils

class MusicBot():
    def __init__(self, manager: MusicManager):
        self.manager = manager

        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=rs.RegisterService().GetPrefix(), intents=intents)
        self.name = rs.RegisterService().GetBotName()
        self.channel = None
        self.voiceClient = None

        @self.bot.event
        async def on_ready():
            print("Music bot available")

        @self.bot.event
        async def on_voice_state_update(member, before, after):
            if (member.name == self.name):
                self.channel = after.channel

        @self.bot.command(name="alive?")
        async def ping(ctx):
            await ctx.send("yeah...")

        @self.bot.command(name="play")
        async def play(ctx, args):

            print("Asked play command from", ctx.author)
            if (self.channel != ctx.author.voice.channel):
                self.voiceClient = await BotUtils.connectUserVoiceChannel(ctx)
                manager.setPlayer(DiscordMusicPlayer(self.voiceClient))
                print("Channel connected")

            await manager.registerPlayRequest(ctx, args)
            
    def run(self):
        self.bot.run(rs.RegisterService().GetToken())



    

