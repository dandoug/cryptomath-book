"""
Explore some things related to hill's system
"""
import math
import signal
import time
from itertools import product
import numpy as np
from sympy import mod_inverse


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
    while i < 0:
        i += 26
    return i % 26


def is_invertible_mod_26(a: np.ndarray) -> bool:
    """
    determine if a matrix is invertible mod 26
    """
    # should check that is square and made of integers, but we'll assume
    det = int_det(a)
    return math.gcd(det, 26) == 1


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


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    global current_count, keys_checked
    raise TimeoutException(
        f"\nComputation timed out.\n"
        f"Keys checked: {keys_checked:,}\n"
        f"Invertible keys found: {current_count:,}"
    )


if __name__ == "__main__":
    current_count = 0
    keys_checked = 0
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(300)  # 5 minutes = 300 seconds

    start_time = time.time()
    try:
        result = count_invertible_keys(2)
        end_time = time.time()
        print(f"\nCompleted!")
        print(f"Total keys checked: {keys_checked:,}")
        print(f"Found invertible keys: {result:,}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
    except TimeoutException as e:
        end_time = time.time()
        print(e)
        print(f"Partial execution time: {end_time - start_time:.2f} seconds")
    finally:
        signal.alarm(0)

