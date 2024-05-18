from .MusicPlayers.IMusicPlayer import IMusicPlayer
from .MusicPlayers.DiscordMusicPlayer import DiscordMusicPlayer
from .MusicRequestHandlers.IMusicRequestHandler import IMusicRequestHandler

class MusicManager():
    def __init__(self, handler: IMusicRequestHandler):
        self.handler = handler
        self.musicPlayers = {}

    def getPlayer(self, ctx):
        if (not ctx.guild.id in self.musicPlayers):
            player = DiscordMusicPlayer(ctx)
            self.musicPlayers[ctx.guild.id] = player

        player = self.musicPlayers[ctx.guild.id]
        return player

    async def registerPlayRequest(self, ctx, args):
        if type(args) != str:
            print("Manager: multiple arguments not supported yet")
            return None
        
        player = self.getPlayer(ctx)

        audioFile = await self.handler.getSound(args)
        if audioFile == None:
            print("Manager: audio does not found")
            return

        await player.play(ctx, audioFile)

        