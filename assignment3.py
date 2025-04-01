def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompting the user for the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)


    if final_price != price:
        print(f"The final price after applying the discount is: {final_price}")
    else:
        print("No discount applied. The original price is:", price)
except ValueError:
    print("Please enter valid numeric inputs for price and discount percentage.")