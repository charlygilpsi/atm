from model.bank_account import BankAccount
from model.atm import ATM

class Transaction:
    """Transaction that coordinates withdrawals between ATM and bank account."""

    def __init__(self, atm: ATM, bank_account: BankAccount) -> None:
        """Initializes a transaction with ATM and account.

        Args:
            atm (ATM): ATM used in the transaction.
            bank_account (BankAccount): Bank account affected.
        """
        self._atm = atm
        self._bank_account = bank_account


    @property
    def atm(self) -> ATM:
        """Gets the associated ATM.

        Returns:
            ATM: ATM used in the transaction.
        """
        return self._atm


    @atm.setter
    def atm(self, atm: ATM) -> None:
        """Sets the associated ATM.

        Args:
            atm (ATM): New ATM.
        """
        self._atm = atm


    @property
    def bank_account(self) -> BankAccount:
        """Gets the associated bank account.

        Returns:
            BankAccount: Bank account used in the transaction.
        """
        return self._bank_account


    @bank_account.setter
    def bank_account(self, bank_account: BankAccount) -> None:
        """Sets the associated bank account.

        Args:
            bank_account (BankAccount): New bank account.
        """
        self._bank_account = bank_account


    def withdraw_cash_from_atm(self, amount: int) -> None:
        """Withdraws cash from the ATM.

        Args:
            amount (int): Amount to withdraw.
        """
        self.atm.withdraw_cash(amount)


    def debit_from_account(self, amount: int) -> None:
        """Debits funds from the account.

        Args:
            amount (int): Amount to debit.
        """
        self.bank_account.debit(amount)


    def validate_withdraw_cash_from_atm(self, amount) -> bool:
        """Validates if the ATM has enough cash.

        Args:
            amount (int): Amount to verify.

        Returns:
            bool: True if enough stock exists, False otherwise.
        """
        return self.atm.validate_stock_available(amount)


    def validate_debit_from_account(self, amount) -> bool:
        """Validates if the account has enough balance.

        Args:
            amount (int): Amount to verify.

        Returns:
            bool: True if enough balance exists, False otherwise.
        """
        return self.bank_account.validate_balance_available(amount)


    def validate_amount_is_multiple_of_ten(self, amount) -> bool:
        """Validates if the amount is a multiple of ten.

        Args:
            amount (int): Amount to verify.

        Returns:
            bool: True if it is a multiple of ten, False otherwise.
        """
        return amount % 10 == 0