import requests
import json
import discord
import asyncio
import random
token = 'MzA3MTA5OTIxNDkxNTE3NDQw.C-Nh9w.kCDnFv-irmQ9K1TDgO9F49eY-Ms'
prefix = '!!'
client = discord.Client()

if __name__ == "__main__":

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.content.startswith(prefix + 'test'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1
            await client.edit_message(tmp, 'You have {} messages.'.format(counter))


    client.run(token)