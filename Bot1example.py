import discord
import requests
import json

def get_quote ():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    words = json_data[0]['q']
    author = json_data[0]['a']
    quote = words + " -" + author
    return (quote)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('pong')
        
    if message.content.startswith('!pong'):
        await message.channel.send('ping')
        
    if message.content.startswith('!Enri'):
        await message.channel.send('Ciao Enri')
        
    if message.content.startswith('!Hello'):
        await message.channel.send("Hello, " + message.author.name + " !")
        
        
    if message.content.startswith('!Quote'):
        quote = get_quote()
        await message.channel.send(quote)

client.run("OTY0Mjg0Njc2NjI3OTAyNTA0.YliaFg.aHByYM4Nhlz5KxUrF3xwfkr6oCw")