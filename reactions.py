from vardata import *


async def addReactions(message):
    for day in raidCombList:

        if (message.content.split(" "))[0] == day.split(";")[0]:
            # await message.add_reaction(discord.utils.get(client.emojis, name=customEmoji1))
            await message.add_reaction(positive)
            await message.add_reaction(negative)
            await message.add_reaction(maybe)

    # Reactions RaidPriority

    for raidName in pRaidList:
        if message.content == raidName:
            await message.add_reaction(pEmoji1)
            await message.add_reaction(pEmoji2)
            await message.add_reaction(pEmoji3)
            await message.add_reaction(pEmoji4)
            await message.add_reaction(pEmoji5)

    if message.content == pX:
        await message.add_reaction(pEmojiX)
