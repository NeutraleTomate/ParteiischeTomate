import discord#pls wörk
import os
import datetime
from datetime import timedelta
from time import sleep
from keepAlive import keep_alive

client = discord.Client()

positive = "👍"
negative = "👎"
maybe = "🤷"
raidCombList = ["Dienstag;20:00;2",
                "Mittwoch;20:00;3",
                "Donnerstag;20:00;4",
                "Freitag;20:00;5",
                "Samstag;15:00;6",
                "Samstag;20:00;6",
                "Sonntag;15:00;0",
                "Sonntag;20:00;0",
                "Montag;20:00;1"]  # liste von Raidterminen: [Wochentag;Uhrzeit;Wochentag als Zahl(Sonntag = 0, Samstag = 6)]

wishEffects = [
    "grants an Ethereal Key.",
    "spawns the ship-chest between Morgeth and the Vault(Glittering Key needed).",
    "unlocks an Emblem.",
    "teleports the fireteam to Shuro Chi.",
    "teleports the fireteam to Morgeth.",
    "teleports the fireteam to the Vault.",
    "teleports the fireteam to Riven.",
    "will play the song, Hope for the Future.",
    "Failsafe comments the Raid.",
    "The Drifter comments the Raid.",
    "activates Confetti mode",
    "fancy Hats",
    "activates Petra's Run.",
    "spawns Corruptes eggs."

]


@client.event
async def on_ready():
    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowYear = (datetime.datetime.now()).strftime("%Y")
    nowTime = (datetime.datetime.now()).strftime("%X")
    now = nowDay + "." + nowMonth + "." + nowYear + " " + nowTime

    print('{0.user} is online at '.format(client) + now)


@client.event
async def on_message(message):
    if False:
        await message.channel.send("Robin hat Recht!")

    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowYear = (datetime.datetime.now()).strftime("%Y")
    nowTime = (datetime.datetime.now()).strftime("%X")
    now = nowDay + "." + nowMonth + "." + nowYear + " " + nowTime

    if message.author == client.user:
        for day in raidCombList:

            if (message.content.split(" "))[0] == day.split(";")[0]:
                print(True)
                await message.add_reaction(positive)
                await message.add_reaction(negative)
                await message.add_reaction(maybe)

    if message.author == client.user:
        return

    if "!throne" in message.content:
        await message.delete()
        await message.channel.send("Shattered Throne: 1st Encounter map:")
        await message.channel.send(file=discord.File("guides/throne.png"))

    if "!heresy" or "!pit" in message.content:
        await message.delete()
        await message.channel.send("Pit of Heresy: 4th Encounter map:")
        await message.channel.send(file=discord.File("guides/heresy.png"))

    if "!wish" in message.content:
        await message.delete()
        number = message.content.split("!wish ")[1]
        if number == "all":
            i = 0;
            for effect in wishEffects:
                i = i + 1
                await message.channel.send(str(i) + ". Wish: " + effect)


        else:
            await message.channel.send(number + ". Wish: " + wishEffects[int(number) - 1])
            await message.channel.send(file=discord.File("guides/wishes/wish-" + number + ".jpg"))

    if "!dsc" in message.content:
        await message.delete()
        number = message.content.split("!dsc ")[1]
        if number == 1 or 3:
            await message.channel.send("DSC " + number + ". Encounter map: ")
            await message.channel.send(file=discord.File("guides/DSC/crypta_map_0" + number + ".png"))

    if "!helöp" in message.content:
        await message.delete()
        await message.channel.send("Available Commands: \n\
      `!throne`: Shattered Throne 1st Encounter map \n\
      `!heresy`: Pit of Heresy 4th Encounter map \n\
      `!dsc 1`: DSC 1st Encounter map \n\
      `!dsc 3`: DSC 3rd Encounter map\n\
      `!wish all`: Overview over all Wishes \n\
      `!wish` + number(1-14): shows the selected wish\n\
      `!wahrheit`: Beschert dir die Erleuchtung nach der du dein Leben lang gesucht hast! "
                                   )

    if "!wahrheit" in message.content:
        await message.channel.send("Robin hat Recht!")

    if "!xxtime" in message.content:
        print(message.author.name + " used !xxtime at " + now)
        await message.delete()
        xxtime = (datetime.datetime.now()).strftime("%c")
        for i in range(1, 60):
            if xxtime != (datetime.datetime.now()).strftime("%c"):
                xxtime = (datetime.datetime.now()).strftime("%c")
                await message.channel.send(xxtime)
            else:
                sleep(0.49)

    if "!weeklypoll" in message.content or "!wp" in message.content:
        await message.delete()
        print(message.author.name + " used !wp at " + now)

        addent = int((datetime.datetime.now()).strftime("%w"))
        addent += -2
        if addent >= 3:
            addent += -7

        date = datetime.datetime.now() - timedelta(days=addent)

        for raidComb in raidCombList:
            raidComb = raidComb.split(";")
            raidDay = raidComb[0]
            raidTime = raidComb[1]

            if date.strftime("%w") != raidComb[
                2]:  # verhindert das bei wiederholung von wochentagen das datum erhöht wird
                date = date + timedelta(days=1)

            day = date.strftime("%d")
            month = date.strftime("%m")
            # year = date.strftime("%Y")
            dateToPrint = day + "." + month + "."  # + year
            await message.channel.send(raidDay + " " + dateToPrint + " " + raidTime)

    if "!send" in message.content:
        text = message.content
        text = text.replace("!send", "")

        print(message.author.name + " used !send at " + now + " with " + text)
        await message.channel.send(text)
        await message.delete()

    if "!nein" in message.content:
        await message.delete()
        print(message.author.name + " used !nein at " + now)
        for i in range(10):
            await message.channel.send("**NEIN**")

    if "!clear" in message.content:
        print(message.author.name + " used !clear at " + now)
        args = message.content.split(" ")
        if len(args) == 2 and args[1].isdigit():
            limit = int(args[1]) + 1
            deleted = await message.channel.purge(limit=limit)
            await message.channel.send("{} messages deleted.".format(len(deleted) - 1))
            sleep(0.7)
            await message.channel.purge(limit=1)
        elif args[1] == "x":
            await message.channel.send("You got me there xD")
        else:
            await message.channel.send("`!clear x` clears x messages. \n Your command doesn't fit this pattern!")


keep_alive()
client.run(os.getenv('TOKEN'))
