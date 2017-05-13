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
    rsi_handle = ""
    rsi_moniker = ""
    discord_name = ""
    discord_nick = ""
    discord_id = ""
    discord_join_date = ""
    rsi_backer = ""
    country = ""
    english = ""
    rsi_orpec_status = ""
    rsi_orpec_rank = ""
    rsi_orpec_stars = ""
    discord_rank = ""
    discord_fleet = ""

    def __init__(self, tracked_user=None, discord_user=None):
        """
        
        :param discord_name: 
        """
        if tracked_user:
            self.update_member(tracked_user)

        if discord_user:
            self.update_discord_info(discord_user)

    def update_member(self, tracked_user):
        """
        
        :param tracked_user: 
        :return: 
        """
        self.rsi_handle = tracked_user.rsi_handle
        self.rsi_moniker = tracked_user.rsi_moniker
        self.discord_name = tracked_user.discord_name
        self.discord_nick = tracked_user.discord_nick
        self.discord_id = tracked_user.discord_id
        self.discord_join_date = datetime.datetime.strptime(tracked_user.discord_join_date, '%y-%m-%d %H:%M:%S.%f')
        self.rsi_backer = tracked_user.rsi_backer
        self.country = tracked_user.country
        self.english = tracked_user.english
        self.rsi_orpec_status = tracked_user.rsi_orpec_status
        self.rsi_orpec_rank = tracked_user.rsi_orpec_rank
        self.rsi_orpec_stars = tracked_user.rsi_orpec_stars
        self.discord_rank = tracked_user.discord_rank
        self.discord_fleet = tracked_user.discord_fleet

    def update_rsi_info(self, rsi_info):
        """
        
        :param rsi_info: 
        :return: 
        """
        self.rsi_moniker = rsi_info['data']['moniker']

        if self.rsi_backer == 'N':
            self.rsi_backer = 'Y' if 'Backer' in rsi_info['data']['forum_roles'] else 'N'

        self.country = rsi_info['data']['country']
        self.english = 'Y' if 'English' in rsi_info['data']['fluency'] else 'N'

        if rsi_info['data']['organizations'] is not None:
            for org in rsi_info['data']['organizations']:
                if org['sid'] == 'orpec':
                    self.rsi_orpec_status = org['type']
                    self.rsi_orpec_rank = org['rank']
                    self.rsi_orpec_stars = org['stars']

                    break
                else:
                    self.rsi_orpec_status = ""
                    self.rsi_orpec_rank = ""
                    self.rsi_orpec_stars = ""

    def update_discord_info(self, discord_info):
        """
        
        :param discord_info: 
        :return: 
        """
        self.discord_name = discord_info.discord_name
        self.discord_nick = discord_info.discord_nick
        self.discord_join_date = discord_info.discord_join_date
        self.discord_id = discord_info.discord_id

        ### NEED REAL COLORS###
        if discord_info.color == (0, 0, 0):
            self.discord_fleet = 'Exploration'
        elif discord_info.color == (100, 100, 100):
            self. discord_fleet = 'Support'
        elif discord_info.color == (255, 255, 255):
            self.discord_fleet = 'Navy'
        else:
            self.discord_fleet = ""

        self.discord_rank = ""
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
