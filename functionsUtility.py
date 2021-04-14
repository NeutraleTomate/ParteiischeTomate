from time import sleep
from vardata import *


async def helop(message):
    await message.delete()
    await message.channel.send(helopText)


async def send(message):
    await message.channel.send(message.content.replace("!send", ""))
    await message.delete()


async def clear(message):
    args = message.content.split(" ")
    if len(args) == 2 and args[1].isdigit():
        limit = int(args[1]) + 1
        deleted = await message.channel.purge(limit=limit)
        await message.channel.send("{} messages deleted.".format(len(deleted) - 1))
        sleep(0.7)
        await message.channel.purge(limit=1)
    else:
        await message.channel.send("`!clear x` clears x messages. \n Your command doesn't fit this pattern!")
