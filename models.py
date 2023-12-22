"""
models.py
"""
from uuid import uuid4
from datetime import datetime



class Expense():
    
    # constructor
    def __init__(self, title, amount):
        # instance variables
        self.id = uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    
    # instance methods    
    def update(self,new_title=None, new_amount=None):
        """
        Allows updating the title and/or amount, updating the updated_at timestamp.
        """
        self.title = new_title if new_title != None else self.title 
        self.amount = new_amount if new_amount != None else self.amount
        self.updated_at = datetime.now()
        
        return f"Expense with ID:{self.id} successfully updated."
            

    
    def to_dict(self,):
        """
        Returns a dictionary representation of the expense.
        """
        expense_dict = {'id':self.id, 
                        'title':self.title,
                        'amount':self.amount,
                        'created_at':self.created_at,
                        'updated_at':self.updated_at}
        return expense_dict
    
    
    def __repr__(self):
        """
        Return a string represntation of the object
        """
        class_name = type(self).__name__
        return f"{class_name}(title={self.title!r}, amount={self.amount!r})"


class ExpenseDB():
    # constructor
    def __init__(self):
        self.expense_db = list()
        
    # instance methods
    def add_expense(self, expense):
        """
        Allows to add an expense.
        """
        self.expense_db.append(expense)
        return f"An Expense with {expense.id} added successfully"
    
    def remove_expense(self, id):
        """
        Allows to remove an expense.
        """
        self.expense_db = [expense for expense in self.expense_db if expense.id != id]
        return f"An Expense with {id} removed successfully"
    
    def get_expense_by_id(self, id):
        """
        Retrieves an expense by ID.
        """
        expense = [expense for expense in self.expense_db if expense.id == id]
        if len(expense) == 0:
            return None
        
        return expense[0]
    
    def get_expense_by_title(self, title):
        """
        Retrieves expenses by title.
        """
        expense = [expense for expense in self.expense_db if expense.title == title]
        if len(expense) == 0:
            return None
        
        return expense[0]
        
    def to_dict(self):
        """
        Returns a list of dictionaries representing expenses.
        """
        expense_db_dict = {'id': [expense.id for expense in self.expense_db], 
                        'title': [expense.title for expense in self.expense_db],
                        'amount': [expense.amount for expense in self.expense_db],
                        'created_at': [expense.created_at for expense in self.expense_db],
                        'updated_at': [expense.updated_at for expense in self.expense_db]}
        return expense_db_dict
    
    def __repr__(self):
        """
        Return a string represntation of the object
        """
        class_name = type(self).__name__
        return f"{class_name}(expenses={self.expense_db!r}"

    
