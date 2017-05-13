# -*- coding: utf-8 -*-
"""
    app

    ~~~

    ORPEC Member Database, an application that utilizes Google Sheets, Discord, and SC-API.com to maintain an active
    organization database.

    :copyright: 2017 ORPEC
"""
# Standard Modules
import time
import threading
import logging.config

# Initialize Logging
logging.config.fileConfig('resources/logging.cfg')

# Application Modules

from resources.DiscordClient import discord_client, fetch_token
from resources.Store import store


def member_manager(logger=logging.getLogger(__name__)):
    """
    
    :return: 
    """
    logger.info("Initializing Member Management.")

    store.fetch_tracked_users()

    while True:

        if store.get_status():
            logger.info("Updating google member dictionary.")
            store.update_users('cache')
            store.update_tracked_users()

        time.sleep(5)


def main():
    """
    
    :return: 
    """
    logger = logging.getLogger(__name__)

    logger.info("Initializing ORPEC Discord Bot")

    bot_thread = threading.Thread(target=member_manager, args=(logger,))
    bot_thread.daemon = True
    bot_thread.start()

    discord_client.run(fetch_token("resources/token.txt"))

if __name__ == '__main__':
    main()
