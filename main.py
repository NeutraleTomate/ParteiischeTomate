import discord
import os
import datetime
import json
import tweepy
import asyncio



#from EpicListener import EpicListener
#from clovisstream import clovisStream

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
from autoTeamsImage import *
from functionsOther import *
from music import *

client = discord.Client()
prefix = "!"


'''intents = discord.Intents.default()
intents.members = True
Intents = discord.Intents.default()
Intents.members = True
client = commands.client(command_prefix='!', intents = intents)'''


'''API_KEY = os.getenv("T_API_Key")
API_SECRET_KEY = os.getenv("T_API_Secret")
ACCESS_TOKEN = os.getenv("T_Access_Token")
SECRET_ACCESS_TOKEN = os.getenv("T_Access_Secret")
os.getenv("T_Bearer")





class EpicListener(tweepy.StreamListener):
  def __init__(self, client, api, auth):
    print("Listener initialized")
    self.client = client
    self.api = api
    self.auth = auth
    def on_data(self, raw_data):
        print("raw_data")
        #self.process_data(raw_data)
        #print("on_data")
        #return True

    def on_status(self, status):
        self.process_data(status)
        print("on_status")
        return True

    def process_data(self, raw_data):
        print("process_data")
        #print(raw_data)
        #print(type(raw_data))
        #tweet = json.loads(raw_data)
        print(raw_data._json)
        print()
        tweet = raw_data._json["extended_tweet"]["full_text"]
        print(tweet)
        for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.name == 'better-clovis-bot':
                        #asyncio.run_coroutine_threadsafe(sendTweet(channel, tweet["text"]))
                        #asyncio.run()
                        asyncio.run_coroutine_threadsafe(channel.send(tweet), client.loop)
                        print("sended")
                        #print("xxxxxxx" + str(tweet["text"]))
                        #client.send_message(channel, tweet["text"] )
                      


    def on_error(self, status_code):
        print("error " + str(status_code))
        #if status_code == 420:
        #    return False




class clovisStream():
    def __init__(self, auth, listener):
      #self.api = api
      self.stream = tweepy.Stream(auth = auth, listener = listener)
      print("stream initialized")

    def start(self):
       print("stream started")
       self.stream.filter(follow=["1024705885103423490","1061305524925415424"], is_async=True)


auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY) 
auth.set_access_token (ACCESS_TOKEN, SECRET_ACCESS_TOKEN) 
api = tweepy.API(auth)


listener = EpicListener(client, api, auth)'''





@client.event
async def on_ready():
    #stream = clovisStream(auth, listener)
    #stream.start()


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

    if message.content == "!autoTeamsImage" or message.content == "!aTI":
        await autoTeamsImage(message.channel, message.channel, client)
    if message.content == "!autoTeamsImage2" or message.content == "!aTI2":
        await autoTeamsImage2(message.channel, message.channel, client)
    
    
    if message.content.startswith(prefix) and "!getAuditLog" in  message.content:
      await getAuditLog(message, client)

    if message.content.startswith(prefix) and "!getRoles" in  message.content:
      print(await getRoles(message, client))
    
    if message.content.startswith(prefix) and  "!giveAdmin" in  message.content:
      return
      print(await giveAdmin(message, client))
    
    if message.content.startswith(prefix) and "!join" in message.content:
        global gVoiceClient
        gVoiceClient = await join(client, message)

    if message.content.startswith(prefix) and "!play" in message.content:
        
        await play(client, message, gVoiceClient)



    if message.content.startswith(prefix) and  "!editMessages" in message.content:
      ed_messages = [879018512385982475,
                  879018513300344852,
                  879018513933684746,
                  879018514520895488,
                  879018515129049128,
                  879018494254018590,
                  879018493687767040,
                  879018492521762847]      
      for ed_mes_id in ed_messages:
          channel = client.get_channel(790270264385863681)
          ed_mes = await channel.fetch_message(ed_mes_id)
          text = ed_mes.content.split(" ")
          output = ""
          output = str(text[0] + ", " + text[1] + " " + text[2])
          await ed_mes.edit(content=output)

    
      

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
client.run( os.getenv('TOKEN'))