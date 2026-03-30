import pytest
from model.bank_account import BankAccount
from model.atm import ATM
from model.transaction import Transaction

@pytest.fixture
def transaction():
    atm = ATM(1000)
    bank_account = BankAccount(1, 1, 123, 1000)
    
    return Transaction(atm, bank_account)


def test_withdraw_cash_from_atm(transaction):
    transaction.withdraw_cash_from_atm(100)
    assert transaction.atm.stock == 900
    
    transaction.withdraw_cash_from_atm(300)
    assert transaction.atm.stock == 600
    