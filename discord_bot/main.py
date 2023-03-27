import bot
import discord
from discord.ext import commands

'''
Invite Bot:
https://discord.com/api/oauth2/authorize?client_id=1088383050792046602&permissions=1634235578432&scope=bot
'''

# bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# @bot.command()
# async def echo(ctx, *arg):
#     embed = discord.Embed(description="<b>Hello</b>", color=0x00ff00)
#     await ctx.send(embed=embed)

if __name__ == '__main__':
    bot.run_discord_bot()
