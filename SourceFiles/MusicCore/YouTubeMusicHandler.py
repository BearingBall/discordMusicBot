import validators
import ffmpeg
import discord
import operator
import os
from difflib import SequenceMatcher
from pytube import YouTube

from .IMusicRequestHandler import IMusicRequestHandler

class YouTubeMusicHandler(IMusicRequestHandler):
    async def getSound(self, arguments):
        if (validators.url(arguments)):
            return self.getSoundByLink(arguments)
        else:
            return self.getSoundByName(arguments)
        
    def getSoundByLink(self, link: str):
        filePath = self.download(link)
        audio = discord.FFmpegPCMAudio(executable= "./ExternalExe/ffmpeg.exe", source= filePath)
        return audio
        
    def getSoundByName(self, name: str):
        return None

    def download(self, link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_audio_only()

        downloadPath = "./DownloadedFiles"

        try:
            outputPath = youtubeObject.download(downloadPath)
        except:
            print("YouTube: downloading error")
        print("YouTube: Download is completed")

        return outputPath
