from model.bank_account import BankAccount
from model.atm import ATM

class Transaction:
    """Transaction that coordinates withdrawals between ATM and bank account."""

    def __init__(self, atm: ATM, bank_account: BankAccount, amount: int) -> None:
        """Initializes a transaction with ATM and account.

        Args:
            atm (ATM): ATM used in the transaction.
            bank_account (BankAccount): Bank account affected.
            amount (int): Amount of cash to withdraw from the ATM and the bank account.
        """
        self._atm = atm
        self._bank_account = bank_account
        self._amount = amount


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
        
    
    @property
    def amount(self) -> int:
        """Gets the associated amount.

        Returns:
            amount: Amount of cash to withdraw from the ATM and the bank account.
        """
        return self._amount
    
    
    @amount.setter
    def amount(self, amount: int) -> None:
        """Sets the amount of cash to withdraw from the ATM and the bank account.

        Args:
            amount (int): New amount of cash to withdraw from the ATM and the bank account.
        """


    def withdraw_cash_from_atm(self) -> None:
        """Withdraws cash from the ATM."""
        self.atm.withdraw_cash(self.amount)


    def debit_from_account(self) -> None:
        """Debits funds from the account."""
        self.bank_account.debit(self.amount)


    def validate_withdraw_cash_from_atm(self) -> bool:
        """Validates if the ATM has enough cash."""
        return self.atm.validate_stock_available(self.amount)


    def validate_debit_from_account(self) -> bool:
        """Validates if the account has enough balance."""
        return self.bank_account.validate_balance_available(self.amount)


    def validate_amount_is_multiple_of_ten(self) -> bool:
        """Validates if the amount is a multiple of ten."""
        return self.amount % 10 == 0