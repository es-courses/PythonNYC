
item_price = 1
total = 0

# Loop as long as item price is not zero
while item_price != 0:
    # Ask user for the item price
    item_price = int(input("Add price (0 to exit): "))

    # Add item price to total
    total = total + item_price

# Print the total price
print(f"Total to pay: {total}")