import discord

class BotUtils():

    async def connectUserVoiceChannel(ctx):
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            print("Command asked not from voice channel!")
            return None

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            vc = await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
            vc = ctx.voice_client
        
        return vc
