class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a BankAccount instance.

        Args:
        initial_balance (float): The initial account balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
        amount (float): The amount to deposit.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.

        Args:
        amount (float): The amount to withdraw.

        Returns:
        bool: True if the withdrawal is successful, False otherwise.
        """
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        """
        Prints the current account balance.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
