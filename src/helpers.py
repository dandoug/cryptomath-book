"""
Helper functions for working with ciphers
"""
from IPython.display import display, Math

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
    By convention pos 1 is 'a' and pos 26 is 'z', so treat 0 as 26
    """
    if pos < 0:
        raise ValueError("position out of range")
    ix = pos % 26
    if ix == 0:
        ix = 26
    return CHARACTERS[ix-1]


def mod_26(a:  int) -> int:
    answer = a % 26
    if answer < 0:
        answer += 26
    return answer


POSSIBLE_KEYS = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
def reverse_mult_key(plain_char: str, cipher_char: str) -> int:
    """
    Given a cipher char and a plain char, return the key used to encrypt it
    assuming that it was done by a simple multiplicative cipher
    Since there are only 12 possible keys, we can brute force the key.
    :raise ValueError if no key is possible
    """
    cipher_pos = pos(cipher_char.lower())
    plain_pos = pos(plain_char.lower())
    for key in POSSIBLE_KEYS:
        if (plain_pos * key) % 26 == cipher_pos:
            return key
    raise ValueError("no multiplicative key found for this pair of characters")


def reverse_add_key(plain_char: str, cipher_char: str) -> int:
    """
    given a cipher char and a plain char, return the key used to encrypt it
    assuming that it was done by a simple additive cipher
    """
    cipher_pos = pos(cipher_char.lower())
    plain_pos = pos(plain_char.lower())
    return mod_26(cipher_pos - plain_pos)

def build_guesses(plaintexts: list[str], ciphertexts:list[str]) -> tuple[tuple[str, str]]:
    """
    Construct guesses from the plaintexts and ciphertexts.  Each element of the lists is a string,
    and all the strings are the same length.  Build character substitution guess tuples by matching
    the combinations of the strings.\
    """
    result = []
    for p in plaintexts:
        for c in ciphertexts:
            guess = []
            for i in range(len(p)):
                guess.append((p[i], c[i].upper()))
            if len(guess) == 1:
                guess = guess[0] # special case for single character substitutions
            result.append(tuple(guess))
    return tuple(result)


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


def display_fequency_tables(letter_counts: dict[str, int],
                           digraph_counts: dict[str, int],
                           trigraph_counts: dict[str, int]):
    latex_table = _get_frequency_display(letter_counts, digraph_counts, trigraph_counts)
    display(Math(latex_table))




def _get_frequency_display(letter_counts: dict[str, int],
                           digraph_counts: dict[str, int],
                           trigraph_counts: dict[str, int]) -> str:
    """
    Create a LaTeX display of frequency tables for letters, digraphs, and trigraphs.
    Arrays are arranged in a single row with letter frequencies on the left,
    digraph frequencies in the middle, and trigraph frequencies on the right.
    All arrays are top-aligned.

    Args:
        letter_counts: Dictionary mapping single letters to their frequencies
        digraph_counts: Dictionary mapping digraphs to their frequencies
        trigraph_counts: Dictionary mapping trigraphs to their frequencies

    Returns:
        LaTeX formatted string containing the frequency tables
    """
    # Create the letter frequency array
    letter_array = "\\begin{array}{c|c}\n"
    letter_array += "\\text{Letter} & \\text{Frequency} \\\\\n\\hline\n"
    for letter, count in letter_counts.items():
        letter_array += f"{letter.upper()} & {count} \\\\\n"
    letter_array += "\\end{array}"

    # Create the digraph frequency array
    digraph_array = "\\begin{array}{c|c}\n"
    digraph_array += "\\text{Digraph} & \\text{Frequency} \\\\\n\\hline\n"
    for digraph, count in digraph_counts.items():
        # only include digraphs with frequency > 1
        if count > 1:
            digraph_array += f"{digraph.upper()} & {count} \\\\\n"
    digraph_array += "\\end{array}"

    # Create the trigraph frequency array
    trigraph_array = "\\begin{array}{c|c}\n"
    trigraph_array += "\\text{Trigraph} & \\text{Frequency} \\\\\n\\hline\n"
    for trigraph, count in trigraph_counts.items():
        # only include trigraphs with frequency > 1
        if count > 1:
            trigraph_array += f"{trigraph.upper()} & {count} \\\\\n"
    trigraph_array += "\\end{array}"

    # Combine the arrays with top alignment using a matrix environment
    return (f"\\begin{{array}}[t]{{ccc}}\n" +
            f"{letter_array} \\quad \\quad & {digraph_array} \\quad \\quad & {trigraph_array}\n" +
            f"\\end{{array}}")
