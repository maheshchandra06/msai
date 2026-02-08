import sys

class Account:
    def __init__(self, correct_pin, balance):
        self.correct_pin = correct_pin
        self.balance = balance
        self.attempts = 0
        self.status = "Active"

    def close_account(self):
        self.status = "Closed"
        print(f"   [Action] Account status set to CLOSED.")


class ATM:
    def __init__(self):
        self.max_attempts = 3

    def start_session(self, account):
        """
        Main execution flow representing the State Machine.
        """
        # --- STATE: IDLE ---
        print("\n--- STATE: IDLE ---")
        print("   [Entry Action] Display Welcome Message")

        # Transition: Insert Card
        print("\n[Event] Card Inserted")
        self.authenticate(account)

    def authenticate(self, account):
        # --- STATE: AUTHENTICATING ---
        print("\n--- STATE: AUTHENTICATING ---")
        print("   [Entry Action] Reset Input Buffer")

        while account.attempts < self.max_attempts:
            # Simulate User Input
            try:
                entered_pin = int(input(f"   > Enter PIN (Attempt {account.attempts + 1}/{self.max_attempts}): "))
            except ValueError:
                print("   [Error] Invalid input format.")
                continue

            # Event: CheckPin
            print(f"   [Event] CheckPin triggered.")

            if entered_pin == account.correct_pin:
                # --- GUARD: PIN Correct ---
                print("   [Guard] PIN is Correct.")

                # Action: Reset Counter
                account.attempts = 0
                print("   [Action] Error counter reset to 0.")

                # Transition to Checking Balance Logic
                self.check_balance_and_proceed(account)
                return
            else:
                # --- GUARD: PIN Incorrect ---
                print("   [Guard] PIN is Incorrect.")

                # Action: Increment Error Counter
                account.attempts += 1
                print(f"   [Action] Error counter incremented to {account.attempts}.")

                # Exit Action loop logic (Internal Transition)
                print("   [Exit Action] Log Attempt.")

        # If loop finishes, Limit is reached
        # --- GUARD: Counter > Limit ---
        print("\n   [Guard] Counter > Limit.")
        self.card_rejected()

    def card_rejected(self):
        # --- STATE: CARD REJECTED ---
        print("\n--- STATE: CARD REJECTED ---")
        print("   [Action] Retain Card.")
        print("   [Transition] System resets to Idle.")

    def check_balance_and_proceed(self, account):
        # --- STATE: CHECKING BALANCE ---
        print("\n--- STATE: CHECKING BALANCE ---")
        print(f"   [Internal] Retrieving Balance: ${account.balance}")

        if account.balance == 0:
            # --- GUARD: Balance == 0 ---
            print("   [Guard] Balance is ZERO.")

            # Action: Close Account
            account.close_account()

            # Transition
            self.account_closed()
        else:
            # --- GUARD: Balance > 0 ---
            print("   [Guard] Balance is positive.")

            # Transition
            self.transaction_menu(account)

    def account_closed(self):
        # --- STATE: ACCOUNT CLOSED ---
        print("\n--- STATE: ACCOUNT CLOSED ---")
        print("   [Action] Eject Card.")
        print("   [Message] Your account has been closed due to zero balance.")
        print("   [Transition] Return to Idle.")

    def transaction_menu(self, account):
        # --- STATE: TRANSACTION MENU ---
        print("\n--- STATE: TRANSACTION MENU ---")
        print("   [Entry Action] Display Options (Withdraw, Exit)")

        while True:
            choice = input("   > Choose option (1: Withdraw, 2: Exit): ")

            if choice == '1':
                # Transition: Select Withdrawal
                self.withdraw(account)
            elif choice == '2':
                # Transition: Cancel
                print("\n[Event] Cancel Selected")
                print("   [Action] Eject Card")
                print("--- STATE: IDLE ---")
                return
            else:
                print("   Invalid option.")

    def withdraw(self, account):
        # --- STATE: WITHDRAWING ---
        print("\n--- STATE: WITHDRAWING ---")
        try:
            amount = float(input("   > Enter amount to withdraw: "))
        except ValueError:
            return

        if amount <= account.balance:
            account.balance -= amount
            print(f"   [Action] Dispense ${amount}")
            print(f"   [Action] Update Balance to ${account.balance}")
            # Transition back to Menu
            print("   [Transition] Return to Menu")
        else:
            print("   [Guard] Insufficient Funds.")
            print("   [Action] Show Error.")


# --- RUN THE SIMULATION ---
if __name__ == "__main__":
    # Create the ATM system
    atm = ATM()

    print("==========================================")
    print("SCENARIO 1: Correct PIN, Zero Balance (Triggers Account Close)")
    print("==========================================")
    # Account with Correct PIN '1234' and Balance $0
    acc1 = Account(correct_pin=1234, balance=0)
    atm.start_session(acc1)

    print("\n\n==========================================")
    print("SCENARIO 2: Incorrect PIN Limit (Triggers Rejection)")
    print("==========================================")
    # Account with Correct PIN '9999', but user will (presumably) fail
    acc2 = Account(correct_pin=9999, balance=100)
    atm.start_session(acc2)