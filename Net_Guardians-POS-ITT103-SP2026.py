
# BEST BUY RETAIL POS SYSTEM program code


# Products in the POS system  (name: [price, stock])
products = {
    "rice": [500, 20],
    "flour": [300, 15],
    "milk": [150, 25],
    "bread": [200, 30],
    "eggs": [400, 10],
    "Box juice": [250, 18],
    "sugar": [350, 12],
    "soap": [100, 40],
    "detergent": [600, 8],
    "water": [120, 50],
    "Toilet paper": [160, 150],
    "Syrup": [460, 350],
    "Bun": [520, 450],
    "salfish": [120, 550],
    "Nuggets": [70, 850],
    "Bacon": [80, 950],
    "chocolate bar": [140, 250]
}

cart = {}



# Functions used in code


# Function used to display products
def display_products():
    print("\n--- Best Buy Retail Product List---")
    for item, details in products.items():
        print(f"{item.capitalize()} - Price: ${details[0]} | Stock: {details[1]}")

# Function used  add items to cart
def add_to_cart():
    item = input("Enter product name: ").lower()

    if item not in products:
        print("This Product is not in the system!")
        return

    # Program to provide exception errors in code

    try:
        qty = int(input("Enter quantity: "))
    except:
        print("Wrong quantity entered!")
        return

    if qty <= 0:
        print("Quantity entered must be greater than 0!")
        return

    if qty > products[item][1]:
        print("Not enough stock available!")
        return

    # Add to cart
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    products[item][1] -= qty
    print("Item has been added to cart!")

# Function used to remove items from cart
def remove_from_cart():
    item = input("Enter item to be removed: ").lower()

    if item not in cart:
        print("Item is not in cart!")
        return

    qty = int(input("Enter quantity to be removed: "))

    if qty >= cart[item]:
        products[item][1] += cart[item]
        del cart[item]
    else:
        cart[item] -= qty
        products[item][1] += qty

    # Displays that item has been removed

    print("Item has been removed!")

# Function used to view stock
def view_cart():
    print("\n--- Best Buy Retail Shopping Cart ---")
    total = 0

    for item, qty in cart.items():
        price = products[item][0]
        item_total = price * qty
        total += item_total
        print(f"{item.capitalize()} x{qty} = ${item_total}")

    print(f"Subtotal: ${total}")

# Function used to check out items
def checkout():
    if not cart:
        print("Shopping Cart is empty!")
        return

    subtotal = sum(products[item][0] * qty for item, qty in cart.items())

    # # Program calculate customer discount

    discount = 0
    if subtotal > 5000:
        discount = subtotal * 0.05

    tax = (subtotal - discount) * 0.10
    total = subtotal - discount + tax

    # Displays items that are checked out

    print("\n--- Best Buy Retail CHECKOUT ---")
    print(f"Subtotal: ${subtotal}")
    print(f"Discount: ${discount}")
    print(f"Tax (10%): ${tax}")
    print(f"Total: ${total}")

    # Program to prevent exception errors in code

    while True:
        try:
            payment = float(input("Enter payment: "))
            if payment < total:
                print("Insufficient payment made!")
            else:
                break
        except:
            print("The value enter is wrong !")

    change = payment - total
    generate_receipt(subtotal, discount, tax, total, payment, change)

# Function used to generate receipt
def generate_receipt(subtotal, discount, tax, total, payment, change):
    print("\n===== BEST BUY RETAIL =====")
    print("------ RECEIPT ------")

    for item, qty in cart.items():
        price = products[item][0]
        print(f"{item.capitalize()} x{qty} @ ${price} = ${price * qty}")

    # Displays the outputs for the user to see what they have bought

    print("--------------------------")
    print(f"Subtotal: ${subtotal}")
    print(f"Discount: ${discount}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")
    print(f"Paid: ${payment}")
    print(f"Change: ${change}")
    print("\nThank you for shopping with us and come again!")
    print("===========================")

    cart.clear()

# Function used to show low stock
def low_stock_alert():
    print("\n--- Best Buy Retail Low Stock alert---")
    for item, details in products.items():
        if details[1] < 5:
            print(f"{item.capitalize()} is low on stock! ({details[1]} is left)")



# Program main menu loop
# Function to print main menu
def main():
    while True:
        print("\n===== Best Buy Retail POS MENU =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        # Prompt to enter choice selection

        choice = input("Choose option: ")

        # IF statements to select the correct option needed by the user
        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Exiting system... Thank for using Best Buy Retail POS. Have a great day")
            break
        else:
            print("Incorrect value enter, please try again!")
        # This calls for low stock function if there is low stock
        low_stock_alert()


# Used to run main program
main()
