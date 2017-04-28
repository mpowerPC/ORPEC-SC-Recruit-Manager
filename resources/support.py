# -*- coding: utf-8 -*-
"""
    resources.support
    
    ~~~~~~~~~~~~~~~~~
    
    Functions to assist Discord Server Bot.
    
    :copyright: 2017 ORPEC
"""
# Standard Modules
import requests
from collections import namedtuple


#Globals
discord_member = namedtuple(
        'disc_member',
        'discord_name, discord_id, discord_nick, discord_join_date, roles, color'
    )


def fetch_token(file):
    """
    
    :param file: 
    :return: 
    """
    with open(file, 'r') as f:
        password = f.read()

    return password


def request_rsi_info(rsi_handle, type):
    """
    
    :param rsi_handle: 
    :return: 
    """
    r = requests.get(
        "http://sc-api.com/?api_source=" + type + "&system=accounts&action=full_profile&target_id=" + rsi_handle + \
        "&expedite=0&format=raw"
    )

    if r.status_code == 200:
        return r.json()
    else:
        return False

