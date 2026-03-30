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