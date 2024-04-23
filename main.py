import SourceFiles.RegisterService.RegisterService as register
import SourceFiles.BotConstructions.bot as constructions
#import SourceFiles.MusicCore.LocalStorageMusicHandler as core
import SourceFiles.MusicCore.YouTubeMusicHandler as core

register.RegisterService().LoadConfiguration()

#core = core.LocalStorageMusicHandler()
core = core.YouTubeMusicHandler()

bot = constructions.MusicBot(core)
bot.run()

#hexogonal architecture