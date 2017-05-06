# -*- coding: utf-8 -*-
"""
    resources.DiscordClient

    ~~~

    Handles contact between the application and Discord

    :copyright: 2017 ORPEC
"""
# Standard Modules
import asyncio
import time

# 3rd Party Modules
import discord

# Application Modules
from resources.Store import store
from resources.support import *

discord_client = discord.Client()

discord_member = namedtuple(
        'disc_member',
        'discord_name, discord_id, discord_nick, discord_join_date, roles, color, member'
    )


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
                member.color.to_tuple(),
                member
            )
        )

    return member_list


def convert_discord_member(member):
    member_list = list()
    member_list.append(
        discord_member(
            str(member.name) + "#" + str(member.discriminator),
            member.id,
            member.display_name,
            member.joined_at,
            [role.name for role in member.roles],
            member.color.to_tuple(),
            member
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
    message = """Hello, Iam ORPEC's management bot, I organize ranks and track new users who enter this server. To help
command better server you, could you please respond with your RSI Handle?
    
Example: https://roberspaceindustries.com/citizens/mpowerpc <- mpowerpc is a RSI Handle
    
If you are unable to find your handle, please message a member of command."""
    store.add_discord_members(convert_discord_member(member))

    pm = await discord_client.start_private_message(member)

    sent = await discord_client.send_message(pm, content=message, tts=True, embed=None)

    response = await discord_client.wait_for_message(timeout=300, channel=pm, author=member)

    if response is not None and response.content != message:

        rsi_info = request_rsi_info(response.content, 'live')

        if rsi_info:
            store.update_rsi_info(str(member), rsi_info)


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

