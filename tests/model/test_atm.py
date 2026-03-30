import pytest
from model.atm import ATM

@pytest.fixture
def atm():
    return ATM(1000)


def test_constructor(atm):
    assert isinstance(atm, ATM)
    assert atm.stock == 1000
    

@pytest.mark.parametrize("amount, expected_result", [
    (100, True),
    (200, True),
    (1000, True),
    (1001, False),
    (22000, False)
])
def test_validate_stock_available(atm, amount, expected_result):
    assert atm.validate_stock_available(amount) == expected_result
    

def test_withdraw_cash(atm):
    atm.withdraw_cash(800)
    assert atm.stock == 200
    
    atm.withdraw_cash(100)
    assert atm.stock == 100
    
    atm.withdraw_cash(100)
    assert atm.stock == 0