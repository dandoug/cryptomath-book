"""
Test divide function
"""
from testbook.exceptions import TestbookRuntimeError

from tests.conftest import crypto_book_testbook

@crypto_book_testbook('1_2_primes_gcd.ipynb')
def test_bad_operands(tb):
    divide = tb.get("divide")
    try:
        _ = divide(None, 1)
    except TestbookRuntimeError as e:
        assert e.eclass is ValueError
    try:
        _ = divide(1, None)
    except TestbookRuntimeError as e:
        assert e.eclass is ValueError
    try:
        _ = divide(-1, None)
    except TestbookRuntimeError as e:
        assert e.eclass is ValueError
    try:
        _ = divide(42, 0)
    except TestbookRuntimeError as e:
        assert e.eclass is ValueError

@crypto_book_testbook('1_2_primes_gcd.ipynb')
def test_good_operands(tb):
    divide = tb.get("divide")

    q, r = divide(25, 5)
    assert q == 5
    assert r == 0

    q, r = divide(5, 25)
    assert q == 0
    assert r == 5

    q, r = divide(42, 17)
    assert q == 2
    assert r == 8
