import discord
import os
import datetime
from datetime import timedelta
from time import sleep
from keepAlive import keep_alive
from loremipsum import get_sentences






customEmoji1 = "eis"
positive = "👍"
negative = "👎"
maybe = "🤷"


client = discord.Client()



raidCombList = ["Dienstag;20:00;2",
                "Mittwoch;20:00;3",
                "Donnerstag;20:00;4",
                "Freitag;20:00;5",
                "Samstag;15:00;6",
                "Samstag;20:00;6",
                "Sonntag;15:00;0",
                "Sonntag;20:00;0",
                "Montag;20:00;1"
                ]  # liste von Raidterminen: [Wochentag;Uhrzeit;Wochentag als Zahl(Sonntag = 0, Samstag = 6)]
pEmoji1 = "⚠️"
pEmoji2 = "🟦"
pEmoji3 = "🟩"
pEmoji4 = "🟨"
pEmoji5 = "🟥"
pEmojiX = "✅"


pX = "Ich möchte einfach raiden - egal was(Wenn diese Option ausgewählt wird bitte nichts anderes auswählen)"

pExplain = "**Erklärung für Prioritäts-Abstimmung:**\n\
            " + pEmoji1 + " Ich möchte, weil ich noch ein Exo brauch\n\
            " + pEmoji2 + " Ich möchte, weil ich noch Rüstung/Waffen brauch\n\
            " + pEmoji3 + " Ich möchte, weil ich bock hab\n\
            " + pEmoji4 + " Ich mach mit wenn jemand fehlt\n\
            " + pEmoji5 + " Ich möchte auf gar keinen fall\n\
            " + pEmojiX + "" + pX 

pRaidList = ["Deep Stone Crypt",
             "Garden of Salvation",
             "Last Wish",
             "Last Wish - only Riven(3x)",
             ]


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
helopText = "**Available Commands:**\n\
      `!throne`: Shattered Throne 1st Encounter map\n\
      `!heresy` or `!pit`: Pit of Heresy 4th Encounter map\n\
      `!dsc 1`: DSC 1st Encounter map\n\
      `!dsc 3`: DSC 3rd Encounter map\n\
      `!dsc loot`: DSC LootTable\n\
      `!gos 2`: GoS 2nd Encounter map\n\
      `!gos 3`: GoS 3rd Encounter Eyes\n\
      `!gos loot`: GoS LootTablen\n\
      `!LW vault`: LW Vault Symbols\n\
      `!wish all`: Overview over all Wishes \n\
      `!wish` + number(1-14): shows the selected wish\n\
      `!wahrheit`: Beschert dir die Erleuchtung nach der du dein Leben lang gesucht hast! "

#genderTable
#!xxtime
#!clear
#!write
#!send
#!nein


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
    await client.change_presence(activity=discord.Game(name="Destiny 2"))
    #await client.change_presence(activity=discord.Game(name="mit Ruben dem dicken Fisch"))

    # Setting `Streaming ` status
    #await client.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    # Setting `Listening ` status
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    # Setting `Watching ` status
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))


@client.event
async def on_message(message):
    #await message.channel.send("**Clemens muss aufhören!**")
    #function Setup
    def loggeneral():
        with open("log.csv", "a") as file:
            file.write(message.author.name + ";" + now + ";" + message.content + "\n")

    async def wp():
        await message.delete()

        addent = int((datetime.datetime.now()).strftime("%w"))
        addent += -2
        if addent >= 3:
            addent += -7

        date = datetime.datetime.now() - timedelta(days=addent)

        for raidComb in raidCombList:
            raidComb = raidComb.split(";")
            raidDay = raidComb[0]
            raidTime = raidComb[1]

            if date.strftime("%w") != raidComb[2]:
                # verhindert das bei wiederholung von wochentagen das datum erhöht wird
                date = date + timedelta(days=1)

            rDay = date.strftime("%d")
            month = date.strftime("%m")
            # year = date.strftime("%Y")
            dateToPrint = rDay + "." + month + "."  # + year
            await message.channel.send(raidDay + " " + dateToPrint + " " + raidTime)

    async def wpraids():
        await message.channel.send(pExplain)
        for raid in pRaidList:
            await message.channel.send(raid)
        await message.channel.send(pX)


    # time Setup
    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowYear = (datetime.datetime.now()).strftime("%Y")
    nowTime = (datetime.datetime.now()).strftime("%X")
    now = nowDay + "." + nowMonth + "." + nowYear + " " + nowTime

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

    # commands
    if "!throne" in message.content:
        loggeneral()
        await message.delete()
        await message.channel.send("Shattered Throne: 1st Encounter map:")
        await message.channel.send(file=discord.File("guides/Dungeons/throne.png"))

    if "!heresy" in message.content or "!pit" in message.content:
        loggeneral()
        await message.delete()
        await message.channel.send("Pit of Heresy: 4th Encounter map:")
        await message.channel.send(file=discord.File("guides/Dungeons/heresy.png"))

    if "!wish" in message.content:
        loggeneral()
        await message.delete()
        number = message.content.split("!wish ")[1]
        if number == "all":
            i = 0
            for effect in wishEffects:
                i = i + 1
                await message.channel.send(str(i) + ". Wish: " + effect)
        else:
            await message.channel.send(number + ". Wish: " + wishEffects[int(number) - 1])
            await message.channel.send(file=discord.File("guides/Raids/LW/wishes/wish-" + number + ".jpg"))

    if"!riven" in message.content:
      loggeneral()
      await message.delete()
      number = "7"
      await message.channel.send(number + ". Wish: " + wishEffects[int(number) - 1])
      await message.channel.send(file=discord.File("guides/Raids/LW/wishes/wish-" + number + ".jpg"))


    if "!LW vault" in message.content:
      loggeneral()
      await message.delete()
      await message.channel.send("LW Vault Symbols:")
      await message.channel.send(file=discord.File("guides/Raids/LW/LW_vault_symbols.png"))



    if "!dsc" in message.content:
        loggeneral()
        await message.delete()
        try:
          number = message.content.split("!dsc ")[1]
        except:
          await message.channel.send("Please enter a Number or word behind `!dsc`")
        if number == "1" or number == "3":
            await message.channel.send("DSC " + number + ". Encounter map: ")
            await message.channel.send(file=discord.File("guides/Raids/DSC/crypta_map_0" + number + ".png"))
        elif number == "loot" or number == "Loot":
          await message.channel.send("DSC Loot Table:")
          await message.channel.send(file=discord.File("guides/Raids/DSC/dsc_loottable.png"))


    if "!gos" in message.content:
        loggeneral()
        await message.delete()
        try:
          number = message.content.split("!gos ")[1]
        except:
          await message.channel.send("Please enter a Number or word behind `!gos`")
        if number == "2" or number == "3":
            await message.channel.send("GoS " + number + ". Encounter: ")
            await message.channel.send(file=discord.File("guides/Raids/GOS/gos_" + number + ".png"))
        elif number == "loot" or number == "Loot":
          await message.channel.send("GoS Loot Table:")
          await message.channel.send(file=discord.File("guides/Raids/GOS/gos_loottable.png"))      


 

    if "!helöp" in message.content:
        loggeneral()
        await message.delete()
        await message.channel.send(helopText)

    if "!wahrheit" in message.content:
        loggeneral()
        await message.channel.send("Robin hat Recht!")

    if "!xxtime" in message.content:
        loggeneral()
        await message.delete()
        xxtime = (datetime.datetime.now()).strftime("%c")
        for i in range(1, 60):
            if xxtime != (datetime.datetime.now()).strftime("%c"):
                xxtime = (datetime.datetime.now()).strftime("%c")
                await message.channel.send(xxtime)
            else:
                sleep(0.49)

    if "!wp" == message.content:
        loggeneral()
        await wp()

    if "!wpx" == message.content:
        loggeneral()
        await wp()
        await message.channel.send("---")
        await wpraids()

    if "!send" in message.content:
        text = message.content
        text = text.replace("!send", "")

        loggeneral()
        await message.channel.send(text)
        await message.delete()

    if "!nein" in message.content:
        await message.delete()
        loggeneral()
        for i in range(5):
            await message.channel.send("**NEIN**")

    if "!clear" in message.content:
        loggeneral()
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

    if "!genderTable" in message.content:
      await message.delete()
      await message.channel.send("Bitte wählen Sie:in Ihr:in Geschlecht:in!")
      await message.channel.send(file=discord.File("guides/genderTable.jpg"))
    
    if "!write" in message.content:
      await message.delete()
      try:
        number =  int(message.content.split("!write ")[1])
      except:
        number = 3      
      sentences_list = get_sentences(number)
      for sentence in sentences_list:
        sentence = sentence.replace("B'", "")
        sentence = sentence.replace("b'", "")
        sentence = sentence.replace("'", "")
        await message.channel.send(sentence)



    if ":(" in message.content or ":frowning:" in message.content or "😦" in message.content:
      await message.channel.send(":(")

    if ":)" == message.content:
      await message.channel.send(":)")


keep_alive()
client.run(os.getenv('TOKEN'))
