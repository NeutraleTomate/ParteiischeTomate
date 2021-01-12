import discord
import os
from keepAlive import keep_alive
client = discord.Client()


@client.event
async def on_ready():
  print('{0.user} is online now!'.format(client))

@client.event
async def on_message(message):
  
  positive = "👍"
  negative = "👎"
  maybe = "🤷"
  raidDays = ["Dienstag 20:00",
          "Mittwoch 20:00",
          "Donnersatg 20:00",
          "Freitag 20:00",
          "Samstag 15:00",
          "Samstag 20:00",
          "Sonntag 15:00",
          "Sonntag 20:00",
          "Montag 20:00"]
  

  for day in raidDays:
    if message.content.startswith(day):
      await message.add_reaction(positive)
      await message.add_reaction(negative)
      await message.add_reaction(maybe)

  if message.author == client.user:
    return

  if message.content.startswith("weeklypoll"):
      for day in raidDays:
        await message.channel.send(day)
      

keep_alive()
client.run(os.getenv('TOKEN'))