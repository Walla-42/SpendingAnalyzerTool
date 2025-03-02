from tkinter import *
from tkinter import ttk
import sqlite3
from program_files.user_settings import UserSettings
from program_files.server_class import Server

class GUI_app(Tk):
    def __init__(self):
        super().__init__()

        # Create the window
        self.title('Spending Analyzer Tool')
        self.geometry('700x400')
        self.configure(bg="#585454")
        self.current_frame = None
        self.database = Server()
        self.User_settings = UserSettings()
        self.show_main_menu()
        print("Success! Program initalized.")
        

    def show_main_menu(self):
        """ Main Window GUI """

        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self, bg="#161313")
        self.current_frame.pack(fill=BOTH, expand=True)

        self.geometry('700x400')
        self.title('Spending Analyzer Tool')

        # Welcome to Spending Analyzer Tool
        appIntroTitle = Label(self.current_frame, text="Spending Analyzer Tool", font=("Helvetica", 42), fg="white", bg="#161313")
        appIntroTitle.pack(pady=10)

        welcomeMessage = Label(self.current_frame, text="Welcome! Select an option to get started:", font=("Helvetica", 18), fg="white", bg="#161313")
        welcomeMessage.pack(pady=20)

        # Create options buttons
        expenseButton = Button(self.current_frame, text="Enter Expense", font=("Helvetica", 10), command=self.show_expense_window, width=15, height=1, fg="black", bg="#2c9c2b")
        expenseButton.pack(pady=10)

        incomeButton = Button(self.current_frame, text="Enter Income", font=("Helvetica", 10), command=self.show_income_window, width=15, height=1, fg="black", bg="#2c9c2b")
        incomeButton.pack(pady=10)

        reportButton = Button(self.current_frame, text="Generate Report", font=("Helvetica", 10), command=None, width=15, height=1, fg="black", bg="#2c9c2b")
        reportButton.pack(pady=10)

        settingsButton = Button(self.current_frame, text="Settings", font=("Helvetica", 10), command=self.show_settings_window, width=15, height=1, fg="black", bg="#2c9c2b")
        settingsButton.pack(pady=10)

    def show_expense_window(self):
        """Function to show expenses option window. This window shows options for the user to enter their expenses. """
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self, bg="#161313")
        self.current_frame.pack(fill=BOTH, expand=True)

        self.geometry('700x400')
        self.title('Spending Analyzer Tool: Expenses')

        for i in range(5):
            self.current_frame.columnconfigure(i, weight=1)

        window_message = Label(self.current_frame, text="Enter your expense below:", font=("Helvetica", 18), fg="white", bg="#161313")
        window_message.grid(row=0, column=1, columnspan=2, pady=10)

        # Amount
        amount_label = Label(self.current_frame, text="Amount:", font=("Helvetica", 12), fg="white", bg="#161313")
        amount_label.grid(row=1, column=1, padx=10, pady=5, sticky=E)
        self.amount_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        self.amount_entry.grid(row=1, column=2, padx=10, pady=5)

        # Name
        name_label = Label(self.current_frame, text="Name:", font=("Helvetica", 12), fg="white", bg="#161313")
        name_label.grid(row=2, column=1, padx=10, pady=5, sticky=E)
        self.name_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        self.name_entry.grid(row=2, column=2, padx=10, pady=5)

        # Date
        date_label = Label(self.current_frame, text="Date:", font=("Helvetica", 12), fg="white", bg="#161313")
        date_label.grid(row=3, column=1, padx=10, pady=5, sticky=E)
        self.date_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        self.date_entry.grid(row=3, column=2, padx=10, pady=5)

        # Store
        store_label = Label(self.current_frame, text="Store:", font=("Helvetica", 12), fg="white", bg="#161313")
        store_label.grid(row=4, column=1, padx=10, pady=5, sticky=E)
        self.store_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        self.store_entry.grid(row=4, column=2, padx=10, pady=5)

        # Category Menu Options
        category_label = Label(self.current_frame, text="Category:", font=("Helvetica", 12), fg="white", bg="#161313")
        category_label.grid(row=5, column=1, padx=10, pady=5, sticky=E)
        categories = ["Housing", "Transportation", "Utilities", "Groceries", "Healthcare/Medical", "Car", "Debt Payment", "Personal Care", "Education", "Household", "Entertainment", "Charity", "Other"]
        self.category_var = StringVar(self.current_frame)
        self.category_var.set(categories[0])  # set the default option
        category_menu = OptionMenu(self.current_frame, self.category_var, *categories)
        category_menu.config(fg="black", bg="#2c9c2b")
        category_menu["menu"].config(fg="black", bg="white")
        category_menu.grid(row=5, column=2, padx=10, pady=5)

        expense_submit = Button(self.current_frame, text="Submit", font=("Helvetica", 10), command=lambda: self.add_expense(), width=15, height=1, fg="black", bg="#2c9c2b")
        expense_submit.grid(row=6, column=1, columnspan=2, pady=10)

        expense_back = Button(self.current_frame, text="Back", font=("Helvetica", 10), command=self.show_main_menu, width=15, height=1, fg="black", bg="#2c9c2b")
        expense_back.grid(row=7, column=1, columnspan=2, pady=10)

        expense_show = Button(self.current_frame, text="Show Expenses", font=("Helvetica", 10), command=self.show_expense_report_window, width=15, height=1, fg="black", bg="#2c9c2b")
        expense_show.grid(row=7, column=3, columnspan=2, pady=10)

    def show_expense_report_window(self):
        """Function to show expenses database within its own window.  """
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self, bg="#161313")
        self.current_frame.pack(fill=BOTH, expand=True)

        self.geometry('700x400')
        self.title('Spending Analyzer Tool: Report')

        tree = ttk.Treeview(self.current_frame, columns=("ID", "Name", "Date", "Amount", "Store", "Category"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Date", text="Date")
        tree.heading("Amount", text="Amount")
        tree.heading("Store", text="Store")
        tree.heading("Category", text="Category")
        tree.pack(fill=BOTH, expand=True)

        conn = sqlite3.connect('transactions.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", END, values=row)
        conn.close()

        report_back = Button(self.current_frame, text="Back", font=("Helvetica", 10), command=self.show_expense_window, width=15, height=1, fg="black", bg="#2c9c2b")
        report_back.pack(pady=10)

    def add_expense(self):
        """Adds expenses to the database using the database class methods to connect to the server"""
        expense_vars = [self.name_entry, self.amount_entry, self.date_entry, self.store_entry, self.category_var]
        expense_data = [var.get() for var in expense_vars]
        print(expense_data)
        self.database.add_to_table("expenses", [tuple(expense_data)])
        
        for var in expense_vars[0:-1]:
            var.delete(0, END)
        self.category_var.set("Food")

    def show_income_window(self):
        """"Function to close previouse window and open new income window. """
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self, bg="#161313")
        self.current_frame.pack(fill=BOTH, expand=True)

        self.geometry('700x400')
        self.title('Spending Analyzer Tool: Expenses')

        for i in range(5):
            self.current_frame.columnconfigure(i, weight=1)

        window_message = Label(self.current_frame, text="Enter your income below:", font=("Helvetica", 18), fg="white", bg="#161313")
        window_message.grid(row=0, column=1, columnspan=2, pady=10)

        # Amount
        name_label = Label(self.current_frame, text="Amount:", font=("Helvetica", 12), fg="white", bg="#161313")
        name_label.grid(row=2, column=1, padx=10, pady=5, sticky=E)
        name_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        name_entry.grid(row=2, column=2, padx=10, pady=5)

        # Job
        date_label = Label(self.current_frame, text="Job", font=("Helvetica", 12), fg="white", bg="#161313")
        date_label.grid(row=3, column=1, padx=10, pady=5, sticky=E)
        date_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        date_entry.grid(row=3, column=2, padx=10, pady=5)

        # Date
        store_label = Label(self.current_frame, text="Date", font=("Helvetica", 12), fg="white", bg="#161313")
        store_label.grid(row=4, column=1, padx=10, pady=5, sticky=E)
        store_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        store_entry.grid(row=4, column=2, padx=10, pady=5)

        # Category Menu Options
        category_label = Label(self.current_frame, text="Category:", font=("Helvetica", 12), fg="white", bg="#161313")
        category_label.grid(row=5, column=1, padx=10, pady=5, sticky=E)
        categories = ["Investments", "Salary", "Other"]
        category_var = StringVar(self.current_frame)
        category_var.set(categories[0])  # set the default option
        category_menu = OptionMenu(self.current_frame, category_var, *categories)
        category_menu.config(fg="black", bg="#2c9c2b")
        category_menu["menu"].config(fg="black", bg="white")
        category_menu.grid(row=5, column=2, padx=10, pady=5)

        income_submit = Button(self.current_frame, text="Submit", font=("Helvetica", 10), command=None, width=15, height=1, fg="black", bg="#2c9c2b")
        income_submit.grid(row=6, column=1, columnspan=2, pady=10)

        income_back = Button(self.current_frame, text="Back", font=("Helvetica", 10), command=self.show_main_menu, width=15, height=1, fg="black", bg="#2c9c2b")
        income_back.grid(row=7, column=1, columnspan=2, pady=10)

    def add_income(self):
        """Function to add the income data to the income table of the transactions database. """
        income_vars = [self.amount_entry, self.job_entry, self.date_entry, self.category_var]
        income_data = [var.get() for var in income_vars]
        print(income_data)
        self.database.add_to_table("income", [tuple(income_data)])
        
        for var in income_vars[0:-1]:
            var.delete(0, END)
        self.category_var.set("Food")
    
    def show_settings_window(self):
        """Function for managing the user setting window"""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self, bg="#161313")
        self.current_frame.pack(fill=BOTH, expand=True)

        self.geometry('700x400')
        self.title('Spending Analyzer Tool: User Settings')
        
        for i in range(2):
            self.current_frame.columnconfigure(i, weight=1)

        # Loading in settings.json file
        settings = self.User_settings.load_preferences()
        report_timeframe_options = settings.get("reportOptions")
        available_reports = settings.get("availableReports")

        # Page Title
        settings_title = Label(self.current_frame, text="Settings", font=("Helvatica", 20), fg="White", bg="#161313")
        settings_title.grid(row=0, column=0, sticky=W)

        # Drop down menu for report frequency
        category_label = Label(self.current_frame, text="Report Frequency:", font=("Helvetica", 12), fg="white", bg="#161313")
        category_label.grid(row=2, column=0, padx=10, pady=5)
        categories = report_timeframe_options
        self.category_var = StringVar(self.current_frame)
        self.category_var.set(settings.get("report_frequency_set"))  
        category_menu = OptionMenu(self.current_frame, self.category_var, *categories)
        category_menu.config(fg="black", bg="#2c9c2b")
        category_menu["menu"].config(fg="black", bg="white")
        category_menu.grid(row=2, column=1, padx=10, pady=5)

        # reports included settings start
        Reports_text = Label(self.current_frame, text="Included in generated reports:", font=("Halvatica", 12), fg="white", bg="#161313")
        Reports_text.grid(row=3, column=0)

        self.report_checkbox_vars = {}
        for i, setting in enumerate(available_reports):
            row = i // 2 + 4
            col = i % 2
            self.report_checkbox_vars[setting] = BooleanVar(value=available_reports[setting])
            checkbox_i = Checkbutton(self.current_frame, text=setting, variable=self.report_checkbox_vars[setting], width=20, height=1, bg="#2c9c2b", fg="black")
            checkbox_i.grid(row=row, column=col, padx=10, pady=10)

        def save_settings():
            """Fuction to gather the user preference data and load it into the settings.json file created by the user_settings class"""

            settings["report_frequency_set"] = self.category_var.get()
            for setting in self.report_checkbox_vars:
                settings["availableReports"][setting] = self.report_checkbox_vars[setting].get()
            self.User_settings.save_preferences(settings)

        # page buttons
        settings_back = Button(self.current_frame, text="Back", font=("Halvatica", 10), command=self.show_main_menu, width=15, height=1, fg="black", bg="#2c9c2b")
        settings_back.grid(row=8, column=0, pady=10)

        settings_save = Button(self.current_frame, text="Save", font=("Halvatica", 10), command=save_settings, width=15, height=1, fg="black", bg="#2c9c2b")
        settings_save.grid(row=8, column=1, pady=10)


   

def main():
    app = GUI_app()
    app.mainloop() 

if __name__ == "__main__":
    main()
