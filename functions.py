import discord
import datetime
from datetime import timedelta
from vardata import*


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