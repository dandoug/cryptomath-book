import signal
import time
from src.hills_system import count_invertible_keys, current_count, keys_checked


class _TimeoutException(Exception):
    pass


def _timeout_handler(_signum, _frame):
    raise _TimeoutException(
        f"\nComputation timed out.\n"
        f"Keys checked: {keys_checked:,}\n"
        f"Invertible keys found: {current_count:,}"
    )

def test_hills_system():
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(300)  # 5 minutes = 300 seconds

    start_time = time.time()
    try:
        result = count_invertible_keys(2)
        end_time = time.time()
        print(f"\nCompleted!")
        print(f"Found invertible keys: {result:,}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
    except _TimeoutException as e:
        end_time = time.time()
        print(e)
        print(f"Partial execution time: {end_time - start_time:.2f} seconds")
    finally:
        signal.alarm(0)
