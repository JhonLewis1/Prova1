import discord

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

client.run("OTY0Mjg0Njc2NjI3OTAyNTA0.YliaFg.aHByYM4Nhlz5KxUrF3xwfkr6oCw")