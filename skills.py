'''
import discord


async def weeklypoll(raidDays, positive, negative, maybe):
  for day in raidDays:
    if message.content.startswith(day):
      await message.add_reaction(positive)
      await message.add_reaction(negative)
      await message.add_reaction(maybe)

    if message.author == client.user:
      return

    if message.content.startswith("!weeklypoll") or message.content.startswith("!wp") :
      await message.delete()
      for day in raidDays:
        await message.channel.send(day)

async def sendInput():
  if message.content.startswith("!sendInput"):
        text = message.content
        text.replace("!sendInput", "")
        await message.channel.send(text)
        await message.delete()
        
'''