# -*- coding: utf-8 -*-
"""
    resources.Store

    ~~~~~~~~~~~~~~~~~

    A class that handles async information sharing.

    :copyright: 2017 ORPEC
"""
# Standard Modules
import threading

# Application Modules
from resources.Member import Member


class Store:
    _lock = threading.Lock()

    _org_members = list()

    def __init__(self):
        """

        """
        pass

    def add_existing_members(self, existing_members):
        for member in existing_members:

            existing_member = False
            for i, org_member in enumerate(self._org_members):
                if org_member.discord_name == member.discord_name:
                    existing_member = True
                    break

            if not existing_member:
                self._org_members.append(Member(orpec_record=member))

    def add_discord_members(self, discord_members):
        try:
            self._lock.acquire()

            for member in discord_members:
                existing_member = False
                for i, org_member in enumerate(self._org_members):

                    if org_member.discord_name == member.discord_name:
                        org_member.update_discord_info(member)
                        self._org_members[i] = org_member
                        existing_member = True
                        break

                if not existing_member:
                    self._org_members.append(Member(discord_info=member))

        except:
            raise

        finally:
            self._lock.release()

    def update_rsi_info(self, discord_name, rsi_info):
        try:
            self._lock.acquire()

            for i, org_member in enumerate(self._org_members):
                if org_member.discord_name == discord_name:
                    org_member.update_rsi_info(rsi_info)
                    self._org_members[i] = org_member
                    break
        except:
            raise

        finally:
            self._lock.release()

    def output(self):
        try:
            self._lock.acquire()
            out = self._org_members

        except:
            raise

        finally:
            self._lock.release()

        return out


store = Store()
