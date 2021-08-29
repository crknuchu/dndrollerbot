import discord
import os
import random

client = discord.Client()

def roll(list):
  numlist = [int(i) for i in list]

  dnum = numlist[0]
  numlist.remove(dnum)

  if dnum not in set([4,8,10,12,20]):
    return "Not valid dice"
  else:
    total = random.randint(1,dnum)
    for num in numlist:
      total += num
    return "You rolled a " + str(total)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$help"):
    await message.channel.send("Roll the dice!\ne.g\n$roll 20 or $roll 8 + 4 + 4")

  if message.content.startswith("$roll"):
    await message.channel.send(roll(message.content.split(" ")[1::2]))    

token = os.getenv('discord_bot_token')
client.run(token)






