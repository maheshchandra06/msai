# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the amounts
# with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.

if __name__ == '__main__':
    # Ask the user to enter the charge for the food
    foodCharge = float(input("Enter the charge for the food: $"))
    if not (foodCharge > 0): raise ValueError("Invalid amount: " + str(foodCharge))

    tip = foodCharge * 0.18
    salesTax = foodCharge * 0.07

    # Calculate total amount
    total_amount = foodCharge + tip + salesTax

    # Display the amounts
    print(f"{'Charge for the food':<30} : ${foodCharge:>10.2f}")
    print(f"{'Tip (18%)':<30} : ${tip:>10.2f}")
    print(f"{'Sales Tax (7%)':<30} : ${salesTax:>10.2f}")
    print(f"{'-------------':>45}")
    print(f"{'Total amount':<30} : ${total_amount:>10.2f}")
    print(f"{'-------------':>45}")