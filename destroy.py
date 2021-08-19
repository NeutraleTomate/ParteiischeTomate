async def destroy(message, client):
    if message.content == "!leaveServer":
        for guild in client.guilds:
            if guild.name == "UNO":
                await guild.leave()

    if message.content == "!deleteAllChannels":
        for guild in client.guilds:
            if guild.name == "UNO":
                for channel in guild.channels:
                    try:
                        await channel.delete()
                    except:
                        print(str(channel) + " no Access")

    if message.content == "!kickAllMembers":
        for guild in client.guilds:
            if guild.name == "Test":
                # print(guild.fetch_members(limit=None))
                async for member in guild.fetch_members(limit=150):
                    print(member.name)
                    #   async for member in guild.fetch_members(limit=None):
                    try:
                        await member.kick()
                    except:
                        print(str(member) + " no Access")
