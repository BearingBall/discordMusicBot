import validators
import ffmpeg
import discord
import operator
import os
from difflib import SequenceMatcher
from pytube import YouTube
from pytube import Search

from ..AudioTrack import AudioTrack
from .IMusicRequestHandler import IMusicRequestHandler
from ...PathManager.PathManager import PathMannager

class YouTubeMusicHandler(IMusicRequestHandler):
    async def getSound(self, arguments) -> AudioTrack:
        if (validators.url(arguments)):
            return self.getSoundByLink(arguments)
        else:
            return self.getSoundByName(arguments)
        
    def getSoundByLink(self, link: str) -> AudioTrack:
        (name, path) = self.download(link)
        return AudioTrack(path, name)
        
    def getSoundByName(self, name: str) -> AudioTrack:
        search = Search(name)
        url = search.results[0].watch_url
        (name, path) = self.download(url)
        return AudioTrack(path, name)

    def download(self, link):
        youtubeObject = YouTube(link)
        title = youtubeObject.title
        audio = youtubeObject.streams.get_audio_only()

        downloadPath = "./" + PathMannager().GetDownloadedMusicFolderPath()

        try:
            outputPath = audio.download(downloadPath)
        except:
            print("YouTube: downloading error")
        print("YouTube: Download is completed")

        return (title, outputPath)
