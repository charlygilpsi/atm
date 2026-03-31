import pytest
from model.bank_account import BankAccount
from model.atm import ATM
from model.transaction import Transaction

@pytest.fixture
def transaction():
    atm = ATM(1000)
    bank_account = BankAccount(1, 2, 123, 900)
    
    return Transaction(atm, bank_account, 400)


@pytest.fixture
def atm():
    return ATM(1000)


@pytest.fixture
def bank_account():
    return BankAccount(1, 2, 123, 900)


def test_constructor(transaction):
    assert isinstance(transaction, Transaction)
    assert isinstance(transaction.atm, ATM)
    assert isinstance(transaction.bank_account, BankAccount)
    assert transaction.atm.stock == 1000
    assert transaction.amount == 400
    assert transaction.bank_account.account_id == 1
    assert transaction.bank_account.account_number == 123
    assert transaction.bank_account.client_id == 2
    assert transaction.bank_account.balance == 900


def test_withdraw_cash_from_atm(transaction):
    transaction.withdraw_cash_from_atm()
    assert transaction.atm.stock == 600
    
    transaction.withdraw_cash_from_atm()
    assert transaction.atm.stock == 200
    
    
def test_debit_from_account(transaction):
    transaction.debit_from_account()
    assert transaction.bank_account.balance == 500
    
    transaction.debit_from_account()
    assert transaction.bank_account.balance == 100
    

@pytest.mark.parametrize("amount, expected_result", [
    (300, True),
    (500, True),
    (1100, False),
    (5000, False)
])
def test_validate_withdraw_cash_from_atm(atm, bank_account, amount, expected_result):
    assert Transaction(atm, bank_account, amount).validate_withdraw_cash_from_atm() == expected_result
    

@pytest.mark.parametrize("amount, expected_result", [
    (300, True),
    (500, True),
    (950, False),
    (1100, False)
])
def test_validate_debit_from_account(atm, bank_account, amount, expected_result):
    assert Transaction(atm, bank_account, amount).validate_debit_from_account() == expected_result
    

@pytest.mark.parametrize("amount, expected_result", [
    (10, True),
    (20, True),
    (5, False),
    (10.5, False)
])
def test_validate_amount_is_multiple_of_ten(atm, bank_account, amount, expected_result):
    assert Transaction(atm, bank_account, amount).validate_amount_is_multiple_of_ten() == expected_result