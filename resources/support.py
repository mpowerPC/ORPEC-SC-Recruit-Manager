# -*- coding: utf-8 -*-
"""
    resources.support
    
    ~~~~~~~~~~~~~~~~~
    
    Functions to assist Discord Server Bot.
    
    :copyright: 2017 ORPEC
"""


def fetch_token(file):
    """
    
    :param file: 
    :return: 
    """
    with open(file, 'r') as f:
        password = f.read()

    return password
