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
    
    
def test_debit_from_account(transaction):
    transaction.debit_from_account(100)
    assert transaction.bank_account.balance == 800
    
    transaction.debit_from_account(600)
    assert transaction.bank_account.balance == 200
    
    transaction.debit_from_account(200)
    assert transaction.bank_account.balance == 0
    

@pytest.mark.parametrize("amount, expected_result", [
    (300, True),
    (500, True),
    (1100, False),
    (5000, False)
])
def test_validate_withdraw_cash_from_atm(transaction, amount, expected_result):
    assert transaction.validate_withdraw_cash_from_atm(amount) == expected_result
    

@pytest.mark.parametrize("amount, expected_result", [
    (300, True),
    (500, True),
    (950, False),
    (1100, False)
])
def test_validate_debit_from_account(transaction, amount, expected_result):
    assert transaction.validate_debit_from_account(amount) == expected_result
    

@pytest.mark.parametrize("amount, expected_result", [
    (10, True),
    (20, True),
    (5, False),
    (10.5, False)
])
def test_validate_amount_is_multiple_of_ten(transaction, amount, expected_result):
    assert transaction.validate_amount_is_multiple_of_ten(amount) == expected_result