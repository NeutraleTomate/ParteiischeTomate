from vardata import *

'''async def catchReactionsDay(payload, client):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
'''


async def autoTeams(histchannel, teamchannel, client):
    Dienstag20 = []
    Mittwoch20 = []
    Donnerstag20 = []
    Freitag20 = []
    Samstag15 = []
    Samstag20 = []
    Sonntag15 = []
    Sonntag20 = []
    Montag20 = []
    dayListsDic = {
        "Dienstag;20:00": Dienstag20,
        "Mittwoch;20:00": Mittwoch20,
        "Donnerstag;20:00": Donnerstag20,
        "Freitag;20:00": Freitag20,
        "Samstag;15:00": Samstag15,
        "Samstag;20:00": Samstag20,
        "Sonntag;15:00": Sonntag15,
        "Sonntag;20:00": Sonntag20,
        "Montag;20:00": Montag20
    }

    VoG = []
    DSC = []
    GoS = []
    LW = []
    LWoR = []
    pListsDic = {
        "Vault of Glass": VoG,
        "Deep Stone Crypt": DSC,
        "Garden of Salvation": GoS,
        "Last Wish": LW,
        "Last Wish - only Riven(3x)": LWoR,
    }
    playerList = {}

    async for message in histchannel.history(oldest_first=True):
        for day in raidCombList:
            try:
                mesCond = ((message.content.split(" "))[0]) + ((message.content.split(" "))[2])
                dayCond = (day.split(";")[0]) + (day.split(";")[1])
                condition = mesCond == dayCond
            except IndexError:
                condition = False
            if condition:
                posList = []
                negList = []
                mayList = []
                for reaction in message.reactions:
                    reacList = []
                    async for user in reaction.users():
                        if user != client.user:
                            reacList.append(user.mention)
                            # playerList[user.mention] = []
                            playerList.update({user.mention: []})

                    if str(reaction) == positive:
                        posList = reacList
                    elif str(reaction) == negative:
                        negList = reacList
                    elif str(reaction) == maybe:
                        mayList = reacList

                elem = str((message.content.split(" ")[0] + ";" + message.content.split(" ")[2]))
                dayListsDic[elem] = [message.content, posList, negList, mayList]

                print(elem)
                '''print((dayListsDic[elem])[0])
                print((dayListsDic[elem])[1])
                print((dayListsDic[elem])[2])'''

        for raid in pRaidList:
            if message.content == raid:
                plist1 = []
                plist2 = []
                plist3 = []
                plist4 = []
                plist5 = []

                for reaction in message.reactions:
                    reacList = []
                    async for user in reaction.users():
                        if user != client.user:
                            reacList.append(user.mention)
                    if str(reaction) == pEmoji1:
                        plist1 = reacList
                    elif str(reaction) == pEmoji2:
                        plist2 = reacList
                    elif str(reaction) == pEmoji3:
                        plist3 = reacList
                    elif str(reaction) == pEmoji4:
                        plist4 = reacList
                    elif str(reaction) == pEmoji5:
                        plist5 = reacList

                elem = message.content
                pListsDic[elem] = [plist1, plist2, plist3, plist4, plist5]

                print(elem)
                '''print((pListsDic[elem])[0])
                print((pListsDic[elem])[1])
                print((pListsDic[elem])[2])
                print((pListsDic[elem])[3])
                print((pListsDic[elem])[4])'''

        if message.content == pX:
            plistX = []
            for reaction in message.reactions:
                reacList = []
                async for user in reaction.users():
                    if user != client.user:
                        reacList.append(user.mention)
                if str(reaction) == pEmojiX:
                    plistX = reacList

    print("PLIST: ")
    print(playerList)
    for day in dayListsDic.values():

        print(day[0])
        for raid in pListsDic.values():
            raidTeam = []
            raidNameX = str(list(pListsDic.keys())[list(pListsDic.values()).index(raid)])
            if raidNameX == "Last Wish - only Riven(3x)":
                raidNameX = "Last Wish"

            print(raidNameX)
            try:
                for player in plistX:
                    if player in day[1]:
                        player = str(player)
                        if player == '<@697121563392081981>' and raidNameX != 'Deep Stone Crypt':
                          continue
                        if (raidNameX not in playerList[player]) and (day[0] not in playerList[player]):
                            raidTeam.append(player)


            except:
                pass

            for prio in raid:  # raid 0 ist die stufe exo
                if prio == raid[4]:
                    continue
                for player in prio:
                    if player in day[1]:
                        player = str(player)
                        print((raidNameX not in playerList[player]))
                        # print(raidNameX)
                        # print(playerList[player])
                        if player == '<@697121563392081981>' and raidNameX != 'Deep Stone Crypt':
                          continue
                        if (raidNameX not in playerList[player]) and (day[0] not in playerList[player]):
                            raidTeam.append(player)

                if len(raidTeam) >= 6:
                    print("break")
                    break
            print(len(raidTeam))
            if len(raidTeam) >= 6:
                raidName = str(list(pListsDic.keys())[list(pListsDic.values()).index(raid)])
                raidAnnounce = raidName + " \n" + day[0] + ": \n"
                for participant in raidTeam:
                    raidAnnounce = raidAnnounce + participant + "\n"
                    playerList[participant].append(raidNameX)
                    playerList[participant].append(day[0])
                # await logchannel.send(raidAnnounce)
                await teamchannel.send(raidAnnounce)
                print("TeamCreated")
                print(playerList)
