class BankAccount:
    """Bank account with basic balance management operations."""

    def __init__(self, account_id: int, client_id: int, account_number: int, balance: int) -> None:
        """Initializes a bank account.

        Args:
            account_id (int): Unique account identifier.
            client_id (int): Account holder client identifier.
            account_number (int): Bank account number.
            balance (int): Initial account balance.
        """
        self._account_id = account_id
        self._client_id = client_id
        self._account_number = account_number
        self._balance = balance


    @property
    def account_id(self) -> int:
        """Gets the account identifier.

        Returns:
            int: Unique account identifier.
        """
        return self._account_id


    @property
    def client_id(self) -> int:
        """Gets the client identifier.

        Returns:
            int: Account holder client identifier.
        """
        return self._client_id


    @property
    def account_number(self) -> int:
        """Gets the account number.

        Returns:
            int: Bank account number.
        """
        return self._account_number


    @account_number.setter
    def account_number(self, account_number: int) -> None:
        """Sets the account number.

        Args:
            account_number (int): New account number.
        """
        self._account_number = account_number


    @property
    def balance(self) -> int:
        """Gets the current balance.

        Returns:
            int: Available account balance.
        """
        return self._balance


    @balance.setter
    def balance(self, balance: int) -> None:
        """Sets the account balance.

        Args:
            balance (int): New account balance.
        """
        self._balance = balance


    def check_balance(self) -> int:
        """Checks the available balance.

        Returns:
            int: Current account balance.
        """
        return self.balance


    def debit(self, quantity: int) -> None:
        """Debits an amount from the balance.

        Args:
            quantity (int): Amount to debit from the account.
        """
        self.balance = self.balance - quantity


    def validate_balance_available(self, amount: int) -> bool:
        """Validates if there is sufficient balance.

        Args:
            amount (int): Amount to verify.

        Returns:
            bool: True if sufficient balance exists, False otherwise.
        """
        return self.balance - amount >= 0