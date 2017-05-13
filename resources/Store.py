# -*- coding: utf-8 -*-
"""
    resources.Store

    ~~~~~~~~~~~~~~~~~

    A class that handles async information sharing.

    :copyright: 2017 ORPEC
"""
# Standard Modules
import threading
import requests
import logging

# Application Modules
from resources.Member import Member
from resources.GoogleClient import google_client


class Store:
    _lock = threading.Lock()
    _tracked_users = list()
    _status = False

    _logger = logging.getLogger(__name__)

    def fetch_tracked_users(self):
        """
        
        :return: 
        """
        self._logger.info("Fetching Tracked Users")
        tracked_users = google_client.get_db()

        for user in tracked_users:
            existing_member = False

            for i, org_member in enumerate(self._tracked_users):
                if org_member.discord_name == user.discord_name:
                    existing_member = True
                    break

            if not existing_member:
                try:
                    self._lock.acquire()
                    self._tracked_users.append(Member(tracked_user=user))

                except Exception as e:
                    self._logger.exception(e)

                finally:
                    self._lock.release()

    def update_discord_users(self, discord_members):
        self._logger.info("Updateing Users from Discord.")
        try:
            self._lock.acquire()

            for member in discord_members:
                existing_member = False
                for i, org_member in enumerate(self._tracked_users):
                    if org_member.discord_name == member.discord_name:
                        org_member.update_discord_info(member)
                        self._tracked_users[i] = org_member
                        existing_member = True
                        break

                    elif member.discord_name == 'ORPEC SC Recruit Manager#0898':
                        existing_member = True
                        break

                if not existing_member:
                    self._tracked_users.append(Member(discord_user=member))

        except:
            raise

        finally:
            self._lock.release()

    @staticmethod
    def fetch_rsi_info(rsi_handle, request_type='cache'):
        if rsi_handle != "":

            r = requests.get(
                "http://sc-api.com/?api_source=" + request_type + "&system=accounts&action=full_profile&target_id=" + rsi_handle + \
                "&expedite=0&format=raw"
            )

            if r.status_code == 200:
                return r.json()

        return False

    def update_users(self, request_type):
        """
        
        :param type: 
        :return: 
        """
        try:
            self._lock.acquire()

            for i, user in enumerate(self._tracked_users):
                rsi_info = self.fetch_rsi_info(user.rsi_handle, request_type)

                if rsi_info:
                    user.update_rsi_info(rsi_info)
                    self._tracked_users[i] = user
                    print(user.create_record())

        except Exception as e:
            logging.exception(e)

        finally:
            self._lock.release()

    def get_status(self):
        """
        
        :return: 
        """
        try:
            self._lock.acquire()
            status = self._status

        except:
            raise

        finally:
            self._lock.release()

        return status

    def toggle_status(self):
        """
        
        :return: 
        """

        try:
            self._lock.acquire()
            self._status = not self._status

        except:
            raise

        finally:
            self._lock.release()

    def update_tracked_users(self):
        """
        
        :return: 
        """
        try:
            self._lock.acquire()

            tracked_users = self._tracked_users

        except Exception as e:
            logging.exception(e)

        finally:
            self._lock.release()

        google_client.clean_db()

        for i, user in enumerate(tracked_users):
            try:
                google_client.write_db(i+2, user.create_record())

            except Exception as e:
                logging.error(e)

                google_client.reset_client()

                try:
                    google_client.write_db(i + 2, user.create_record())

                except Exception as e_2:
                    logging.exception(e_2)

        self.toggle_status()


store = Store()
