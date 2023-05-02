# import bot
import config
import random
import discord
from discord.ext import commands
from tabulate import tabulate
from api_calls import get_rank_by_summoner_name


'''
Invite Bot:
https://discord.com/api/oauth2/authorize?client_id=1088383050792046602&permissions=1634235578432&scope=bot
'''

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
summoner_names = config.SUMMONER_NAMES

@bot.command()
async def table(ctx):
    
    data = []
    for i in range(len(summoner_names)):
        data.append(get_rank_by_summoner_name(summoner_names[i]))
    
    print(data)

    sorted_data = sorted(data, key=lambda x: (["MASTER","DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE", "IRON"].index(x[1].split()[0]), 
                                                {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}[x[1].split()[1]], 
                                                x[2]),)
    table = tabulate(sorted_data, headers=['Summoner Name', 'Rank', 'LP'], tablefmt='orgtbl')

    await ctx.send(f'```{table}```')

if __name__ == '__main__':
    bot.run(config.DISCORD_KEY)
    print(f'{bot.user} has connected to Discord!')
    
