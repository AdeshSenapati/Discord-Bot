import discord
import pyjokes

TOKEN = "NDY3OTI5MjYyOTYwMTQ4NDkw.W0rfFQ.t5AfsrRvsdgR8CATXlHiABbb9g4"

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye {username}')
            return
        elif user_message.lower() == '!joke':
            tell_joke = pyjokes.get_joke()
            await message.channel.send(tell_joke)
            return

client.run(TOKEN)



