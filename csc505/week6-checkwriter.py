# Check Writer

from datetime import datetime
from num2words import num2words

class Check:
    def __init__(self, date, name, purpose, amount):
        self.date = date
        self.name = name
        self.purpose = purpose
        self.amount = amount

def read_check_data() -> Check:
    date = input("Enter date: ")
    name = input("Enter name: ")
    purpose = input("Enter purpose: ")
    amount = input("Enter amount (e.g., 123.45): ")
    return Check(date, name, purpose, amount)

def validate(check) -> Check:
    try:
        # Parse the date
        check.date = datetime.strptime(check.date, '%m/%d/%Y').date()
        # Parse the amount
        check.amount = float(check.amount)
    except Exception as e:
        raise ValueError(f"Invalid check data: {e}")
    return check

def convert_amount_number_to_words(amount) -> str:
    try:
        amount = num2words(float(amount), to="currency", currency='USD')
    except ValueError:
        raise ValueError(f"Invalid amount: {amount}")
    return amount

if __name__ == "__main__":
    print("=== Check Writer ===")

    # Read inputs for check
    check = read_check_data()

    # Validate inputs
    check = validate(check)

    # Covert numeric amount into words
    check.amount = convert_amount_number_to_words(check.amount)

    print(f"{'-' * 115}")
    print(f"{' Date':25}: {check.date}")
    print(f"{' Pay to the order of':25}: {check.name}")
    print(f"{' Purpose':25}: {check.purpose}")
    print(f"{' Amount':25}: {check.amount}")
    print(f"{'-'*115}")