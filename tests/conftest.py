import sys
from pathlib import Path
from functools import wraps
from testbook import testbook

PROJECT_ROOT = Path(__file__).parent.parent
NOTEBOOKS_PATH = PROJECT_ROOT / 'notebooks'

sys.path.insert(0, f"{str(PROJECT_ROOT)}")


def crypto_book_testbook(notebook_name, execute=True):
    """Custom decorator that wraps testbook and simplifies path management."""
    notebook_path = NOTEBOOKS_PATH / notebook_name

    def decorator(func):
        @testbook(str(notebook_path), execute=execute)
        @wraps(func)
        def wrapper(tb):
            return func(tb)
        return wrapper
    return decorator
