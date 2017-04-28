# -*- coding: utf-8 -*-
"""
    resources.Member

    ~~~

    Member Object.

    :copyright: 2017 ORPEC
"""
# Standard Modules
import datetime


class Member:
    orpec_id = None
    rsi_handle = None
    rsi_moniker = None
    discord_name = None
    discord_nick = None
    discord_id = None
    discord_join_date = None
    rsi_backer = None
    country = None
    english = None
    rsi_orpec_status = None
    rsi_orpec_rank = None
    rsi_orpec_stars = None
    discord_rank = None
    discord_fleet = None

    def __init__(self, orpec_record=None, discord_info=None):
        """
        
        :param discord_name: 
        """
        if orpec_record:
            self.update_member(orpec_record)

        if discord_info:
            self.update_discord_info(discord_info)

    def update_member(self, orpec_record):
        """
        
        :param orpec_record: 
        :return: 
        """
        self.orpec_id = orpec_record.orpec_id
        self.rsi_handle = orpec_record.rsi_handle if orpec_record.rsi_handle != '' else None
        self.rsi_moniker = orpec_record.rsi_moniker if orpec_record.rsi_moniker != '' else None
        self.discord_name = orpec_record.discord_name if orpec_record.discord_name != '' else None
        self.discord_nick = orpec_record.discord_nick if orpec_record.discord_nick != '' else None
        self.discord_id = orpec_record.discord_id if orpec_record.discord_id != '' else None
        self.discord_join_date = datetime.datetime.strptime(orpec_record.discord_join_date, '%y-%m-%d %H:%M:%S.%f') \
            if orpec_record.discord_join_date != '' else None
        self.rsi_backer = orpec_record.rsi_backer if orpec_record.rsi_backer != '' else None
        self.country = orpec_record.country if orpec_record.country != '' else None
        self.english = orpec_record.english if orpec_record.english != '' else None
        self.rsi_orpec_status = orpec_record.rsi_orpec_status if orpec_record.rsi_orpec_status != '' else None
        self.rsi_orpec_rank = orpec_record.rsi_orpec_rank if orpec_record.rsi_orpec_rank != '' else None
        self.rsi_orpec_stars = orpec_record.rsi_orpec_stars if orpec_record.rsi_orpec_stars != '' else None
        self.discord_rank = orpec_record.discord_rank if orpec_record.discord_rank != '' else None
        self.discord_fleet = orpec_record.discord_fleet if orpec_record.discord_fleet != '' else None

    def update_rsi_info(self, rsi_info):
        """
        
        :param rsi_info: 
        :return: 
        """
        self.rsi_handle = rsi_info['data']['handle']
        self.rsi_moniker = rsi_info['data']['moniker']
        self.rsi_backer = 'Y' if 'Backer' in rsi_info['data']['forum_roles'] else 'N'
        self.country = rsi_info['data']['country']
        self.english = 'Y' if 'English' in rsi_info['data']['fluency'] else 'N'

        self.rsi_orpec_status = None
        self.rsi_orpec_rank = None
        self.rsi_orpec_stars = None

        for org in rsi_info['data']['organizations']:
            if org['sid'] == 'orpec':
                self.rsi_orpec_status = org['type']
                self.rsi_orpec_rank = org['rank']
                self.rsi_orpec_stars = org['stars']

    def update_discord_info(self, discord_info):
        """
        
        :param discord_info: 
        :return: 
        """
        self.discord_name = discord_info.discord_name
        self.discord_nick = discord_info.discord_nick
        self.discord_join_date = discord_info.discord_join_date
        self.discord_id = discord_info.discord_id

        self.discord_fleet = None
        if discord_info.color== (0, 0, 0):
            self.discord_fleet = 'Exploration'
        elif discord_info.color == (100, 100, 100):
            self. discord_fleet = 'Support'
        elif discord_info.color== (255, 255, 255):
            self.discord_fleet = 'Navy'

        self.discord_rank = None
        for rank in discord_info.roles:
            if rank == 'Admiral':
                self.discord_rank = 'Admiral'
                break

            elif rank == 'Vice Admiral':
                self.discord_rank = 'Vice Admiral'
                break

            elif rank == 'Commodore':
                self.discord_rank = 'Commodore'
                break

            elif rank == 'Captain':
                self.discord_rank = 'Captain'
                break

            elif rank == 'Commander':
                self.discord_rank = 'Commander'
                break

            elif rank == 'Lieutenant Commander':
                self.discord_rank = ' Lieutenant Commander'
                break

            elif rank == 'Lieutenant':
                self.discord_rank = 'Lieutenant'
                break

            elif rank == 'Chief Petty Officer':
                self.discord_rank = 'Chief Petty Officer'
                break

            elif rank == 'Petty Officer':
                self.discord_rank = 'Petty Officer'
                break

            elif rank == 'Master Sailor':
                self.discord_rank = 'Master Sailor'
                break

            elif rank == 'Sailor':
                self.discord_rank = 'Sailor'
                break

    def create_record(self):
        """
        
        :return: 
        """
        return (
            self.rsi_handle,
            self.rsi_moniker,
            self.discord_name,
            self.discord_nick,
            self.discord_id,
            self.discord_join_date.strftime('%y-%m-%d %H:%M:%S.%f'),
            self.rsi_backer,
            self.country,
            self.english,
            self.rsi_orpec_status,
            self.rsi_orpec_rank,
            self.rsi_orpec_stars,
            self.discord_rank,
            self.discord_fleet
        )

    def __str__(self):
        """
        
        :return: 
        """

        return (
            str(self.rsi_handle) +
            "\n\tDiscord Name: " + str(self.discord_name) +
            "\n\tOrpec Status: " + str(self.rsi_orpec_status) +
            "\n\tOrpec Fleet: " + str(self.discord_fleet) +
            "\n\tOrpec Rank: " + str(self.discord_rank)
        )
