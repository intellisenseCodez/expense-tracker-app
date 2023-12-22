"""
main.py
"""
from models import Expense, ExpenseDB
from prettytable import PrettyTable
import uuid


def draw_table(data):
    pt = PrettyTable()
    pt.field_names = ['id', 'title', 'amount', 'created_at', 'updated_at']
    
    pt.title = "Expense Tracker Database"
    # add rows
    for _ in data:
        pt.add_row([_.id, _.title, _.amount, _.created_at, _.updated_at])   
    return pt

# view the database
def view_db():
    """
    View the Database
    """
    return draw_table(data=edb.expense_db)

# populate the database with sample data
def load_sample_data():
    # create an object of expense
    expense1 = Expense("Enrolled into AltSchool", "250000")
    expense2 = Expense("Get a Pen", "200")
    expense3 = Expense("Bought a House", "5500000")
    expense4 = Expense("Apply for Visa", "35000")
    expense5 = Expense("Data Subscription", "10000")
    
    all_expenses = [expense1, expense2, expense3, expense4, expense5]
    for expense in all_expenses:
        # add each expenses to the ExpenseDB
        edb.add_expense(expense=expense)
            
    # return a table
    return draw_table(data=all_expenses)
    
    
# user can add new expense
def add_expense():
    title = input("Enter an Expense Title: ")
    amount = eval(input("Enter expense amount: "))
    
    expense = Expense(title=title, amount=amount)
    # add new expense
    edb.add_expense(expense=expense)
    print("Expense with ID:{self.id} successfully added.")
    return draw_table(data=edb.expense_db)
    

# user can update existing expense
def update_expense():
    id = uuid.UUID(input("Enter expense ID: "))
    for expense in edb.expense_db:
        if expense.id == id:
            title = input("Enter title: ") 
            amount = eval(input("Enter amount: "))
            expense.update(new_title=title, new_amount=amount)
            
    print("Expense with ID:{self.id} successfully updated.")
    return draw_table(data=edb.expense_db)
        

# user can remove existing expense
def remove_expense():
    id = input("Enter expense ID: ")
    edb.remove_expense(uuid.UUID(id))
    print("Expense with ID:{self.id} successfully removed.")
    return draw_table(data=edb.expense_db)

# user can filter existing expense by id
def get_expense_by_id():
    id = input("Enter expense ID: ")
    record = [edb.get_expense_by_id(uuid.UUID(id))]
    return draw_table(data=record)


# user can filter existing expense by title
def get_expense_by_title():
    title = input("Enter expense title: ")
    records = [edb.get_expense_by_title(title)]
    return draw_table(data=records)




if __name__ == "__main__":
    print("\nWelcome to my Expense Tracker APP.")
    print("Developer: Oyekanmi Olamilekan")
    print("Client: Alt School Fall Semester DE Project.")
    print('\n')
    
    # make an instance of the Database
    edb = ExpenseDB()
    
    while True:
        key = input("List of Operations: \n1. View Database \n2. Load Sample Expenses  \n3. Add Expense \n4. Update Expense \n5. Remove Expense \n6. Filter by ID \n7. Filter by Title \n0. Exit App \n >> ")
        if key == '0':
            print("Thanks for using our Expense Tracker")
            break
        # call default database
        match key:
            case '1':
                print(view_db())
            case '2':
                print(load_sample_data())
            case '3':
                print(add_expense())
            case '4':
                print(update_expense())
            case '5':
                print(remove_expense())
            case '6':
                print(get_expense_by_id())
            case '7':
                print(get_expense_by_title())
    
    
    
    
   
    

    
  