from vardata import raidDayList,\
                    pRaidList, pEmoji1, pEmoji2, pEmoji3, pEmoji4, pEmoji5, pEmojiX, pX,\
                    positive, negative, maybe\



async def autoTeams(sourcechannel, teamchannel, client):
    dayListsDic = {
        "Dienstag;20:00": [],
        "Mittwoch;20:00": [],
        "Donnerstag;20:00": [],
        "Freitag;20:00": [],
        "Samstag;15:00": [],
        "Samstag;20:00": [],
        "Sonntag;15:00": [],
        "Sonntag;20:00": [],
        "Montag;20:00": []
    }

    pListsDic = {
        "Vault of Glass": [],
        "Deep Stone Crypt": [],
        "Garden of Salvation": [],
        "Last Wish": [],
        "Last Wish - only Riven(3x)": [],
    }
    playerList = {}

    async for message in sourcechannel.history(oldest_first=True):
        for day in raidDayList:
            try:
                messageCond = ((message.content.split(" "))[0]) + ((message.content.split(" "))[2])
                dayCond = (day.split(";")[0]) + (day.split(";")[1])
                condition = messageCond == dayCond
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
