import pytest
from model.bank_account import BankAccount

@pytest.fixture
def bank_account():
    return BankAccount(1, 1, 123, 1000)


def test_constructor(bank_account):
    assert isinstance(bank_account, BankAccount)
    assert bank_account.account_id == 1
    assert bank_account.client_id == 1
    assert bank_account.account_number == 123
    assert bank_account.balance == 1000
    

def test_check_balance(bank_account):
    assert bank_account.check_balance() == 1000
    assert bank_account.check_balance() != 100000
    

def test_debit(bank_account):
    bank_account.debit(100)
    assert bank_account.check_balance() == 900
    
    bank_account.debit(500)
    assert bank_account.check_balance() == 400
    
    bank_account.debit(400)
    assert bank_account.check_balance() == 0
    

@pytest.mark.parametrize("amount, expected_result", [
    (100, True),
    (500, True),
    (1200, False),
    (1001, False)
])
def test_validate_balance_available(bank_account, amount, expected_result):
    assert bank_account.validate_balance_available(amount) == expected_result