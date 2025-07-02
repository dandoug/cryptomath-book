"""
Polygraphic ciphers utilities
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path().absolute().parent))

from src.helpers import CHARACTERS


def validate_playfair_key(key: list[list[str]],
                          omitted_letter: str,
                          padding_letter: str,
                          double_letter_replacement: str):
    """
    Validates a key for the Playfair cipher.
    :raises ValueError: if the key is invalid in some way.
    """
    if len(key) != 5:
        raise ValueError("key must be a 5x5 matrix")
    for row in key:
        if len(row) != 5:
            raise ValueError("key must be a 5x5 matrix")
    set_of_letters = set()
    uppers = CHARACTERS.upper()
    for row in key:
        for char in row:
            if char not in uppers:
                raise ValueError(f"key must contain only letters, found {char}")
            if char in set_of_letters:
                raise ValueError(f"key must not contain duplicate letters, but found: {char}")
            if char == omitted_letter:
                raise ValueError(f"key must not contain the omitted letter: {omitted_letter}")
            set_of_letters.add(char)
    if len(set_of_letters) != 25:
        raise ValueError("key must contain 25 unique letters")
    if padding_letter not in set_of_letters:
        raise ValueError(f"padding letter must be in key, but did not find {padding_letter}")
    if double_letter_replacement not in set_of_letters:
        raise ValueError("double letter replacement must be in key, " +
                         f"but did not find {double_letter_replacement}")


def format_digraph_plaintext(plaintext: str) -> str:
    """
    Display decrypted plaintext as lowercase in lines of 20 digraph pairs
    """
    # just to make sure that all letters and no spaces
    plaintext = (''.join(c for c in plaintext.lower() if c in CHARACTERS))
    formatted_text = []
    for i in range(0, len(plaintext), 40):  # each line has 40 chars (20 digraphs)
        line = []
        for j in range(i, min(i+40, len(plaintext)), 2):
            line.append(plaintext[j] + plaintext[j+1])
        formatted_text.append(' '.join(line))
    return '\n'.join(formatted_text)
