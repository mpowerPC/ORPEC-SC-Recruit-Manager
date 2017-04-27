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
from resources.support import fetch_token

# Globals
WPATH = os.path.dirname(os.path.realpath(__file__))


# The client is persistent, but should be in function/class. Figure out what works?
client = discord.Client()

token = fetch_token(os.path.join(WPATH, "resources", "token.txt"))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


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
