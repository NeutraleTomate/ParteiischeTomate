import discord
import os
import datetime
from datetime import time

from keepAlive import keep_alive
from commands import commands, exactCommands
from vardata import *
from functionsUtility import *
from functionsMemes import *
from functionsDestiny import *
from setup import *
from reactions import *
from destroy import destroy
from autoTeams import *

client = discord.Client()
prefix = "!"
intents = discord.Intents.default()
intents.members = True
Intents = discord.Intents.default()
Intents.members = True
countdown = False 


# client = commands.client(command_prefix='!', intents = intents)


@client.event
async def on_ready():
    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowYear = (datetime.datetime.now()).strftime("%Y")
    nowTime = (datetime.datetime.now()).strftime("%X")
    now = nowDay + "." + nowMonth + "." + nowYear + " " + nowTime
    print('{0.user} is online at '.format(client) + now)

    # Setting `Playing ` status
    # await client.change_presence(activity=discord.Game(name="Destiny 2"))
    # Setting `Streaming ` status
    await client.change_presence(
        activity=discord.Streaming(name="Destiny 2", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    # Setting `Listening ` status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    # Setting `Watching ` status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))


@client.event
async def on_message(message):

    async def join(client, message):
      channel = message.author.voice.voice_channel
      await client.join_voice_channel(channel)
    async def leave(client, message):
      server = message.guild
      voice_client = client.voice_client_in(server)
      await voice_client.disconnect()
    
    
    if message.content.startswith('!member'):
        for member in message.guild.members:
            print(member)  #
    now = timeSetup()

    if message.author == client.user:
        await addReactions(message)

    if message.author == client.user:  # ignoring bots
        return

    if message.content.startswith(prefix):
        await loggeneral(message, now)

        if message.content.replace(prefix, "") in exactCommands:
            await exactCommands[message.content.replace(prefix, "")](message)

        else:
            for item in commands:
                if item in message.content:
                    await commands[item](message)

    # await destroy(message, client)

    if message.content == "!autoTeams":
        await autoTeams(message.channel, message.channel, client)

    if message.content == "!autoTeamsRaidTermine":
        raidTermineChannel = client.get_channel(790270264385863681)
        logchannel = client.get_channel(840316851887669309)
        await autoTeams(raidTermineChannel, logchannel, client)

    if message.content == "!autoTeamsTest":
        histchannel = client.get_channel(840630822640943134)
        logchannel = client.get_channel(840316851887669309)
        await autoTeams(histchannel, logchannel, client)

    '''if message.content == "!start countdown":
      countdown = True 

    if message.content == "!stop countdown":
      countdown = False
      print("cd false")

    themessage = await message.channel.fetch_message(841652780048973834)
    while countdown == True:
          print(countdown)
          
          nowD = datetime.datetime.now() + timedelta(hours = 2)
          timeD = datetime.datetime(2021, 5, 11, 19, 00, 00, 000000)
          print(nowD)
        
          timeDeltaToPrint =  timeD - nowD 
          #await message.channel.send("Countdown für Spielzeit der Klebepresse: t = -" + str(timeDeltaToPrint)[:-7])
          toEdit = str("Countdown für Spielzeit der Klebepresse: t = -" + str(timeDeltaToPrint)[:-7])
          await themessage.edit(content = toEdit)
          
          sleep(1)
    '''


'''
@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):

    if await client.fetch_user(payload.user_id) != client.user:
        await catchReactionsDay(payload, client)

    channel = client.get_channel(payload.channel_id)
    user = await client.fetch_user(payload.user_id)
    if user != client.user:

        message = await channel.fetch_message(payload.message_id)
        #message = discord.utils.get(await channel.history(limit=100).flatten(), author=user)
        print(user)
        print(channel)
        #await channel.send(user.mention)
        #if str(payload.emoji) == positive:
            #await channel.send(payload.emoji)
        #await channel.send(message.reactions)
        #await channel.send(message.content)
        posList = []
        negList = []
        mayList = []
        for reaction in message.reactions:
            reacList = []
            #await channel.send(reaction)
            #await channel.send(reaction.users)
            async for userf in reaction.users():
                reacList.append(userf.mention)
                #await channel.send(userf)
                #await channel.send(userf.mention)

            if str(reaction)==positive:
                posList = reacList
            elif str(reaction) == negative:
                negList = reacList
            elif str(reaction) == maybe:
                mayList = reacList
        print(len(posList) + " " + posList)
        print(len(negList) + " " + negList)
        print(len(mayList) + " " + mayList)
        
     if reaction.message.author == client.user and user != client.user:
       await checkReaction(reaction.message, reaction, user, client)
'''

keep_alive()
client.run(os.getenv('TOKEN'))
