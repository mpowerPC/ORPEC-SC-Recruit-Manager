# -*- coding: utf-8 -*-
"""
    resources.support
    
    ~~~~~~~~~~~~~~~~~
    
    Functions to assist Discord Server Bot.
    
    :copyright: 2017 ORPEC
"""
# 3rd Party Modules
from oauth2client.service_account import ServiceAccountCredentials
import gspread


def fetch_token(file):
    """
    
    :param file: 
    :return: 
    """
    with open(file, 'r') as f:
        password = f.read()

    return password


class ORPECDB():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('resources/client_secret.json', scope)
    client = gspread.authorize(creds)

    def __init__(self, work_book, work_sheet):
        self.work_book = self.client.open(work_book)
        self.work_sheet = self.work_book.worksheet(work_sheet)

    def get_users(self):

        user_list = list()
        for i,member in enumerate(self.work_sheet.col_values(3)):
            if i == 0:
                continue
            if member != '':
                user_list.append(member)

        return user_list



