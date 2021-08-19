import discord
import PIL
from PIL import Image, ImageDraw, ImageFont
from vardata import *
import requests

async def autoTeamsImage(histchannel, teamchannel, client):
    histchannel = client.get_channel(790270264385863681)
    testch=client.get_channel(727474264315396117)
    testch = teamchannel
    dayListsDic = {}
    pListsDic = {}
    playerList = []

    async for message in histchannel.history(oldest_first=True):
        for day in raidCombList:
            try:
                mesCond = ((message.content.split(", "))[0]) + ((message.content.split(" "))[2])
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
                            reacList.append(user.avatar_url)
                            # playerList[user.mention] = []
                            if not user.avatar_url in playerList:
                                playerList.append(user.avatar_url)
                            

                    if str(reaction) == positive:
                        posList = reacList
                    elif str(reaction) == negative:
                        negList = reacList
                    elif str(reaction) == maybe:
                        mayList = reacList

                elem = str((message.content.split(" ")[0] + ";" + message.content.split(" ")[2]))
                dayListsDic[elem] = [message.content, posList, negList, mayList]

                print(elem)
    print(dayListsDic)
    color_foreground = (230, 230, 230)
    color_background = (35, 39, 42)
    im_out = Image.new(mode = "RGB", size = (2000, (len(playerList)*200)+200), color = color_background)
    draw = ImageDraw.Draw(im_out)

    #table base
    for i in range(10):
        for j in range(len(playerList)+1):
            x = i * 200
            y = j * 200
            draw.rectangle([x,y,x+199,y+199], outline = color_foreground)

    #hardlines
    draw.rectangle([0,197,im_out.size[0],201],fill=color_foreground)#horizontal
    draw.rectangle([197,0,201,im_out.size[1]],fill=color_foreground)#vertical

    # writings
    i = 1
    font = ImageFont.truetype("guides/autoTeamsImage/arial.ttf", size=30)
    for elem in dayListsDic.values():
      txt = elem[0].replace(",","\n")
      draw.text(xy = [((i*200)+100),100], text = txt, anchor="mm", align = "center", font=font)
      i += 1



    # player avatars
    i = 1
    for player in playerList:
      try:
          #player_avatar = Image.open(urllib2.urlopen(player))
          player_avatar = Image.open(requests.get(player, stream=True).raw)
          print(player_avatar.size)
          player_avatar = player_avatar.resize([150,150])
          im_out.paste(player_avatar, box = [25,(25+(i*200))])
      except Exception as e:
        print(str(i) + " error " + str(e))
      i += 1

    #symbols
    i = 1
    for day in dayListsDic.values():
        for entry in day:
            for player in entry:
                if entry == day[0]:
                    continue
                j = playerList.index(player) + 1
                x = i * 200 + 25 
                y = j * 200 + 25
                if player in day[1]:
                    symbol = Image.open("guides/autoTeamsImage/symbols/dark_low/positive.png")
                if player in day[2]:
                    symbol = Image.open("guides/autoTeamsImage/symbols/dark_low/negative.png")
                if player in day[3]:
                    symbol = Image.open("guides/autoTeamsImage/symbols/dark_low/maybe.png")

                
                symbol = symbol.resize([150,150])
                im_out.paste(symbol, box = [x,y])
            

        i += 1


    im_out.save("guides/autoTeamsImage/out.jpg")
    await testch.send(file=discord.File("guides/autoTeamsImage/out.jpg"))
    
    

'''
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
'''
 