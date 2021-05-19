from vardata import positive, negative, maybe,\
                    raidDayList, pRaidList,\
                    pEmoji1, pEmoji2, pEmoji3, pEmoji4, pEmoji5, pEmojiX, pX


async def addReactions(message):
    # Reactions RaidDay
    for day in raidDayList:
        if (message.content.split(" "))[0] == day.split(";")[0]:
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
