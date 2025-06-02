"""
Test the prime_factors function in 1_2_prime_factors.ipynb
"""
from tests.conftest import crypto_book_testbook


@crypto_book_testbook('1_2_primes_gcd.ipynb')
def test_prime_factors(tb):
    prime_factors = tb.get("prime_factors")
    factors = prime_factors(12)
    _compare_lists(factors, [2, 2, 3])

def _compare_lists(actual: list[int], expected: list[int]):
    if actual is None:
        assert expected is None
    if expected is None:
        assert actual is None
    assert len(actual) == len(expected)
    for a, e in zip(actual, expected):
        assert a == e
