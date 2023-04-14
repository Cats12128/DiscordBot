 print(f'We have logged in as {client.user}')
  print(f'client is {client}\n')
  print(f'client.guilds is {client.guilds}\n')
  print(f'client.guilds[0] is {client.guilds[0]}\n')
  print(f'client.guilds[0].id is {client.guilds[0].id}\n')
  print(f'client.guilds type is {type(client.guilds)}\n')
  for guild in client.guilds:
    print(f'guild is {guild}\n')
    print(type(guild))
    for channel in guild.channels:
      if channel.name == "general":
        general = client.get_channel(channel.id)
        print(f'general = {general}')
      else:
        print("Not Found")
      try:
        print(channel.id)
      except:
        print("no id")
      print(type(channel))