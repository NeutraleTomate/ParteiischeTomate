import datetime
from time import sleep

from loremipsum import get_sentences


async def wahrheit(message):
    await message.channel.send("Robin hat Recht!")


async def nein(message):
    await message.delete()
    for i in range(5):
        await message.channel.send("**NEIN**")


async def xxtime(message):
    await message.delete()
    for i in range(1, 60):
        xtime = (datetime.datetime.now()).strftime("%c")
        await message.channel.send(xtime)
        sleep(0.49)


async def write(message):
    await message.delete()
    try:
        number = int(message.content.split("!write ")[1])
    except:
        number = 3
    sentences_list = get_sentences(number)
    for sentence in sentences_list:
        sentence = sentence.replace("B'", "")
        sentence = sentence.replace("b'", "")
        sentence = sentence.replace("'", "")
        await message.channel.send(sentence)

