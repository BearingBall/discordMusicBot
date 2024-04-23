import SourceFiles.RegisterService.RegisterService as register
import SourceFiles.BotConstructions.bot as constructions
#import SourceFiles.MusicCore.LocalStorageMusicHandler as core
import SourceFiles.MusicCore.MusicRequestHandlers.YouTubeMusicHandler as handler
import SourceFiles.MusicCore.MusicManager as manager

register.RegisterService().LoadConfiguration()

#core = core.LocalStorageMusicHandler()
core = manager.MusicManager(handler.YouTubeMusicHandler())

bot = constructions.MusicBot(core)
bot.run()

#hexogonal architecture