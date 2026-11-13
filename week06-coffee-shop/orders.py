import csv 
from datetime import datetime

def load_store_menu():
    """ Read store menu from csv file, put in a dictionary and return """
    store_menu = {}
    file = open('week06-coffee-shop/storemenu.csv')
    reader = csv.DictReader(file)
    for row in reader:
        beverage = row['beverage']
        price = float(row['price'])
        store_menu[beverage] = price
    return store_menu


def display_store_menu(store_menu):
    print("=== BEVERAGES ===")
    for key in store_menu:
        if len(key) < 6:
            print(f"{key}:\t\t{store_menu[key]}")
        else:
            print(f"{key}:\t{store_menu[key]}")


def get_user_selction():
    """ Prompt user to select and return selection """
    sel = -1
    try:
        sel = int(input("Select > "))
    except ValueError:
        print("ERROR: Please give integer values only")
    return sel


def display_user_menu():
    print("=== APP MENU ===")
    print("1. Add Order")
    print("2. Orders by Customer")
    print("3. Orders by Beverage")
    print("0. EXIT")

def add_order(store_menu):
    print("--- Add Order ---")
    try:
        cust = input("Customer: ")
        bev = input("Beverage: ")
        quant = int(input("Quantity: "))
        dt = str(datetime.now()) 
        price = store_menu[bev]
        file = open('week06-coffee-shop/orders.csv', 'a')
        file.write(f"{cust},{bev},{price},{quant},{dt}\n")
        file.close()
        print(">>>>>>> Order added")
    except ValueError:
        print("ERROR: Quantity must be a number")
    except KeyError:
        print("ERROR: Beverage not found")


def open_orders_file_for_reading():
    file = open("week06-coffee-shop/orders.csv")
    reader = csv.DictReader(file)
    return reader


def orders_of_customer():
    cust = input("Customer: ")
    reader = open_orders_file_for_reading()
    counter = 0
    for row in reader:
        if row['customer'] == cust:
            counter += 1
            print(row)
    if counter == 0:
        print("No orders found")
    else:
        print(f"{counter} orders found")


store_menu = load_store_menu()

selection = -1

while selection != 0:
    display_store_menu(store_menu)
    display_user_menu()
    selection = get_user_selction()
    match selection:
        case 1:
            add_order(store_menu)
        case 2:
            orders_of_customer()
        case 3: 
            print("by bev")
        case 0:
            print("Bye!")
        case _:
            print("Invalid selection")