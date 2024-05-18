import SourceFiles.RegisterService.RegisterService as register
import SourceFiles.BotConstructions.bot as constructions
import SourceFiles.MusicCore.MusicRequestHandlers.AssemblyMusicHandler as assembly
import SourceFiles.MusicCore.MusicRequestHandlers.LocalStorageMusicHandler as localHandler
import SourceFiles.MusicCore.MusicRequestHandlers.YouTubeMusicHandler as youtubeHandler
import SourceFiles.MusicCore.MusicManager as manager

register.RegisterService().LoadConfiguration()

handler = assembly.AssemblyMusicHandler([localHandler.LocalStorageMusicHandler(), 
                                         youtubeHandler.YouTubeMusicHandler()])

core = manager.MusicManager(handler)
bot = constructions.MusicBot(core)
bot.run()

#hexogonal architecture
