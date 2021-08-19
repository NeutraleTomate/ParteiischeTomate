import tweepy

class clovisStream():
    def __init__(self, auth, listener):
      #self.api = api
      self.stream = tweepy.Stream(auth = auth, listener = listener)
      print("stream initialized")

    def start(self):
       print("stream started")
       self.stream.filter(follow=["1024705885103423490","1061305524925415424"], is_async=True)