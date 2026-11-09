# Program name: Point_Of_Sales.py
# Description: Console food ordering for Evan's Eatery. Shows a menu, takes orders
#    until the user types done, totals them and simulates payment at checkout.
# Author: Exanes, Evan Prens
# Date Compiled: 10/17/2025
# ======================================================================
# Date           Description                      Programmer name
# ======================================================================
# 10/17/2025     Initial Implementation           EPPE
# 11/09/2026     Added header and comments;       EPPE with Claude
#                moved to the repo root
# 11/09/2026     Corrected DINUGUAN spelling      EPPE with Claude
# 11/09/2026     Added function comments          EPPE with Claude
# ======================================================================

def welcome():
    """Print the greeting that opens the program."""
    print("🍽️ Welcome to Evan's Eatery POS System!")  
    print("Please select from the menu below:\n")

def show_menu(menu):
    """Print every menu item with its price, one per line."""
    print("📋 MENU")
    for item, price in menu.items():
        print(f"{item} - ₱{price}")
    print()

def take_order(menu):
    """Ask for item names until the user types "done", and return the chosen items in order.

    Input is upper-cased to match the menu keys. The same item can be ordered more than once.
    """
    order = []
    # Each pass takes one item. Typing DONE is the only way out.
    while True:
        choice = input("Enter item name to order (or type 'done' to finish): ").upper()
        if choice == 'DONE':
            break
        elif choice in menu:
            order.append(choice)
            print(f"✅ {choice} added to your order.")
        else:
            print("❌ Item not found. Please try again.")
    return order

def calculate_total(order, menu):
    """Add up the menu price of each ordered item. An item ordered twice is counted twice."""
    total = sum(menu[item] for item in order)
    return total

def checkout(order, total):
    """Print the itemised order and the total, then simulate payment.

    Prices are read from the module-level menu, not passed in.
    """
    print("\n🧾 CHECKOUT")
    print("Your order summary:")
    for item in order:
        print(f"- {item} - ₱{menu[item]}")
    print(f"Total: ₱{total}")
    input("Press Enter to simulate payment... 💳")
    print("✅ Payment successful! Thank you for dining with us.")

# Prices are in pesos. Item names are upper case because take_order upper-cases what the user types.
menu = {
    "MENUDO": 100,
    "ADOBO": 120,
    "SINIGANG": 130,
    "LECHON": 150,
    "LUMPIA": 80,
    "DINUGUAN": 80,
    "PAPAITAN":80,
    "PASTIL": 50
}

# Runs as soon as the file is loaded: there is no main() guard.
welcome()
show_menu(menu)
order = take_order(menu)
total = calculate_total(order, menu)
checkout(order, total)
