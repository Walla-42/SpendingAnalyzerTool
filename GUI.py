from tkinter import *

class GUI_app(Tk):
    def __init__(self):
        super().__init__()

        #create the window
        self.title('Spending Analyzer Tool')
        self.geometry('700x400')

        #Welcome to Spending Analyzer Tool
        self.appIntroTitle = Label(self, text="Spending Analyzer Tool", font=("Halvetica, 42"))
        self.appIntroTitle.pack(pady=10)

        self.welcomeMessage = Label(self, text="Welcome! Select an option to get started:", font=("Halvetica, 18"))
        self.welcomeMessage.pack(pady=20)

        
        #create options buttons
        self.expenseButton = Button(self, text="Enter Expense", font=("Halvatica", 10), command=lambda: self.switch_window(expense_window), width=15, height=1)
        self.expenseButton.pack(pady=10)

        self.incomeButton = Button(self, text="Enter Income", font=("Halvatica", 10), command=None, width=15, height=1)
        self.incomeButton.pack(pady=10)

        self.incomeButton = Button(self, text="Generate Report", font=("Halvatica", 10), command=None, width=15, height=1)
        self.incomeButton.pack(pady=10)

        self.incomeButton = Button(self, text="Settings", font=("Halvatica", 10), command=None, width=15, height=1)
        self.incomeButton.pack(pady=10)
   
    def switch_window(self, window_class):
            window = window_class()
            self.destroy()
            window.mainloop()

class expense_window(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('700x400')
        self.title('Spending Analyser Tool: Expenses')

        self.window_message = Label(self, text="Enter your expenses below:", font=("Halvetica, 18"))
        self.window_message.pack(pady=10)

        self.expense_entry = Entry(self, width=50)
        self.expense_entry.pack(pady=10)

        self.expense_submit = Button(self, text="Submit", font=("Halvetica, 10"), command=None, width=15, height=1)
        self.expense_submit.pack(pady=10)

        self.expense_back = Button(self, text="Back", font=("Halvetica, 10"), command=lambda: self.switch_window(GUI_app), width=15, height=1)
        self.expense_back.pack(pady=10)
        
    def switch_window(self, window_class):
            window = window_class()
            self.destroy()
            window.mainloop()
app = GUI_app()
app.mainloop()