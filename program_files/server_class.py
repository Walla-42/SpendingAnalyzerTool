import sqlite3

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
            self.c.executemany(f"INSERT INTO {table} (item_name, date, amount, store, category) VALUES (?,?,?,?,?)", table_data)
        elif table == "income":
            self.c.executemany(f"INSERT INTO {table} (job, amount, date, category) VALUES (?,?,?,?)", table_data)
        self.conn.commit()
        print("Data added to table")