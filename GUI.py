from tkinter import *

class GUI_app(Tk):
    def __init__(self):
        super().__init__()

        #create the window
        self.title('Spending Analyzer Tool')
        self.geometry('600x400')

        #Welcome to Spending Analyzer Tool
        self.appIntroTitle = Label(self, text="Spending Analyzer Tool", font=("Halvetica, 42"))
        self.appIntroTitle.pack(pady=10)

        self.welcomeMessage = Label(self, text="Welcome! Select an option to get started:", font=("Halvetica, 20"))
        self.welcomeMessage.pack(pady=20)

        
        #create options buttons
        self.expenseButton = Button(self, text="Enter Expense", font=("Halvatica", 12), commmand=None, width=10, height=1)
        self.expenseButton.pack(pady=10)

        self.incomeButton = Button(self, text="Enter Income", font=("Halvatica", 12), command=None, width=10, height=1)
        self.incomeButton.pack(pady=10)

        self.incomeButton = Button(self, text="Generate Report", font=("Halvatica", 12), command=None, width=10, height=1)
        self.incomeButton.pack(pady=10)

        self.incomeButton = Button(self, text="Settings", font=("Halvatica", 12), command=None, width=10, height=1)
        self.incomeButton.pack(pady=10)

app = GUI_app()
app.mainloop()