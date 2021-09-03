import discord
import ffmpeg
import youtube_dl
import os



async def join(client, message):
    try:
          voiceChannel = message.author.voice.channel
    except AttributeError:
        await message.channel.send("You have to be connected to a voice channel!")
        return None
    global gVoiceClient      
    gVoiceClient = await voiceChannel.connect()




#async def play(client, message):
#    gVoiceClient.play(discord.FFmpegPCMAudio('video.mp4'))


async def play(client, message):
    try:
        if not gVoiceClient.is_connected():
            await join(client, message)
    except:
        await join(client, message)

        
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors" : [{
            "key" : "FFmpegExtractAudio",
            "preferredcodec" : "mp3",
            "preferredquality" : "192"
        }]
    }
    text = message.content.split("-play ")[1]
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % text, download=False)["entries"][0]
        except:
            pass
            
    src = info["formats"][0]["url"]
    gVoiceClient.play(discord.FFmpegPCMAudio(src))


async def dontplay(client, message):
    try:
        if not gVoiceClient.is_connected():
            await join(client, message)
    except:
        await join(client, message)

    try:
        if os.path.isfile("song.mp3"):
            os.remove("song.mp3")
    except:
        pass

    print("cont: ", message.content)
    vid_url = message.content.split("-play ")[0]
    print("url: ", vid_url)
    if not "http" in vid_url:
        vid_url = message.content.split("-play ")[1]
    print("url: ", vid_url)
    if not "http" in vid_url:
        await message.channel.send("Please enter a valid URL")
    print("url: ", vid_url)

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors" : [{
            "key" : "FFmpegExtractAudio",
            "preferredcodec" : "mp3",
            "preferredquality" : "192"
        }]
    }
    print(1)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vid_url])
        print(2)
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
            print(2)
    gVoiceClient.play(discord.FFmpegPCMAudio('song.mp3'))




async def ayaya(client, message):
    gVoiceClient.play(discord.FFmpegPCMAudio('ayaya.mp3'))
    pass


  
    

async def leave(client, message):
    await gVoiceClient.disconnect()


async def pause(client, message):
    pass


async def clear(client, message):
    pass


async def play_now(client, message):
    pass

async def queue(client, message):
    pass


