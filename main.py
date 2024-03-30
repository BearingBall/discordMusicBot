import RegisterService.RegisterService as rs
import BotConstructions.bot as bc

rs.RegisterService().LoadConfiguration()

bot = bc.MusicBot()
bot.run()
