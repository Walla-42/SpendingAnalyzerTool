from program_files.server_class import Server

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


