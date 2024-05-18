import ffmpeg
import discord

class AudioTrack():
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def getName(self):
        return self.name

    def getFFmpeg(self):
        return discord.FFmpegPCMAudio(executable= "./FFmpegExe/ffmpeg.exe", source = self.path)