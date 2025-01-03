import pytest
from src.is_even_or_odd import is_even_or_odd

def test_is_even_or_odd():
    assert is_even_or_odd(2) == "even"
    assert is_even_or_odd(3) == "odd"
    assert is_even_or_odd(0) == "even"
    assert is_even_or_odd(-2) == "even"
    assert is_even_or_odd(-3) == "odd"
