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

# Application Modules
from resources.support import *
from resources.Member import Member
from resources.DiscordClient import discord_client
from resources.GoogleClient import google_client
from resources.Store import store


def bot():
    while True:
        existing_members = google_client.get_db()
        store.add_existing_members(existing_members)

        time.sleep(60)

        google_client.clean_db()

        for i, org_mem in enumerate(store.output()):
            google_client.write_db(i+2, org_mem.create_record())


def main():
    bot_thread = threading.Thread(target=bot)
    bot_thread.daemon = True
    bot_thread.start()

    discord_client.run(fetch_token("resources/token.txt"))

if __name__ == '__main__':
    main()
