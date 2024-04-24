from .IMusicPlayer import IMusicPlayer
from asyncio import sleep

class DiscordMusicPlayer(IMusicPlayer):
    def __init__(self, voiceClient):
        self.voiceClient = voiceClient

    async def play(self, audio):
        self.voiceClient.play(audio)

        while self.isPlaying():
            await sleep(1)

    def isPlaying(self):
        return self.voiceClient.is_playing()

    def pause(self):
        self.voiceClient.pause()

    def resume(self):
        self.voiceClient.resume()

    def stop(self):
        self.voiceClient.stop()