from .MusicPlayers.IMusicPlayer import IMusicPlayer
from .MusicRequestHandlers.IMusicRequestHandler import IMusicRequestHandler

class MusicManager():
    def __init__(self, handler: IMusicRequestHandler):
        self.handler = handler
        self.musicQueue = []
        self.player = None

    def setPlayer(self, player: IMusicPlayer):
        if (self.player != None and self.player.isPlaying):
            self.player.stopPlaying()
        self.player = player

    async def registerPlayRequest(self, ctx, args):
        if type(args) != str:
            print("Manager: multiple arguments not supported yet")
            return None
        
        audioFile = await self.handler.getSound(args)
        if audioFile == None:
            print("Manager: audio does not found")

        self.musicQueue.append(audioFile)

        if (self.player.isPlaying()):
            return len(self.musicQueue)

        trackIdx = 0
        while(trackIdx < len(self.musicQueue)):
            track = self.musicQueue[trackIdx]
            await self.player.play(track)
            trackIdx = trackIdx + 1

        return 0

    def stop(self):
        self.musicQueue.clear()
        self.player.stop()

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.resume()



    def pushMusis(track):
        pass

    async def playQueue():
        pass

    def nextTrack():
        pass

    def prevTrack():
        pass

        