"""
Test gcd function
"""
from math import gcd as math_gcd

from tests.conftest import crypto_book_testbook

TEST_INPUT = [
    (6394, 9828),
    (2862, 6851),
    (4368, 7290),
    (8275, 4788),
    (9961, 3765),
    (8994, 5819),
    (4094, 4518),
    (9495, 4249),
    (2304, 1239),
    (8845, 2703),
    (2366, 3693),
    (7151, 5309),
    (6663, 4370),
    (4080, 5807),
    (3350, 2837),
    (9825, 5594),
    (2127, 9791),
    (5668, 4558),
    (4582, 6991),
    (4752, 9831),
]


@crypto_book_testbook('1_2_primes_gcd.ipynb')
def test_gdc(tb):
    # Compare our gcd program to the math gcd
    gcd = tb.get("gcd")

    for x, y in TEST_INPUT:
        assert gcd(x, y) == math_gcd(x, y)
