from tkinter import *

class GUI_app(Tk):
    def __init__(self):
        super().__init__()

        # Create the window
        self.title('Spending Analyzer Tool')
        self.geometry('700x400')
        self.configure(bg="#585454")
        self.current_frame = None
        self.show_main_menu()
        

    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self, bg="#161313")
        self.current_frame.pack(fill=BOTH, expand=True)

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

        settingsButton = Button(self.current_frame, text="Settings", font=("Helvetica", 10), command=None, width=15, height=1, fg="black", bg="#2c9c2b")
        settingsButton.pack(pady=10)

    def show_expense_window(self):
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
        amount_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        amount_entry.grid(row=1, column=2, padx=10, pady=5)

        # Name
        name_label = Label(self.current_frame, text="Name:", font=("Helvetica", 12), fg="white", bg="#161313")
        name_label.grid(row=2, column=1, padx=10, pady=5, sticky=E)
        name_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        name_entry.grid(row=2, column=2, padx=10, pady=5)

        # Date
        date_label = Label(self.current_frame, text="Date:", font=("Helvetica", 12), fg="white", bg="#161313")
        date_label.grid(row=3, column=1, padx=10, pady=5, sticky=E)
        date_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        date_entry.grid(row=3, column=2, padx=10, pady=5)

        # Store
        store_label = Label(self.current_frame, text="Store:", font=("Helvetica", 12), fg="white", bg="#161313")
        store_label.grid(row=4, column=1, padx=10, pady=5, sticky=E)
        store_entry = Entry(self.current_frame, width=50, fg="white", bg="#585454")
        store_entry.grid(row=4, column=2, padx=10, pady=5)

        # Category Menu Options
        category_label = Label(self.current_frame, text="Category:", font=("Helvetica", 12), fg="white", bg="#161313")
        category_label.grid(row=5, column=1, padx=10, pady=5, sticky=E)
        categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]
        category_var = StringVar(self.current_frame)
        category_var.set(categories[0])  # set the default option
        category_menu = OptionMenu(self.current_frame, category_var, *categories)
        category_menu.config(fg="black", bg="#2c9c2b")
        category_menu["menu"].config(fg="black", bg="white")
        category_menu.grid(row=5, column=2, padx=10, pady=5)

        expense_submit = Button(self.current_frame, text="Submit", font=("Helvetica", 10), command=None, width=15, height=1, fg="black", bg="#2c9c2b")
        expense_submit.grid(row=6, column=1, columnspan=2, pady=10)

        expense_back = Button(self.current_frame, text="Back", font=("Helvetica", 10), command=self.show_main_menu, width=15, height=1, fg="black", bg="#2c9c2b")
        expense_back.grid(row=7, column=1, columnspan=2, pady=10)

    def show_income_window(self):
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

        expense_submit = Button(self.current_frame, text="Submit", font=("Helvetica", 10), command=None, width=15, height=1, fg="black", bg="#2c9c2b")
        expense_submit.grid(row=6, column=1, columnspan=2, pady=10)

        expense_back = Button(self.current_frame, text="Back", font=("Helvetica", 10), command=self.show_main_menu, width=15, height=1, fg="black", bg="#2c9c2b")
        expense_back.grid(row=7, column=1, columnspan=2, pady=10)
app = GUI_app()
app.mainloop()