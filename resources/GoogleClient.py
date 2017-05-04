# -*- coding: utf-8 -*-
"""
    resources.GoogleClient

    ~~~

    Handles contact between the application and the Google Sheet.

    :copyright: 2017 ORPEC
"""
# 3rd Party Modules
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# Application Modules
from resources.support import *


class GoogleClient:
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name('resources/client_secret.json', scope))

    _member = namedtuple(
        'member',
        'orpec_id, rsi_handle, rsi_moniker, discord_name, discord_nick, discord_id, discord_join_date, rsi_backer, \
        country, english, rsi_orpec_status, rsi_orpec_rank, rsi_orpec_stars, discord_rank, discord_fleet'
    )

    def __init__(self, work_book, work_sheet):
        """
        
        :param work_book: 
        :param work_sheet: 
        """
        self.work_book = self.client.open(work_book)
        self.work_sheet = self.work_book.worksheet(work_sheet)

    def reset_client(self):
        self.client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name('resources/client_secret.json',
                                                                                         self.scope))

    def get_db(self):
        """

        :return: 
        """
        self.reset_client()

        count = 2
        row = self.work_sheet.row_values(count)

        member_list = list()
        while row[3] != '' or row[1] != '':
            member_list.append(
                self._member(
                    count-1,
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13]
                )
            )

            count += 1
            row = self.work_sheet.row_values(count)

        return member_list

    def write_db(self, row, record):
        """
        
        :param row: 
        :param record: 
        :return: 
        """
        self.work_sheet.insert_row(record, row)

    def clean_db(self):
        """
        
        :return: 
        """
        self.reset_client()

        row = self.work_sheet.row_values(2)
        while row[3] != '' or row[1] != '':
            self.work_sheet.delete_row(2)
            row = self.work_sheet.row_values(2)


google_client = GoogleClient('Members', 'member_db')