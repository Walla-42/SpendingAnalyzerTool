import numpy as np
import datetime as dt
import json, os
import sqlite3

class Transactions():
    def __init__(self, amount, date=None, category=None):
        self.amount = amount
        self.date = date if date != None else dt.today().date()
        self.category = category
        

class Expense(Transactions):
    def __init__(self, amount, name, date, store, category):
        super.__init__(amount, date, category)
        self.name = name
        self.store = store


class Income(Transactions):
    def __init__(self, amount, job, date, category):
        super.__init__(amount, date, category)
        self.job = job


class UserSettings():
    """
    Class for handeling the default settings which can be updated by the user. Includes the ability to create a default settings file if 
    the default settings file is not present. 
    """

    def __init__(self, settings_file="user_preferences.json"):
        self.settings_file = settings_file
        self.default_settings = {
        "income_1": 0,
        "income_2": 0,
        "income_3": 0,
        "income_4": 0,
        "report_start_date": "01 January",
        "report_frequency_set": "weekly",
        "reportOptions": {
            "weekly" : False,
            "monthly": False,
            "quarterly": False,
            "bi_annual": False,
            "annual": False
            },
        "availableReports": {
            "Percent Income Spent": False,
            "Spending Breakdown": False,
            "Avg Daily Expense": False,
            "Highest Expense": False,
            "Avg Categorial Expense": False,
            "Spending Trends": False
            }
        }
        self.load_preferences()

    def save_preferences(self, settings):
        print("Saving user default settings...")
        with open(self.settings_file, "w") as settings_file:
            json.dump(settings, settings_file, indent=4)
        

    def load_preferences(self):
        try:
            print("Loading user default settings...")
            with open(self.settings_file, "r") as settings:
                return json.load(settings)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Settings file not found. Creating Default Settings file...")
            self.save_preferences(self.default_settings)
            return


