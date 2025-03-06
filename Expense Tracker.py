class Expense_Tracker:
    def __init__(self, expense_id, description, amount, date):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.date = date



    @property
    def get_expense_id(self):
       return self.expense_id
    
    
    