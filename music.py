import discord
import ffmpeg

async def join(client, message):
    try:
          voiceChannel = message.author.voice.channel
    except AttributeError:
        await message.channel.send("You have to be connected to a voice channel!")
        return None
        
    voiceClient = await voiceChannel.connect()
    voiceClient.play(discord.FFmpegPCMAudio('video.mp4'))
    return voiceClient



async def play(client, message, voiceClient):
    #data = discord.FFmpegOpusAudio(["test.mp3",])
    #voiceClient.sendAudoipacket(data)
    pass


  
    

async def leave(client, message, voiceClient):
    pass


async def pause(client, message, voiceClient):
    pass


async def clear(client, message, voiceClient):
    pass


async def play_now(client, message, voiceClient):
    pass


