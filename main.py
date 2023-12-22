"""
main.py
"""
from models import Expense, ExpenseDB
# import pretty_table_printer




if __name__ == "__main__":
    print("Welcome to my Expense Tracker APP.")
    print("#"*20)
    
    # create an object of expense
    expense1 = Expense("Enrolled into AltSchool", "250000")
    expense2 = Expense("Get a Pen", "200")
    expense3 = Expense("Bought a House", "5500000")
    expense4 = Expense("Apply for Visa", "35000")
    expense5 = Expense("Data Subscription", "10000")
    
    all_expenses = [expense1, expense2, expense3, expense4, expense5]
    
    # add an expense to the database
    edb = ExpenseDB()
    print("Initializing Database")
    print(edb.expense_db)
    
    print("Add New Expense")
    edb.add_expense(expense1)
    print(edb.expense_db)
    
    print("Add another Expense")
    edb.add_expense(expense2)
    print(edb.expense_db)
    
    # print("Remove an Expense")
    # edb.remove_expense(expense2.id)
    # print(edb.expense_db)
    
    # print("Get an Expense")
    # print(edb.get_expense_by_id(expense2.id))
    
    print("Get an Expense")
    print(edb.get_expense_by_title(expense1.title))
    
    
  