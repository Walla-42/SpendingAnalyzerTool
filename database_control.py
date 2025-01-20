import sqlite3

conn = sqlite3.connect('spending.db')

c = conn.cursor()

# Datatypes in sqlite = NULL, INTEGER, REAL, TEXT, BLOB
# conn.execute() used to do one command
# conn.executemany() used to do multiple commands
try:
    c.execute("""CREATE TABLE items (
            item_name text,
            item_price real,
            item_category text, 
            item_date text    
        )""")
except:
    pass

items_list = []

while True:
    print("Welcome to the Spending Analyzer Tool")
    selection = input("What would you like to do?\n1.Enter an item\n2.Exit\n")
    if selection == "1":
        item_name = input("Enter the name of the item: ")
        item_price = input("Enter price of Item: ")
        item_category = input("Enter Category of Item: ")
        item_date = input("Date purchased: ")
        items_list.append((item_name, item_price, item_category, item_date))
    elif selection == "2":
        break
    else:
        print("Please enter a valid input.")
print(items_list)
print("Data entering database...")
c.executemany("INSERT INTO items VALUES (?,?,?,?)", items_list)
conn.commit()

# c.execute("DELETE FROM items")
c.execute("SELECT * FROM items")
all_expenses = c.fetchall()
print(all_expenses)
# c.execute("SELECT * FROM items") to select all from table
# c.fetchone() to select one row, c.fetchmany() to select multiple rows
# c.fetchall() to select all rows
# These will all return the table rows as a list of tuples
conn.commit()
conn.close()

