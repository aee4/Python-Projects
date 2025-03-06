class ExpenseTracker:
    def __init__(self, expense_id: str, description: str, amount: float, date: str):
        self.expense_id = expense_id
        self.description = description
        self._amount = amount
        self.date = date

    @property
    def amount(self):
       return self._amount
    
    @amount.setter
    def amount(self, amount: float):
       if amount >= 0:
           self._amount = amount
       else:
           raise ValueError("Value should be greater than 0")
           

    def add_expenses(self,amount):
        self._amount += amount
        return self.amount
    
    

        

        

    
    
    