import discord
import datetime
from datetime import timedelta
from vardata import *


async def wp(message):
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


async def dsc(message):
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


async def gos(message):
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


async def wish(message):
    await message.delete()
    try:
        number = message.content.split("!wish ")[1]
    except:
        await message.channel.send("Please enter a Number or word behind `!wish`")
    if number == "all":
        i = 0
        for effect in wishEffects:
            i = i + 1
            await message.channel.send(str(i) + ". Wish: " + effect)
    else:
        await message.channel.send(number + ". Wish: " + wishEffects[int(number) - 1])
        await message.channel.send(file=discord.File("guides/Raids/LW/wishes/wish-" + number + ".jpg"))


async def vault(message):
    await message.delete()
    await message.channel.send("LW Vault Symbols:")
    await message.channel.send(file=discord.File("guides/Raids/LW/LW_vault_symbols.png"))
