import validators
import ffmpeg
import discord
import operator
import os
from difflib import SequenceMatcher

from .IMusicRequestHandler import IMusicRequestHandler

class LocalStorageMusicHandler(IMusicRequestHandler):
    async def getSound(self, arguments):
        if (validators.url(arguments)):
            print("LocalStorage: link does not supported")
            return None
        else:
            return self.getSoundByName(arguments)

    def getSoundByName(self, name: str):
        localMusicPath = "./LocalMusic"

        localMusicList = os.listdir(localMusicPath)

        musicSimilarityRating = [(SequenceMatcher(None, musicName, name).ratio(), musicName) for musicName in localMusicList]
        musicSimilarityRating.sort(key=operator.itemgetter(0), reverse=True)
        
        if (musicSimilarityRating[0][0] < 0.5 and (musicSimilarityRating[0][0] - musicSimilarityRating[1][0]) < 0.15):
            print("File not found")
            return None
        
        trackPath = os.path.join(localMusicPath, musicSimilarityRating[0][1])
        audio = discord.FFmpegPCMAudio(executable= "./FFmpegExe/ffmpeg.exe", source= trackPath)
        return audio
    