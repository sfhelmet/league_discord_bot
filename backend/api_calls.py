import requests
import json
import config

key = config.API_KEY

def get_account_puuid(username, tagline): # Riot API call to get account puuid
    response = requests.get(f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tagline}?api_key={key}')
    return response.text

def get_user_by_summoner_name(summoner_name):
    response = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={key}')
    return response.text

def get_rank_by_encrypted_summoner_id(encrypted_summoner_id):
    response = requests.get(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{encrypted_summoner_id}?api_key={key}')
    return response.text

summoner_name = "sfhelmet"
user_info = json.loads(get_user_by_summoner_name(summoner_name=summoner_name))

encrypted_summoner_id = user_info['id']
rank_info = json.loads(get_rank_by_encrypted_summoner_id(encrypted_summoner_id=encrypted_summoner_id))[0]

tier = rank_info['tier']
rank = rank_info['rank']
league_points = rank_info['leaguePoints']

print(summoner_name, tier, rank, league_points)

