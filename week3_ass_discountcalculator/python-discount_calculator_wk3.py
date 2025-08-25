def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    else:
        return price

input_price = float(input("Enter the price: "))
input_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(input_price, input_percentage)
if input_percentage >= 20:
    print(f"The final price after discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The price is: {final_price:.2f}")