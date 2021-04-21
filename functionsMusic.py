


import discord
from discord.voice_client import*
import asyncio

async def davis(message):
    user=message.author
    print(user)

    Voicechannel = message.author.voice.voice_channel
    print(Voicechannel)
    
    VoiceChannel.connect()



'''async def davis(message):
    # grab the user who sent the command
    user=message.author
    voice_channel=user.voice.voice_channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await message.channel.send('User is in channel: '+ channel)
        # create StreamPlayer
        vc = await VoiceChannel.connect()
        player = vc.create_ffmpeg_player('media/davis2.mp4', after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await message.channel.send('User is not in a channel.')'''