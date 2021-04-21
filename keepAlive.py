from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hey, you! Yeah exactly you right there! You're not supposed to be here!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


# by freecodecamp.org
# https://www.youtube.com/watch?v=SPTfmiYiuok