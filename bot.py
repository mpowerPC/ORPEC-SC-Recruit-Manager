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
import datetime

# Application Modules
from resources.support import *
from resources.DiscordClient import discord_client
from resources.GoogleClient import google_client
from resources.Store import store


def bot():
    """
    
    :return: 
    """
    last_date = datetime.datetime.now()

    while True:
        sys_date = datetime.datetime.now()

        if sys_date > last_date + datetime.timedelta(minutes=5):
            store.mass_update_rsi_info()

            google_client.clean_db()

            google_client.reset_client()
            for i, org_mem in enumerate(store.output()):
                print(org_mem.create_record())
                print()
                google_client.write_db(i + 2, org_mem.create_record())

            last_date = sys_date

        try:
            existing_members = google_client.get_db()
        except:
            google_client.reset_client()
            existing_members = google_client.get_db()

        store.add_existing_members(existing_members)

        time.sleep(60)
        
@client.event
async def on_member_join(member):
    print("Member Joined", member)
    server = member.server
    print(server)
    fmt = 'Welcome {0.mention} to ORPEC, the Outer Rim Protection and Exploration Corporation'
    await client.send_message(server, fmt.format(member, server))


def main():
    bot_thread = threading.Thread(target=bot)
    bot_thread.daemon = True
    bot_thread.start()

    discord_client.run(fetch_token("resources/token.txt"))

if __name__ == '__main__':
    main()
