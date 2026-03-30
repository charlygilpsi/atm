class BankAccount:
    def __init__(self, account_id: int, client_id: int, account_number: int, balance: int) -> None:
        self._account_id = account_id
        self._client_id = client_id
        self._account_number = account_number
        self._balance = balance
    
    
    @property
    def account_id(self) -> int:
        return self._account_id


    @property
    def client_id(self) -> int:
        return self._client_id
    
    
    @client_id.setter
    def client_id(self, client_id: int) -> None:
        self._client_id = client_id
    
    
    @property
    def account_number(self) -> int:
        return self._account_number
    
    
    @account_number.setter
    def account_number(self, account_number: int) -> None:
        self._account_number = account_number
    
    
    @property
    def balance(self) -> int:
        return self._balance
    
    
    @balance.setter
    def balance(self, balance: int) -> None:
        self._balance = balance
    
    
    def check_balance(self) -> int:
        return self.balance
    
    
    def debit(self, quantity: int) -> None:
        self.balance = self.balance - quantity
        
    
    def validate_balance_available(self, amount: int) -> bool:
        return self.balance - amount >= 0