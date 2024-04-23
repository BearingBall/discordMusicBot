from .IMusicPlayer import IMusicPlayer
from asyncio import sleep

class DiscordMusicPlayer(IMusicPlayer):
    def __init__(self, voiceClient):
        self.voiceClient = voiceClient

    async def play(self, audio):
        self.voiceClient.play(audio)

        while self.voiceClient.is_playing():
            await sleep(1)

        #await voiceClient.disconnect()