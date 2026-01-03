# Tip Calculator

def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    total = bill_amount + tip
    return tip, total

if __name__ == "__main__":
    try:
        bill = float(input("Enter the bill amount in $ "))
        tip_percent = float(input("Enter tip percentage (e.g., 15 for 15%): "))

        tip, total = calculate_tip(bill, tip_percent)

        print("\n"+"------ Receipt ------".center(35))
        print(f"{'Bill amount':25}: ${bill:10.2f}")
        print(f"{'Tip amount':25}: ${tip:10.2f}")
        print(f"{'Total bill (with tip)':25}: ${total:10.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")