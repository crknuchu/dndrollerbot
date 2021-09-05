import discord
import os
import random

client = discord.Client()

def roll(numOfDice,size,modifier):
  total = 0
  if size not in set([4,8,10,12,20]):
    return "Not valid dice"
  else:
    for i in range(0,numOfDice):
      total += random.randint(1,size)
  total += modifier
  return "Total: " + str(total)

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
    numOfDice = int(message.content.split(" ")[1].split("d")[0])
    size = int(message.content.split(" ")[1].split("d")[1])
    modifier = int(message.content.split(" ")[3])
    await message.channel.send(str(numOfDice) + "d" + str(size) + " + " + str(modifier) + "\n" + roll(numOfDice,size,modifier))
    #print(message.content.split(" "))
    #print(roll(numOfDice,size,modifier))



my_secret = os.environ['discord_bot_token']
token = os.getenv('discord_bot_token')
client.run(token)






