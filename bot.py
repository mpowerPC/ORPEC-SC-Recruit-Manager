# -*- coding: utf-8 -*-
"""
    bot
    
    ~~~
    
    Discord Server Bot.
    
    :copyright: 2017 ORPEC
"""
# Standard Modules
import os
import asyncio

# 3rd Party Modules
import discord

# Application Modules
from resources.support import *


# The client is persistent, but should be in function/class. Figure out what works?
client = discord.Client()

token = fetch_token("resources/token.txt")


def get_discord_members():
    return [str(member.name) + "#" + str(member.discriminator) for member in client.get_all_members()]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    print(get_discord_members())

    ODB = ORPECDB('Members', 'Sheet1')
    print(ODB.get_users())

@client.event
async def on_member_join(member):
    print(member)

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(token)
