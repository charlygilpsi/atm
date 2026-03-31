class ATM:
    """Automated Teller Machine with available cash management."""

    def __init__(self, stock: int) -> None:
        """Initializes an ATM.

        Args:
            stock (int): Initial cash amount in the ATM.
        """
        self._stock = stock


    @property
    def stock(self) -> int:
        """Gets the available cash stock.

        Returns:
            int: Cash amount in the ATM.
        """
        return self._stock


    @stock.setter
    def stock(self, stock: int) -> None:
        """Sets the cash stock.

        Args:
            stock (int): New cash amount.
        """
        self._stock = stock


    def validate_stock_available(self, amount: int) -> bool:
        """Validates if there is sufficient cash in the ATM.

        Args:
            amount (int): Amount to verify.

        Returns:
            bool: True if sufficient cash exists, False otherwise.
        """
        return self.stock - amount >= 0


    def withdraw_cash(self, amount: int) -> None:
        """Withdraws cash from the ATM.

        Args:
            amount (int): Amount to withdraw.
        """
        self.stock = self.stock - amount