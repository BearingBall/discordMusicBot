import validators
import ffmpeg
import discord
import operator
import os
from difflib import SequenceMatcher

from ..AudioTrack import AudioTrack
from .IMusicRequestHandler import IMusicRequestHandler

class LocalStorageMusicHandler(IMusicRequestHandler):
    async def getSound(self, arguments) -> AudioTrack:
        if (validators.url(arguments)):
            print("LocalStorage: link does not supported")
            return None
        else:
            return self.getSoundByName(arguments)

    def getSoundByName(self, name: str) -> AudioTrack:
        localMusicPath = "./LocalMusic"

        localMusicList = os.listdir(localMusicPath)

        musicSimilarityRating = [(SequenceMatcher(None, musicName, name).ratio(), musicName) for musicName in localMusicList]
        musicSimilarityRating.sort(key=operator.itemgetter(0), reverse=True)
        
        if (musicSimilarityRating[0][0] < 0.5 and (musicSimilarityRating[0][0] - musicSimilarityRating[1][0]) < 0.15):
            print("File not found")
            return None
        
        musicName = musicSimilarityRating[0][1]
        trackPath = os.path.join(localMusicPath, musicName)

        return AudioTrack(trackPath, musicName)
    