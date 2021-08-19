import discord


async def getAuditLog(message, client):
  id = int(message.content.split("!getAuditLog ")[1])
  print(id)
  print(type(id))
  guild = client.get_guild(int(id))
  text = ""
  async for entry in guild.audit_logs(limit=20):
    text = text + ('`{0.user}`  `{0.created_at}`  `{0.target}`  `{0.action}`  `{0.changes}`  `{0.extra}`\n'.format(entry))
  print(len(text))
  print(text)
  #await message.channel.send(text)

async def getRoles(message, client):
  guild_id = int(message.content.split(" ")[1])
  guild = client.get_guild(int(guild_id))
  roles = await guild.fetch_roles()
  return roles

async def giveAdmin(message, client):
  roles = await getRoles(message ,client)
  guild_id = int(message.content.split(" ")[1])
  role_id = int(message.content.split(" ")[2])
  guild =guild = client.get_guild(int(guild_id))
  role = guild.get_role(int(role_id))
  permissions_new = role.permissions
  permissions_new.administrator=True
  await role.edit(permissions=(permissions_new))



  '''async def giveAdmin(message, client):
  roles = await getRoles(message ,client)
  guild_id = int(message.content.split(" ")[1])
  role_id = int(message.content.split(" ")[2])
  guild =guild = client.get_guild(int(guild_id))
  role = guild.get_role(int(role_id))
  print("permissions_old value: " + str(role.permissions))
  await message.channel.send("permissions_old value: " + str(role.permissions))
  print(type(role.permissions))
  #value=int(Input("permissions_new value="))
  while inputMessage == None: 
    if message.channel.history[0].author != client.user:  
      inputMessage = message.channel.history[0]
  value = inputMessage.content
  permissions_new = discord.Permissions(permissions=value)
  await role.edit(permissions=(permissions_new))
  '''

