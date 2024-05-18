from ..AudioTrack import AudioTrack
from .IMusicRequestHandler import IMusicRequestHandler

class AssemblyMusicHandler(IMusicRequestHandler):
    def __init__(self, handlers: list):
        self.handlers = handlers

    async def getSound(self, arguments) -> AudioTrack:
        for handler in self.handlers:
            track = await handler.getSound(arguments)

            if (track != None):
                return track
    