from decimal import Decimal
from app.split_evenly import split_evenly
import pytest

# Edge Case: num_people < 0 or not an integer


def test_num_people_invalid():
    with pytest.raises(ValueError):
        split_evenly(100, -1)  # negative people
    with pytest.raises(ValueError):
        split_evenly(100, 0)  # zero people
    with pytest.raises(ValueError):
        split_evenly(100, 2.5)  # not an integer

def test_total_amt_invalid():
    with pytest.raises(ValueError):
        split_evenly(0, 3)  # bill is $0
    with pytest.raises(ValueError):
        split_evenly(-100, 3) # bill is negative

def test_even_split():
    result = split_evenly(50, 5)
    assert result == [Decimal("10.00"),Decimal("10.00"),
                      Decimal("10.00"),Decimal("10.00"),
                      Decimal("10.00")]

