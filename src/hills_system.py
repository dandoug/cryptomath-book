"""
Explore some things related to hill's system
"""
import math
import time
from itertools import product
from sympy import mod_inverse
from heapq import heappush, heappushpop, nlargest
from dataclasses import dataclass
from typing import Any, List
import numpy as np
import numpy.typing as npt

def int_det(a: np.ndarray) -> int:
    """
    Determine the integer determinant of a matrix
    :raise Value Error if the matrix does not have an integer determinant
    """
    det = np.linalg.det(a)
    if abs(det - round(det)) < 1e-8:
        return int(round(det))
    else:
        raise ValueError("Determinant is not close to an integer!")


def _mod_26(i: int) -> int:
    ans = i % 26
    while ans < 0:
        ans += 26
    return ans


def is_invertible_mod_26(a: np.ndarray) -> bool:
    """
    determine if a matrix is invertible mod 26
    """
    # should check that is square and made of integers, but we'll assume
    det = int_det(a)
    return math.gcd(det, 26) == 1


current_count = 0
keys_checked = 0


def count_invertible_keys(n: int) -> int:
    """
    Count the number of invertible nxn matrices mod 26 for Hill's cipher system
    where matrix elements must be a permutation of numbers 0 through 25
    :return: number of invertible matrices
    """
    if n<1 or n>10:
        raise ValueError("n must be between 1 and 10")
    global current_count, keys_checked
    count = 0
    key_elements = n**2
    total_keys = math.pow(26, key_elements)
    last_update_time = time.time()
    update_interval = 4.0  # Update progress every 2 seconds

    for i, key_values in enumerate(product(range(26), repeat=key_elements)):
        array = []
        row = []
        for j in range(len(key_values)):
            if j % n == 0 and j > 0:
                array.append(row)
                row = []
            row.append(key_values[j])
        array.append(row)

        matrix = np.array(array, dtype=int)
        keys_checked += 1
        if is_invertible_mod_26(matrix):
            count += 1
            current_count = count

        # Show progress periodically
        current_time = time.time()
        if current_time - last_update_time > update_interval:
            progress = (i + 1) / total_keys * 100
            print(f"\rProgress: {progress:.1f}% - Checked: {keys_checked:,}" +
                  f" - Found invertible: {count:,}...",
                  end="", flush=True)
            last_update_time = current_time

    return count


def matrix_inverse_mod26(matrix: np.ndarray) -> np.ndarray:
    """
    Compute the inverse of a matrix mod 26.
    :raise ValueError: If the matrix is not invertible mod 26
    """
    # First check if matrix is invertible mod 26
    det = int_det(matrix)
    if math.gcd(det, 26) != 1:
        raise ValueError("Matrix is not invertible mod 26")

    # Calculate the adjugate matrix
    n = matrix.shape[0]
    adj = np.zeros_like(matrix)

    for i in range(n):
        for j in range(n):
            # Calculate cofactor
            minor = np.delete(np.delete(matrix, i, 0), j, 1)
            cofactor = int_det(minor) * (-1) ** (i + j)
            adj[j, i] = cofactor  # Note the transpose: [j,i] instead of [i,j]

    # Calculate the multiplicative inverse of determinant mod 26
    det_inv = mod_inverse(det % 26, 26)

    # Calculate inverse matrix and take modulo 26
    inv = (det_inv * adj) % 26

    return inv.astype(int)


def validate_hills_key(key: npt.NDArray[np.int_]):
    """
    Validate a key for Hill's cipher system (ivertible check done separately)
    """
    if not isinstance(key, np.ndarray):
        raise ValueError("Key must be a numpy array")
    if key.ndim != 2 or key.shape[0] != key.shape[1]:
        raise ValueError("Key must be a 2D square matrix")
    if not np.issubdtype(key.dtype, np.integer):
        raise ValueError("Key must contain only integers")


@dataclass
class Result:
    """
    Represents a result object encapsulating a score, a key, and a plaintext.
    Used in heap to keey only the best results.
    """
    score: float
    key: tuple
    plaintext: str

    def __lt__(self, other):
        # For heap operations, compare by score
        return self.score < other.score


class TopResults:
    def __init__(self, max_size: int = 10):
        self.heap: List[Result] = []
        self.max_size = max_size

    def add(self, score: float, key: tuple, plaintext: str):
        result = Result(score, key, plaintext)
        if len(self.heap) < self.max_size:
            heappush(self.heap, result)
        elif score > self.heap[0].score:  # if better than worst score
            heappushpop(self.heap, result)

    def get_best(self):
        # Returns list sorted by score (highest first)
        return nlargest(len(self.heap), self.heap)
