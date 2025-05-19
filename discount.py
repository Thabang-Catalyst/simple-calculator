#function that calculates the final price after applying a discount.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: R"))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: R{final_price:.2f}")
    else:
        print(f"No discount applied. Final price: R{final_price:.2f}")
except ValueError:
    print("Enter valid numeric values.")
