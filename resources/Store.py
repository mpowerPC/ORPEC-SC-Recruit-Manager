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
from resources.support import request_rsi_info


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

                    elif member.discord_name == 'ORPEC SC Recruit Manager#0898':
                        existing_member = True
                        break

                if not existing_member:
                    self._org_members.append(Member(discord_info=member))

        except:
            raise

        finally:
            self._lock.release()

    def mass_update_rsi_info(self):
        try:
            self._lock.acquire()

            for i, org_member in enumerate(self._org_members):
                if org_member.rsi_handle != "":
                    type = 'cache'
                    rsi_info = request_rsi_info(org_member.rsi_handle, type)
                    org_member.update_rsi_info(rsi_info, type)
                    self._org_members[i] = org_member
        except:
            raise

        finally:
            self._lock.release()

    def update_rsi_info(self, discord_name, rsi_info):
        try:
            self._lock.acquire()

            for i, org_member in enumerate(self._org_members):
                if org_member.discord_name == discord_name:
                    type = 'live'
                    org_member.update_rsi_info(rsi_info, type)
                    self._org_members[i] = org_member
                    print(org_member.create_record())
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
