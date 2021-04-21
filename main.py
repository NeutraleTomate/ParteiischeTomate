import discord
import os
import datetime

from keepAlive import keep_alive

from commands import commands, exactCommands
from vardata import *
from functionsUtility import *
from functionsMemes import *
from functionsDestiny import *
from functionsMusic import*

client = discord.Client()
prefix = "!"

"""def log(text):
    with open("log.csv", "a") as file:
        file.write(text + "\n")"""


@client.event
async def on_ready():
    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowYear = (datetime.datetime.now()).strftime("%Y")
    nowTime = (datetime.datetime.now()).strftime("%X")
    now = nowDay + "." + nowMonth + "." + nowYear + " " + nowTime
    print('{0.user} is online at '.format(client) + now)

    # Setting `Playing ` status
    #await client.change_presence(activity=discord.Game(name="Destiny 2"))
    # await client.change_presence(activity=discord.Game(name="mit Ruben dem dicken Fisch"))

    # Setting `Streaming ` status
    await client.change_presence(activity=discord.Streaming(name="Destiny 2", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    # Setting `Listening ` status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    # Setting `Watching ` status
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))


@client.event
async def on_message(message):
    # time Setup
    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowYear = (datetime.datetime.now()).strftime("%Y")
    nowTime = (datetime.datetime.now()).strftime("%X")
    now = nowDay + "." + nowMonth + "." + nowYear + " " + nowTime

    async def loggeneral(message):
        with open("log.csv", "a") as file:
            file.write(message.author.name + ";" + now + ";" + message.content + "\n")

    # Reactions
    # Reactions RaidDates
    if message.author == client.user:
        for day in raidCombList:

            if (message.content.split(" "))[0] == day.split(";")[0]:
                # await message.add_reaction(discord.utils.get(client.emojis, name=customEmoji1))
                await message.add_reaction(positive)
                await message.add_reaction(negative)
                await message.add_reaction(maybe)

    # Reactions RaidPriority
    if message.author == client.user:
        for raidName in pRaidList:
            if message.content == raidName:
                await message.add_reaction(pEmoji1)
                await message.add_reaction(pEmoji2)
                await message.add_reaction(pEmoji3)
                await message.add_reaction(pEmoji4)
                await message.add_reaction(pEmoji5)

        if message.content == pX:
            await message.add_reaction(pEmojiX)

    # ignoring bots
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        await loggeneral(message)
        
        if message.content.replace(prefix, "") in exactCommands:
            await exactCommands[message.content.replace(prefix, "")](message)
        
        else:
            for item in commands:
                if item in message.content:
                    await commands[item](message)






keep_alive()
client.run(os.getenv('TOKEN'))
