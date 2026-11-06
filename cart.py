#Name: Armeen Farooqui
#Period: AM

import datetime
# Store inventory with five products and their prices
products = {
    "Gaming Mouse": 25.99,
    "Mechanical Keyboard": 59.99,
    "USB Headset": 34.99,
    "Mouse Pad": 12.50,
    "USB Flash Drive": 9.99
}
shopping_cart = {}


# Function to display all available products
def display_products(products):
    print("\nAVAILABLE PRODUCTS")

    number = 1
    for name, price in products.items():
        print(number, name, "$", price)
        number += 1

    # Return product names
    return list(products.keys())

# 2. Add products to cart
def add_product(products, shopping_cart):

    # Show products
    product_names = display_products(products)

    # Ask which product
    choice = int(input("Enter product number: "))

    # Check if choice is valid
    while choice < 1 or choice > 5:
        print("Invalid number!")
        choice = int(input("Enter product number: "))

    # Get product name
    product = product_names[choice - 1]

    # Ask for quantity
    quantity = int(input("How many do you want? "))

    # Make sure quantity is more than 0
    while quantity <= 0:
        print("Enter a number bigger than 0!")
        quantity = int(input("How many do you want? "))

    # Add product to cart
    if product in shopping_cart:
        shopping_cart[product] = shopping_cart[product] + quantity
    else:
        shopping_cart[product] = quantity

    print("Product added!")
    print("You now have", shopping_cart[product])


def remove_product(shopping_cart):

    # Check if cart is empty
    if len(shopping_cart) == 0:
        print("Your cart is empty!")
        return

    # Show products in cart
    names = list(shopping_cart.keys())

    number = 1

    for product, quantity in shopping_cart.items():
        print(number, product, "Quantity:", quantity)
        number = number + 1

    # Ask which product to remove
    choice = int(input("Enter item number: "))

    # Check if number is correct
    while choice < 1 or choice > len(names):
        print("Wrong number!")
        choice = int(input("Enter item number: "))

    # Find product
    product = names[choice - 1]

    # Remove one item
    shopping_cart[product] = shopping_cart[product] - 1

    # Delete product if quantity is 0
    if shopping_cart[product] == 0:
        del shopping_cart[product]

    print("One item removed!")


def calculate_total(products, shopping_cart):

    total = 0

    # Calculate each product price
    for product, quantity in shopping_cart.items():
        total = total + products[product] * quantity

    return total


# Function to show the shopping cart
def display_cart(products, shopping_cart):

    if len(shopping_cart) == 0:
        print("Your cart is empty!")
        return

    print("\nYOUR SHOPPING CART")

    total_items = 0

    for product in shopping_cart:

        quantity = shopping_cart[product]
        price = products[product]
        total = price * quantity

        print("Product:", product)
        print("Price: $", price)
        print("Quantity:", quantity)
        print("Total: $", total)

        total_items = total_items + quantity

    print("Total Items:", total_items)

    total = calculate_total(products, shopping_cart)

    print("Subtotal:", total)

# Function to calculate the discount
def calculate_discount(total):
    if total < 10:
        discount = 0
    elif total < 20:
        discount = 0.05
    elif total < 40:
        discount = 0.10
    else:
        discount = 0.15

    return discount


# Function to checkout
def checkout(products, shopping_cart):

    # Do not checkout if cart is empty
    if len(shopping_cart) == 0:
        print("Your cart is empty! Add products first.")
        return False

    # Calculate subtotal
    total = calculate_total(products, shopping_cart)

    # Calculate discount
    discount = calculate_discount(total)

    # Calculate savings
    saved = total * discount

    # Calculate final price
    final_total = total - saved

    # Get today's date
    today = datetime.date.today()

    # Print receipt
    print("\n========== RECEIPT ==========")
    print("Date:", today.strftime("%m/%d/%Y"))

    total_items = 0

    # Show purchased products
    for product, quantity in shopping_cart.items():

        price = products[product]
        line_total = price * quantity

        print("\nProduct:", product)
        print("Unit Price: $", format(price, ".2f"))
        print("Quantity:", quantity)
        print("Line Total: $", format(line_total, ".2f"))

        total_items = total_items + quantity

    # Show final receipt information
    print("\nTotal Items:", total_items)
    print("Subtotal: $", format(total, ".2f"))
    print("Discount:", format(discount * 100, ".0f"), "%")
    print("Amount Saved: $", format(saved, ".2f"))
    print("Final Total: $", format(final_total, ".2f"))

    print("\nThank you for shopping!")

    return True

# Main menu
while True:

    # Show menu choices
    print("\n========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")

    # Ask customer for a choice
    choice = int(input("\nEnter your choice: "))

    # Check if choice is correct
    while choice < 1 or choice > 6:
        print("Invalid choice!")
        choice = int(input("Enter your choice: "))

    # Option 1: Show products
    if choice == 1:
        display_products(products)

    # Option 2: Add products
    elif choice == 2:
        add_product(products, shopping_cart)

    # Option 3: Remove products
    elif choice == 3:
        remove_product(shopping_cart)

    # Option 4: Show shopping cart
    elif choice == 4:
        display_cart(products, shopping_cart)

    # Option 5: Show current total
    elif choice == 5:
        total = calculate_total(products, shopping_cart)
        print("Current Total: $", format(total, ".2f"))

    # Option 6: Checkout
    elif choice == 6:
        if checkout(products, shopping_cart):
            break