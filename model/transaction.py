from atm import ATM
from bank_account import BankAccount

class Transaction:
    def __init__(self, atm: ATM, bank_account: BankAccount) -> None:
        self._atm = atm
        self._bank_account = bank_account
        
    
    @property
    def atm(self) -> ATM:
        return self._atm
    
    
    @atm.setter
    def atm(self, atm: ATM) -> None:
        self._atm = atm
        
    
    @property
    def bank_account(self) -> BankAccount:
        return self._bank_account
    
    
    @bank_account.setter
    def bank_account(self, bank_account: BankAccount) -> None:
        self._bank_account = bank_account
        
    
    def withdraw_cash_from_atm(self, amount: int) -> None:
        self.atm.withdraw_cash(amount)
        
    
    def debit_from_account(self, amount: int) -> None:
        self.bank_account.debit(amount)
        
    
    def validate_withdraw_cash_from_atm(self, amount) -> bool:
        return self.atm.validate_stock_available(amount)
    
    
    def validate_debit_from_account(self, amount) -> bool:
        return self.bank_account.validate_balance_available(amount)
    
    
    def validate_amount_is_multiple_of_ten(self, amount) -> bool:
        return amount % 10 == 0