import discord
import os

TOKEN = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = discord.Client(intents=intents)

last_typing_user = ""

def displayAllChannels():
  for guild in client.guilds:
    print(f'Guild Name={guild.name}')
    for channel in guild.channels:
      print(f'Channel Name =  {channel.name}')
      print(f'Channel ID =  {channel.id}\n')
      
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


@client.event
async def on_ready():
  await displayAllChannels()
  #await general.send(f'general = {general} and \nclient = {client}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('A'):
    await message.channel.send('Hello!')
    print(message.channel)
    print(type(message.channel))


@client.event
async def on_typing(channel, user, when):
  global last_typing_user
  if user != last_typing_user:
    await channel.send(f'I see you typing {user.name}')
    last_typing_user = user


@client.event
async def on_voice_state_update(member, before, after):
  await general.end(f'{member.name} has joined {after}')


client.run(TOKEN)
