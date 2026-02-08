# ATM
# Authentication, Check Account Status, balance, Withdrawl
#

class Account:
    def __init__(self, correct_pin, balance):
        self.correct_pin = correct_pin
        self.balance = balance
        self.attempts = 0
        self.status = "Active"

    def close_account(self):
        self.status = "Closed"
        print(f"\t[Action] Account status set to CLOSED.")


class ATM:
    def __init__(self):
        self.max_attempts = 3

    def start_session(self, account):
        print("\n--- STATE: IDLE ---")
        print("\t[Entry Action] Display Welcome Message")
        print("\n[Event] Card Inserted")
        self.authenticate(account)

    def authenticate(self, account):
        print("\n--- STATE: AUTHENTICATING ---")
        print("\t[Entry Action] Reset Input Buffer")

        while account.attempts < self.max_attempts:
            try:
                entered_pin = int(input(f"\t> Enter PIN (Attempt {account.attempts + 1}/{self.max_attempts}): "))
            except ValueError:
                print("\t[Error] Invalid input format.")
                continue

            print(f"\t[Event] CheckPin triggered.")

            if entered_pin == account.correct_pin:
                print("\t[Guard] PIN is Correct.")
                account.attempts = 0
                print("\t[Action] Error counter reset to 0.")
                self.check_balance_and_proceed(account)
                return
            else:
                print("   [Guard] PIN is Incorrect.")
                account.attempts += 1
                print(f"\t[Action] Error counter incremented to {account.attempts}.")
                print("\t[Exit Action] Log Attempt.")

        print("\n\t[Guard] Counter > Limit.")
        self.card_rejected()

    def card_rejected(self):
        print("\n--- STATE: CARD REJECTED ---")
        print("\t[Action] Retain Card.")
        print("\t[Transition] System resets to Idle.")

    def check_balance_and_proceed(self, account):
        print("\n--- STATE: CHECKING BALANCE ---")
        print(f"\t[Internal] Retrieving Balance: ${account.balance}")

        if account.balance == 0:
            print("\t[Guard] Balance is ZERO.")
            account.close_account()
            self.account_closed()
        else:
            print("\t[Guard] Balance is positive.")
            self.transaction_menu(account)

    def account_closed(self):
        print("\n--- STATE: ACCOUNT CLOSED ---")
        print("\t[Action] Eject Card.")
        print("\t[Message] Your account has been closed due to zero balance.")
        print("\t[Transition] Return to Idle.")

    def transaction_menu(self, account):
        print("\n--- STATE: TRANSACTION MENU ---")
        print("\t[Entry Action] Display Options (Withdraw, Exit)")

        while True:
            choice = input("\t> Choose option (1: Withdraw, 2: Exit): ")

            if choice == '1':
                self.withdraw(account)
            elif choice == '2':
                print("\n[Event] Cancel Selected")
                print("\t[Action] Eject Card")
                print("--- STATE: IDLE ---")
                return
            else:
                print("\tInvalid option.")

    def withdraw(self, account):
        print("\n--- STATE: WITHDRAWING ---")
        try:
            amount = float(input("\t> Enter amount to withdraw: "))
        except ValueError:
            return

        if amount <= account.balance:
            account.balance -= amount
            print(f"\t[Action]\t- Dispense ${amount}")
            print(f"\t[Action]\t- Update Balance to ${account.balance}")
            print("\t[Transition]\t- Return to Menu")
        else:
            print("\t[Guard]\t- Insufficient Funds.")
            print("\t[Action]\t- Show Error.")


if __name__ == "__main__":
    atm = ATM()

    print("\n\n======================================================================")
    print("SCENARIO 1: Correct PIN, Zero Balance (Triggers Account Close)")
    print("======================================================================")
    # Account with Correct PIN '1234' and Balance $0
    acc1 = Account(correct_pin=1234, balance=0)
    atm.start_session(acc1)

    print("\n\n======================================================================")
    print("SCENARIO 2: Incorrect PIN Limit (Triggers Rejection)")
    print("======================================================================")
    # Account with Correct PIN '9999', but user will (presumably) fail
    acc2 = Account(correct_pin=9999, balance=100)
    atm.start_session(acc2)

    print("\n\n======================================================================")
    print("SCENARIO 3: Correct PIN, Amount Withdrawl ")
    print("======================================================================")
    # Account with Correct PIN '1379', but user will (presumably) fail
    acc3 = Account(correct_pin=1379, balance=500)
    atm.start_session(acc3)