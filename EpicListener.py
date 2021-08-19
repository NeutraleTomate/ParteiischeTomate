import discord
import tweepy
import asyncio
import json



class EpicListener(tweepy.StreamListener):
  def __init__(self, client, api, auth):
    print("Listener initialized")
    self.client = client
    self.api = api
    self.auth = auth
    #def on_data(self, raw_data):
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


