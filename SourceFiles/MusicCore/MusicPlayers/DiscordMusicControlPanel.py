from .IMusicPlayer import IMusicPlayer
from asyncio import sleep
import discord
from discord.partial_emoji import PartialEmoji
from discord.ext import commands
from discord.ui import Button, View, Item

class DiscordMusicControlPanel():
    def __init__(self, player: IMusicPlayer):
        self.player = player
        self.message = None

        async def pauseCallback(interaction: discord.Interaction):
            self.player.pause()
            await self.drawView(self.ctx)
        self.pauseButton = Button(custom_id='pause', label="||", style=discord.ButtonStyle.blurple)
        self.pauseButton.callback = pauseCallback


        async def resumeCallback(interaction: discord.Interaction):
            self.player.resume()
            await self.drawView(self.ctx)
        self.resumeButton = Button(custom_id='resume', label=">", style=discord.ButtonStyle.blurple)
        self.resumeButton.callback = resumeCallback


        async def prevCallback(interaction: discord.Interaction):
            self.player.currentTrackIdx = max([0, self.player.currentTrackIdx - 2])
            self.player.voiceClient.stop()
            await self.drawView(self.ctx)
        self.prevButton = Button(custom_id='prev', label="<<", style=discord.ButtonStyle.blurple)
        self.prevButton.callback = prevCallback


        async def nextCallback(interaction: discord.Interaction):
            self.player.voiceClient.stop()
            await self.drawView(self.ctx)
        self.nextButton = Button(custom_id='next', label=">>", style=discord.ButtonStyle.blurple)
        self.nextButton.callback = nextCallback


        async def stopCallback(interaction: discord.Interaction):
            self.player.stop()
            self.player.voiceClient.stop()
            await self.drawView(self.ctx)
        self.stopButton = Button(custom_id='stop', label="x", style=discord.ButtonStyle.blurple)
        self.stopButton.callback = stopCallback


    async def drawView(self, ctx):
        if (self.message != None):
            await self.message.delete()

        self.ctx = ctx
        
        view = View()
        view.add_item(self.prevButton)

        if (self.player.isPlaying()):
            view.add_item(self.pauseButton)
        else:
            view.add_item(self.resumeButton)

        view.add_item(self.stopButton)
        view.add_item(self.nextButton)

        nameList = self.player.getTrackNameList()
        idx = self.player.getCurrentTrackIdx()

        if (idx == -1 or idx >= len(nameList)):
            self.message = None
            return
        
        nameList[idx] = "**->" + nameList[idx] + "**"

        for i in range(len(nameList)):
            if (i != idx):
                nameList[i] = "" + nameList[i]
     
        message_text = '\n'.join(nameList)

        self.message = await ctx.send(message_text, view=view)


