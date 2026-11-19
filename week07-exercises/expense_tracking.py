from datetime import datetime

def load_categories():
    categories = []
    categories_file = open('week07-exercises/categories.csv')

    lines = categories_file.readlines()
    for line in lines:
        categories.append(line.strip())
    categories_file.close()
    return categories


def display_menu():
    print("1. Add Expense")
    print("2. Total expenses of category")
    print("3. Total expenses")
    print("0. EXIT")


def add_expense(categories):
    category = input("Category: ")
    amount = float(input("Amount: "))
    day_time = datetime.now()
    if category in categories:
        s = f"{category},{amount},{day_time}\n"
        return s 
    else:
        return None 



categories = load_categories()
expenses_file = open('week07-exercises/expenses.csv', 'a')

selection = -1

while selection != 0:
    display_menu()
    selection = int(input("Select: "))
    if selection == 1:
        expense = add_expense(categories)
        if expense is not None:
            expenses_file.write(expense)
            expenses_file.flush()

expenses_file.close()
