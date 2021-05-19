import discord
import os
import datetime

from keepAlive import keep_alive
from commands import commands, exactCommands
from setup import timeNow, log
from reactions import addReactions
from autoTeams import autoTeams


client = discord.Client()
prefix = "!"

@client.event
async def on_ready():
    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowTime = (datetime.datetime.now()).strftime("%X")
    now = nowDay + "." + nowMonth + ". " + nowTime
    print(client + " is online at " + now)

    await client.change_presence(
        activity=discord.Streaming(name="Destiny 2", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))

@client.event
async def on_message(message):    
    now = timeNow()

    if message.author == client.user:
        await addReactions(message)
        return  # ignoring bots

    if message.content.startswith(prefix):
        await log(message, now)

        if message.content.replace(prefix, "") in exactCommands:
            await exactCommands[message.content.replace(prefix, "")](message)
        else:
            for item in commands:
                if item in message.content:
                    await commands[item](message)

    if message.content == "!autoTeams":
        await autoTeams(message.channel, message.channel, client)

    if message.content == "!autoTeamsRaidTermine":
        getChannel = client.get_channel(790270264385863681)
        sendChannel = client.get_channel(840316851887669309)
        await autoTeams(getChannel, sendChannel, client)

    if message.content == "!autoTeamsTest":
        getChannel = client.get_channel(840630822640943134)
        sendChannel = client.get_channel(840316851887669309)
        await autoTeams(getChannel, sendChannel, client)

    
    
    
    
    
    '''
    async def join(client, message):
      channel = message.author.voice.voice_channel
      await client.join_voice_channel(channel)
    async def leave(client, message):
      server = message.guild
      voice_client = client.voice_client_in(server)
      await voice_client.disconnect()
    '''


keep_alive()
client.run(os.getenv('TOKEN'))
