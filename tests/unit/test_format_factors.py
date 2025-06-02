"""
Test format_factors
"""
import pytest
from src.utilities import format_factors


def test_empty_factors():
    with pytest.raises(ValueError):
        _ = format_factors([])

def test_null_factors():
    with pytest.raises(ValueError):
        _ = format_factors(None)

def test_outof_order_factors():
    with pytest.raises(ValueError):
        _ = format_factors([2, 3, 2])

def test_negative_factors():
    with pytest.raises(ValueError):
        _ = format_factors([-2, 3, 3])

def test_factors():
    formatted_str = format_factors([2, 3, 3, 5, 37])
    assert formatted_str == "2 \\cdot 3^2 \\cdot 5 \\cdot 37"
