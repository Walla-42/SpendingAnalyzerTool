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
        print("Creating database tables...")
        try:
            print("Creating expenses table")
            self.c.execute("""CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        item_name TEXT,
                        date TEXT,
                        amount REAL,
                        store TEXT,
                        category TEXT
                )""")
            print("Creating income table")
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
    """
    Class for handeling the default settings which can be updated by the user. Includes the ability to create a default settings file if 
    the default settings file is not present. 
    """

    def __init__(self, settings_file="user_preferences.json"):
        self.settings_file = settings_file
        self.default_settings = {
        "income_1" : 0,
        "income_2" : 0,
        "income_3" : 0,
        "income_4" : 0,
        "reportFrequency" : "monthly",
        "reportOptions" : ["weekly", "monthly", "quarterly", "bi_annual", "annual"],
        "availableReports" : ["percentIncomeSpent", "spendingBreakdown", "avgDailyExpense", "highestExpense", "avgCategorialExpense", "spendingTrends"],
        "chosenReports" : ["percentIncomeSpent", "spendingBreakdown", "avgDailyExpense", "highestExpense", "avgCategorialExpense", "spendingTrends"],
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


class Report(Server):
    """
    Class for handeling reports generated including the statistics produced by the report
    """
    def __init__(self, database_name='transactions.db', category:str=None, date_range:tuple=None, store:str=None):
        super().__init__(database_name)

        base_query = "SELECT * FROM expenses WHERE 1=1"
        if category:
            base_query += f" AND category = {category}"
        if date_range:
            base_query += f" AND date BETWEEN {date_range[0]} AND {date_range[1]}"
        if store:
            base_query += f" AND store  = {store}"
        self.expenses = self.c.execute(base_query)
        self.income = self.c.execute("SELECT * FROM income")
        self.expense_data = self.expenses.fetchall()
        self.income_data = self.income.fetchall()


    def percent_income_spent(self):
        total_income = [sum(income[2] for income in self.income_data)]
        total_expense = [sum(expense[3] for expense in self.expense_data)]
        return total_expense/total_income * 100
    
    def spending_breakdown(self):
        pass

    def highest_expense(self):
        pass

    def avg_daily_expense(self):
        pass

    def avg_categorial_expense(self):
        pass

    def spending_trend(self):
        pass

    def generate_report(self):
        pass

    def save_report(self):
        pass

class GUI_window:
    def __init__(self):
        pass

def main():
    userSettings = UserSettings()
    database = Server()
    print("Success! Program initalized.")

if __name__ == "__main__":
    main()
