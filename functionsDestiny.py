import discord
import datetime
from datetime import timedelta
from vardata import raidDayList, pRaidList, pExplain, pX, wishEffects


async def noVaildNum(message, command):
    await message.channel.send("Please enter a valid Number or word behind `{}`".format(command))


async def wp(message):
    await message.delete()

    gap = int((datetime.datetime.now()).strftime("%w"))  #Abstand zu letztem Sonntag in Tagen
    gap -= 2 # Abstand zu letztem Dienstag in Tagen

    if gap >= 3: # Wenn Tag >= Freitag (Freitag hat einen Abstand von 3 Tagen zu Dienstag)
        gap -= 7 # dann eine Woche weiter(bis Donnerstag: letzter Dienstag, ab Freitag nächster Dienstag)

    date = datetime.datetime.now() - timedelta(days=gap) # findet nächsten/letzten Dienstag als Objekt der Klasse datetime

    for raidComb in raidDayList:
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



async def wpraids(message):
    await message.channel.send(pExplain)
    for raid in pRaidList:
        await message.channel.send(raid)
    await message.channel.send(pX)


async def wpx(message):
    await wp(message)
    await message.channel.send("---")
    await wpraids(message)


async def throne(message):
    await message.delete()
    await message.channel.send("Shattered Throne: 1st Encounter map:")
    await message.channel.send(file=discord.File("guides/Dungeons/throne.png"))


async def pit(message):
    await message.delete()
    await message.channel.send("Pit of Heresy: 4th Encounter map:")
    await message.channel.send(file=discord.File("guides/Dungeons/heresy.png"))

async def vog(message):
    try:
        number = message.content.split("!vog ")[1]
    except:
        await noVaildNum(message, "!vog")
        return
    if number == "1" or number == "3":
        await message.channel.send("VOG " + number + ". Encounter map: ")
        await message.channel.send(file=discord.File("guides/Raids/DSC/vog_" + number + ".png"))
        await message.delete()
    elif number == "loot" or number == "Loot":
        await message.channel.send("VoG Loot Table:")
        await message.channel.send(file=discord.File("guides/Raids/VoG/vog_loottable.png"))
        await message.delete()
    else:
        await noVaildNum(message, "!vog")

async def dsc(message):
    try:
        number = message.content.split("!dsc ")[1]
    except:
        await noVaildNum(message, "!dsc")
        return
    if number == "1" or number == "3":
        await message.channel.send("DSC " + number + ". Encounter map: ")
        await message.channel.send(file=discord.File("guides/Raids/DSC/dsc_" + number + ".png"))
        await message.delete()
    elif number == "loot" or number == "Loot":
        await message.channel.send("DSC Loot Table:")
        await message.channel.send(file=discord.File("guides/Raids/DSC/dsc_loottable.png"))
        await message.delete()
    else:
        await noVaildNum(message, "!dsc")


async def gos(message):
    try:
        number = message.content.split("!gos ")[1]
    except:
        await noVaildNum(message, "!gos")
        return
    if number == "2" or number == "3":
        await message.channel.send("GoS " + number + ". Encounter: ")
        await message.channel.send(file=discord.File("guides/Raids/GOS/gos_" + number + ".png"))
        await message.delete()
    elif number == "loot" or number == "Loot":
        await message.channel.send("GoS Loot Table:")
        await message.channel.send(file=discord.File("guides/Raids/GOS/gos_loottable.png"))
        await message.delete()
    else:
        await noVaildNum(message, "!gos")


async def wish(message):
    try:
        number = message.content.split("!wish ")[1]
    except:
        await noVaildNum(message, "!wish")
        return
    if number == "all":
        i = 0
        for effect in wishEffects:
            i = i + 1
            await message.channel.send(str(i) + ". Wish: " + effect)
            # await message.delete()
    elif number.isdigit():
        if 1 <= int(number) <= 14:
            await message.channel.send(number + ". Wish: " + wishEffects[int(number) - 1])
            await message.channel.send(file=discord.File("guides/Raids/LW/wishes/wish-" + number + ".jpg"))
            await message.delete()
        else:
            await noVaildNum(message, "!wish")
    else:
        await noVaildNum(message, "!wish")


async def vault(message):
    await message.delete()
    await message.channel.send("LW Vault Symbols:")
    await message.channel.send(file=discord.File("guides/Raids/LW/LW_vault_symbols.png"))
