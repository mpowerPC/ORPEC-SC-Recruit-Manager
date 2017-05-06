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

import commands



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
    print("Member Joined", member)
    server = member.server
    print(server)
    fmt = 'Welcome {0.mention} to ORPEC, the Outer Rim Protection and Exploration Corporation'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!add'):
        try:
            inputVars = message.content.split(" ")[1:]

        except IndexError:
            temp = await client.send_message(message.channel, 'Invalid Request')
        try:
            temp = await client.send_message(message.channel, 'Adding ' + inputVars[0] + ' to ' + inputVars[1] + ' as ' + inputVars[2])
        except IndexError:
            temp = await client.send_message(message.channel,'Not enough details provided')
    elif message.content.startswith('!showMember'):
        inputVars = message.content.split(" ")[1:]
        response = await commands.showMember(input);
        await client.send_message(message.channel, response)

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(token)
