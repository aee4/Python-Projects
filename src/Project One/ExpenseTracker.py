class ExpenseTracker:
    def __init__(self, filename = "Expense.json" ):
       self.filename  = filename 
       self.expenses = self.load_expenses()