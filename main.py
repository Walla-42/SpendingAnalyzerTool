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


class Server():
    def __init__(self, database_name='transactions.db'):
        self.database_name = database_name
        self.conn = sqlite3.connect(database_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.c.execute("""CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        item_name TEXT,
                        date TEXT,
                        amount REAL,
                        store TEXT,
                        category TEXT
                )""")
            self.c.execute("""CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        job TEXT,
                        amount REAL,
                        date TEXT,
                        category TEXT
                )""")
            
            self.conn.commit()

        except sqlite3.Error() as e:
            print("Error {e}: Failed to Create table")
            

    def add_to_table(self, table, table_data):
        if table == "expenses":
            self.c.executemany(f"INSERT INTO {table} VALUES (?,?,?,?,?), {table_data}")
        elif table == "income":
            self.c.executemany(f"INSERT INTO {table} VALUES (?,?,?,?), {table_data}")


class UserSettings():
    def __init__(self, settings_file="user_preferences.json"):
        self.settings_file = settings_file

    def load_preferences():
        pass

    def save_preferences():
        pass

class Report():
    def __init__():
        pass