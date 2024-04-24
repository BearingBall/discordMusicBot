import discord
from discord.ext import commands
from discord.ui import Button, View

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

            queueLen = await manager.registerPlayRequest(ctx, args)

            if (queueLen == 0):
                await self.voiceClient.disconnect()

        @self.bot.command(name="stop")
        async def stop(ctx):
            manager.stop()

        @self.bot.command(name="pause")
        async def pause(ctx):
            manager.pause()

        @self.bot.command(name="resume")
        async def resume(ctx):
            manager.resume()

        @self.bot.command(name="test")
        async def test(ctx):

            async def button_callback(interaction):
                await interaction.response.edit_message(content='Button clicked!', view=None)

            button = Button(custom_id='button1', label='WOW button!', style=discord.ButtonStyle.green)
            button.callback = button_callback

            await ctx.send('Hello World!', view=View(button))

    def run(self):
        self.bot.run(rs.RegisterService().GetToken())



    

