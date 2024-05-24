import ffmpeg
import discord
from ..PathManager.PathManager import PathMannager

class AudioTrack():
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def getName(self):
        return self.name

    def getFFmpeg(self):
        return discord.FFmpegPCMAudio(executable= "./" + PathMannager().GetFfmpegExeFilePath(), source = self.path)