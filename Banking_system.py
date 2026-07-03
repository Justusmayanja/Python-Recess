# Lab 1 Exercise 1: Banking System
# Demonstrates method overloading (parent class) and method overriding (child classes)

print("=" * 50)
print("       BANKING TRANSACTION SYSTEM")
print("=" * 50)


class BankAccount:
    """Represents a bank account with a balance."""

    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"  Account Holder : {self.account_holder}")
        print(f"  Account Number : {self.account_number}")
        print(f"  Current Balance: UGX {self.balance:,.2f}")


class Transaction:
    """
    Parent class for all banking transactions.
    Demonstrates METHOD OVERLOADING through optional parameters.
    """

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.description = ""
        self.reference = ""
        self.status = "Pending"

    # ------------------------------------------------------------------
    # METHOD OVERLOADING (simulated in Python using default parameters)
    # Same method name 'process' — different behaviours based on arguments
    # ------------------------------------------------------------------

    def process(self, amount=None, description=None, reference=None):
        """
        Overloaded process method:
          process()                          -> uses stored amount only
          process(amount)                    -> uses a new amount
          process(amount, description)       -> adds a description
          process(amount, description, ref)  -> adds a reference number
        """
        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if reference is not None:
            self.reference = reference

        return self.execute()

    def execute(self):
        """Base transaction logic — overridden by child classes."""
        print("\n  [Transaction] Processing generic transaction...")
        self.status = "Completed"
        return True

    def display_receipt(self):
        """Print a standard transaction receipt."""
        print("\n  --- Transaction Receipt ---")
        print(f"  Type       : {self.__class__.__name__}")
        print(f"  Account    : {self.account.account_number}")
        print(f"  Amount     : UGX {self.amount:,.2f}")
        if self.description:
            print(f"  Description: {self.description}")
        if self.reference:
            print(f"  Reference  : {self.reference}")
        print(f"  Status     : {self.status}")
        print("  ---------------------------")


# ----------------------------------------------------------------------
# CHILD CLASSES — each OVERRIDES the parent's execute() method
# ----------------------------------------------------------------------

class Deposit(Transaction):
    """Handles deposit transactions — overrides execute()."""

    def execute(self):
        print(f"\n  [Deposit] Depositing UGX {self.amount:,.2f} "
              f"into account {self.account.account_number}...")
        self.account.balance += self.amount
        self.status = "Completed"
        print("  [Deposit] Funds credited successfully.")
        return True


class Withdrawal(Transaction):
    """Handles withdrawal transactions — overrides execute()."""

    def execute(self):
        print(f"\n  [Withdrawal] Withdrawing UGX {self.amount:,.2f} "
              f"from account {self.account.account_number}...")
        if self.amount > self.account.balance:
            self.status = "Failed — Insufficient Funds"
            print("  [Withdrawal] ERROR: Insufficient balance.")
            return False
        self.account.balance -= self.amount
        self.status = "Completed"
        print("  [Withdrawal] Funds debited successfully.")
        return True


class Transfer(Transaction):
    """Handles transfer transactions — overrides execute() and display_receipt()."""

    def __init__(self, from_account, to_account, amount):
        super().__init__(from_account, amount)
        self.to_account = to_account

    def execute(self):
        print(f"\n  [Transfer] Transferring UGX {self.amount:,.2f}")
        print(f"             From : {self.account.account_number} "
              f"({self.account.account_holder})")
        print(f"             To   : {self.to_account.account_number} "
              f"({self.to_account.account_holder})")

        if self.amount > self.account.balance:
            self.status = "Failed — Insufficient Funds"
            print("  [Transfer] ERROR: Insufficient balance.")
            return False

        self.account.balance -= self.amount
        self.to_account.balance += self.amount
        self.status = "Completed"
        print("  [Transfer] Transfer completed successfully.")
        return True

    def display_receipt(self):
        """Override receipt to show both source and destination accounts."""
        print("\n  --- Transfer Receipt ---")
        print(f"  From Account : {self.account.account_number} "
              f"({self.account.account_holder})")
        print(f"  To Account   : {self.to_account.account_number} "
              f"({self.to_account.account_holder})")
        print(f"  Amount       : UGX {self.amount:,.2f}")
        if self.description:
            print(f"  Description  : {self.description}")
        if self.reference:
            print(f"  Reference    : {self.reference}")
        print(f"  Status       : {self.status}")
        print("  ------------------------")


class Employee:
    """An employee with a linked bank account."""

    def __init__(self, name, employee_id, account):
        self.name = name
        self.employee_id = employee_id
        self.account = account

    def display_info(self):
        print(f"\n  Employee Name : {self.name}")
        print(f"  Employee ID   : {self.employee_id}")
        self.account.display_balance()


# ======================================================================
# DEMONSTRATION
# ======================================================================

# Set up accounts
employee_account = BankAccount("ACC-1001", "Mayanja Justus", 500_000.00)
colleague_account = BankAccount("ACC-2002", "Jane Smith", 150_000.00)

employee = Employee("Mayanja Justus", "EMP-06735", employee_account)

print("\n--- EMPLOYEE ACCOUNT (Before Transactions) ---")
employee.display_info()

# ------------------------------------------------------------------
# 1. DEPOSIT — method overriding (Deposit overrides execute)
#    Method overloading: process() called with description & reference
# ------------------------------------------------------------------
print("\n" + "=" * 50)
print("  TRANSACTION 1: DEPOSIT")
print("=" * 50)

deposit = Deposit(employee.account, 200_000.00)
deposit.process(description="Monthly salary top-up", reference="DEP-001")
deposit.display_receipt()

# ------------------------------------------------------------------
# 2. WITHDRAWAL — method overriding (Withdrawal overrides execute)
#    Method overloading: process() called with amount only
# ------------------------------------------------------------------
print("\n" + "=" * 50)
print("  TRANSACTION 2: WITHDRAWAL")
print("=" * 50)

withdrawal = Withdrawal(employee.account, 0)
withdrawal.process(75_000.00, description="ATM cash withdrawal")
withdrawal.display_receipt()

# ------------------------------------------------------------------
# 3. TRANSFER — method overriding (Transfer overrides execute
#    and display_receipt)
# ------------------------------------------------------------------
print("\n" + "=" * 50)
print("  TRANSACTION 3: TRANSFER")
print("=" * 50)

transfer = Transfer(employee.account, colleague_account, 100_000.00)
transfer.process(reference="TRF-003")
transfer.display_receipt()

# ------------------------------------------------------------------
# Final balances
# ------------------------------------------------------------------
print("\n" + "=" * 50)
print("  FINAL ACCOUNT BALANCES")
print("=" * 50)

print("\n--- Employee Account ---")
employee.account.display_balance()

print("\n--- Colleague Account ---")
colleague_account.display_balance()

print("\n" + "=" * 50)
print("  All transactions completed.")
print("=" * 50)
