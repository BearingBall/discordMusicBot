from .IMusicPlayer import IMusicPlayer
from .DiscordMusicControlPanel import DiscordMusicControlPanel
from asyncio import sleep
import discord
from discord.partial_emoji import PartialEmoji
from discord.ext import commands
from discord.ui import Button, View

class DiscordMusicPlayer(IMusicPlayer):
    def __init__(self, ctx):
        self.voiceClient = None
        self.musicQueue = []
        self.currentTrackIdx = 0
        self.controlPanel = DiscordMusicControlPanel(self)

    async def __updateVoiceClient(self, ctx):
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            return

        voice_channel = ctx.author.voice.channel
        if (ctx.voice_client is None):
            self.voiceClient = await voice_channel.connect()
        elif (voice_channel.id != self.voiceClient.channel.id):
            await ctx.voice_client.move_to(voice_channel)
            self.voiceClient = ctx.voice_client

    async def play(self, ctx, audio):
        await self.__updateVoiceClient(ctx)
        self.musicQueue.append(audio)

        if (self.voiceClient is None):
            return
        
        if (not self.isPlaying()):
            self.__playLoop()

        await self.controlPanel.drawView(ctx)

    def __playLoop(self, exception = None):        
        if (self.currentTrackIdx < len(self.musicQueue)):
            track = self.musicQueue[self.currentTrackIdx]
            self.currentTrackIdx = self.currentTrackIdx + 1
            self.voiceClient.play(track.getFFmpeg(), after = self.__playLoop)
            return

        self.currentTrackIdx = 0
        self.musicQueue.clear()

    def isPlaying(self):
        if (self.voiceClient == None):
            return False

        return self.voiceClient.is_playing()

    def pause(self):
        self.voiceClient.pause()

    def resume(self):
        self.voiceClient.resume()

    def stop(self):
        self.currentTrackIdx = 0
        self.musicQueue = []
        self.voiceClient.stop()

    def getTrackNameList(self):
        return [track.getName() for track in self.musicQueue]
    
    def getCurrentTrackIdx(self):
        return self.currentTrackIdx - 1
