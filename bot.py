import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # if user_message[0] == '?':
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, is_private=True)

        # else:
        #     await send_message(message, user_message, is_private=False)

        is_private = isinstance(message.channel, discord.DMChannel)
        await send_message(message, message.content, is_private)
        print(f'{message.author} sent a message in {message.channel}: {message.content}')

    TOKEN = 'MTA4ODM4MzA1MDc5MjA0NjYwMg.G-880l.gIbPhgdf8DGJesMVqzlyOEy2JQKlLPZLaEPxnY'
    
    client.run(TOKEN)
    