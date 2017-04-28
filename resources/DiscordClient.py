# -*- coding: utf-8 -*-
"""
    resources.DiscordClient

    ~~~

    Handles contact between the application and Discord

    :copyright: 2017 ORPEC
"""
# Standard Modules
import asyncio

# 3rd Party Modules
import discord

# Application Modules
from resources.support import *
from resources.Store import store

discord_client = discord.Client()


def get_discord_members():

    member_list = list()

    for member in discord_client.get_all_members():
        member_list.append(
            discord_member(
                str(member.name) + "#" + str(member.discriminator),
                member.id,
                member.display_name,
                member.joined_at,
                [role.name for role in member.roles],
                member.color.to_tuple()
            )
        )

    return member_list


@discord_client.event
async def on_ready():
    print(discord_client.user.name)
    print(discord_client.user.id)
    print('------')

    store.add_discord_members(get_discord_members())


@discord_client.event
async def on_member_join(member):
    print(member)


@discord_client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await discord_client.send_message(message.channel, 'Calculating messages...')
        async for log in discord_client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await discord_client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await discord_client.send_message(message.channel, 'Done sleeping')

