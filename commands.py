from bot import *
import requests
import json
import asyncio

async def get_json(html):
    page = requests.get(html)
    print(html)
    text = page.text
    data = json.loads(text)
    return data


async def addMember():
    blank = 0

async def removeMember():
    blank = 0

async def viewRank():
    blank = 0

async def viewFleet():
    blank = 0

async def createFleet():
    blank = 0

async def showMember(handle):

    player_Stats = get_json('http://sc-api.com/?api_source=cache&start_date=&end_date=&system=accounts&action=full_profile&target_id='+ handle +'&format=pretty_json')
    response =  '```'+\
                'Name : ' + player_Stats['data']['handle'] +\
                '```'
    return response
    # http://sc-api.com/?api_source=cache&start_date=&end_date=&system=accounts&action=full_profile&target_id=Hawkerr&format=pretty_json
    # http://sc-api.com/?api_source=cache&start_date=&end_date=&system=organizations&action=organization_members&target_id=Orpec&start_page=1&end_page=1000&format=pretty_json

if __name__ == "__main__":
    print("Commands involving managing the Main bot functions, meta commands and HTML / JSON API requests")