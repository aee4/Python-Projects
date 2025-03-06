import json
class Expense:
    def __init__(self, expense_id: str, description: str, amount: float, date: str):
        self.expense_id = expense_id
        self.description = description
        self._amount = amount
        self.date = date

    def json_form(self):
        return {
            "expense_id": self.expense_id,
            "description": self.description,
            "amount": self._amount,
            "date": self.date
            }

   
    

        

        

    
    
    