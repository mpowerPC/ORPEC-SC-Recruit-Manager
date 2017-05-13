# -*- coding: utf-8 -*-
"""
    resources.DiscordClient

    ~~~

    Handles contact between the application and Discord

    :copyright: 2017 ORPEC
"""
# Python Native Modules
from collections import namedtuple
import asyncio

import logging
logger = logging.getLogger(__name__)

# 3rd Party Modules
import discord

# Application Modules
from resources.Store import store


discord_client = discord.Client()

discord_member = namedtuple(
        'disc_member',
        'discord_name, discord_id, discord_nick, discord_join_date, roles, color, member'
    )


def fetch_token(file):
    """

    :param file: 
    :return: 
    """
    with open(file, 'r') as f:
        password = f.read()

    return password


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
    logger.debug(discord_client.user.name)
    logger.debug(discord_client.user.id)
    logger.debug('------')

    store.update_discord_users(get_discord_members())

    store.toggle_status()


@discord_client.event
async def on_member_join(member):
    store.update_discord_users(convert_discord_member(member))

    logger.info("Member Joined", member)
    server = member.server

    msg = 'Welcome {0.mention} to ORPEC, the Outer Rim Protection and Exploration Corporation'
    await discord_client.send_message(server, msg.format(member, server))


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

