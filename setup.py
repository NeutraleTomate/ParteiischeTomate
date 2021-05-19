import datetime


def timeNow():
    nowDay = (datetime.datetime.now()).strftime("%d")
    nowMonth = (datetime.datetime.now()).strftime("%m")
    nowYear = (datetime.datetime.now()).strftime("%Y")
    nowTime = (datetime.datetime.now()).strftime("%X")
    return nowDay + "." + nowMonth + "." + nowYear + " " + nowTime


async def log(message, now):
    with open("log.csv", "a") as file:
        file.write(message.author.name + ";" + now + ";" + message.content + "\n")
