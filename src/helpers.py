"""
Helper functions for working with ciphers
"""

CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'


def pos(c: str) -> int:
    """
    For a single character, return its position in the alphabet
    This is the index of the character in the CHARACTERS string + 1
    """
    if len(c) != 1:
        raise ValueError("expecting a single character")
    c = c.lower() # make sure it's lowercase
    i = CHARACTERS.find(c)
    if i == -1:
        raise ValueError("not a letter")
    return i + 1


def char_at(pos: int) -> str:
    """
    Return the character at position pos in the alphabet
    pos is computed using mod 26 arithmatic and will be in the range 0..25
    By convention pos 1 is 'a' and pos 26 is 'z', so treat 0 as 26 lookup
    """
    if pos < 0:
        raise ValueError("position out of range")
    ix = pos % 26
    if ix == 0:
        ix = 26
    return CHARACTERS[ix-1]

def strip_text(text: str) -> str:
    """
    Clean an input text for encryption or decryption by
    - converting to lowercase
    - removing all characters that are not a...z
    """
    return ''.join(c for c in text.lower() if c in CHARACTERS)


def format_ciphertext(ciphertext: str) -> str:
    """
    Convert ciphertext to uppercase and format into blocks of 5 characters,
    Format into lines of 10 of such groups.
    """
    # just to make sure that all letters and no spaces
    ciphertext = (''.join(c for c in ciphertext.lower() if c in CHARACTERS)).upper()
    result = []

    # Break into 5-character blocks
    for i in range(0, len(ciphertext), 5):
        block = ciphertext[i:i + 5]
        result.append(block)

    # Group blocks into lines of 10 so each line is 60 chars or less
    formatted_text = []
    for i in range(0, len(result), 10):
        line = ' '.join(result[i:i + 10])
        formatted_text.append(line)

    return '\n'.join(formatted_text)


def format_plaintext(plaintext: str) -> str:
    """
    Display decrypted plaintext as lowercase in lines of 60 characters
    """
    # just to make sure that all letters and no spaces
    plaintext = (''.join(c for c in plaintext.lower() if c in CHARACTERS))
    formatted_text = []
    for i in range(0, len(plaintext), 60):
        formatted_text.append(plaintext[i:i + 60])
    return '\n'.join(formatted_text)
