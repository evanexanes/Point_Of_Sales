# Food POS System

# Welcome statement with emoji to be more enganging
def welcome():
    print("🍽️ Welcome to Evan's Eatery POS System!")  
    print("Please select from the menu below:\n")

def show_menu(menu):
    print("📋 MENU")
    for item, price in menu.items():
        print(f"{item} - ₱{price}")
    print()

def take_order(menu):
    order = []
    while True: # nag decalare ako ng while loop para magtuloy tuloy ang order at mag end pag nag declare na ang user input ng DONE (sa break)
        choice = input("Enter item name to order (or type 'done' to finish): ").upper()
        if choice == 'DONE':
            break
        elif choice in menu:
            order.append(choice)
            print(f"✅ {choice} added to your order.")
        else:
            print("❌ Item not found. Please try again.")
    return order

# for calculation ng order
def calculate_total(order, menu):
    total = sum(menu[item] for item in order)
    return total

# Print for your check order
def checkout(order, total):
    print("\n🧾 CHECKOUT")
    print("Your order summary:")
    for item in order:
        print(f"- {item} - ₱{menu[item]}")
    print(f"Total: ₱{total}")
    input("Press Enter to simulate payment... 💳")
    print("✅ Payment successful! Thank you for dining with us.")

# Food Menu of Evan's Eatery and it's Price
menu = {
    "MENUDO": 100,
    "ADOBO": 120,
    "SINIGANG": 130,
    "LECHON": 150,
    "LUMPIA": 80,
    "DINIGUGAN": 80,
    "PAPAITAN":80,
    "PASTIL": 50
}

# For running the full POS system: show welcome, display menu, take order, calculate total, and checkout
welcome()
show_menu(menu)
order = take_order(menu)
total = calculate_total(order, menu)
checkout(order, total)
