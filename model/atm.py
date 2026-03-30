class ATM:
    def __init__(self, stock: int) -> None:
        self._stock = stock
        
    
    @property
    def stock(self) -> int:
        return self._stock
    
    
    @stock.setter
    def stock(self, stock: int) -> None:
        self._stock = stock
        
    
    def validate_stock_available(self, amount: int) -> bool:
        return self.stock - amount >= 0
    
    
    def withdraw_cash(self, amount: int) -> None:
        self.stock = self.stock - amount