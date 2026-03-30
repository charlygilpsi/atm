import pytest
from model.bank_account import BankAccount
from model.atm import ATM
from model.transaction import Transaction

@pytest.fixture
def transaction():
    atm = ATM(1000)
    bank_account = BankAccount(1, 2, 123, 900)
    
    return Transaction(atm, bank_account)


def test_constructor(transaction):
    assert isinstance(transaction, Transaction)
    assert isinstance(transaction.atm, ATM)
    assert isinstance(transaction.bank_account, BankAccount)
    assert transaction.atm.stock == 1000
    assert transaction.bank_account.account_id == 1
    assert transaction.bank_account.account_number == 123
    assert transaction.bank_account.client_id == 2
    assert transaction.bank_account.balance == 900


def test_withdraw_cash_from_atm(transaction):
    transaction.withdraw_cash_from_atm(100)
    assert transaction.atm.stock == 900
    
    transaction.withdraw_cash_from_atm(300)
    assert transaction.atm.stock == 600
    