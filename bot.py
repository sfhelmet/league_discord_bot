import discord
from discord.ext import commands
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    client = discord.Client(intents=discord.Intents.all())
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    @bot.command()
    async def html(ctx):
        embed = discord.Embed(title="HTML", description="HTML is the standard markup language for creating Web pages.", color=0xeee657)
        await ctx.send(embed=embed)


    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):

        username = message.author.name
        user_message = message.content
        channel = message.channel
        if message.author == client.user:
            return
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        else:
            await send_message(message, user_message, is_private=False)

        print(f'{username} sent a message in {channel}: {user_message}')

    TOKEN = 'MTA4ODM4MzA1MDc5MjA0NjYwMg.G-880l.gIbPhgdf8DGJesMVqzlyOEy2JQKlLPZLaEPxnY'
    
    client.run(TOKEN)
    