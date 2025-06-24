"""
  Utilities and references for use with cracking polyalphabetic ciphers
"""
from IPython.display import display, Math

# Table 2.1 from section 2.5, used for Letter-Number encryption
TABLE_2_1 = {
    'a': [15, 33, 37, 55, 57, 72, 91, 96],
    'b': [24],
    'c': [3, 39, 67],
    'd': [4, 43, 61, 88],
    'e': [8, 12, 20, 46, 47, 59, 64, 79, 81, 85, 90, 94, 97],
    'f': [40, 48],
    'g': [29, 53],
    'h': [5, 16, 30, 42, 69, 99],
    'i': [14, 45, 50, 60, 73, 82, 93],
    'j': [11],
    'k': [77],
    'l': [1, 26, 71, 98],
    'm': [34, 87],
    'n': [6, 17, 22, 31, 49, 58],
    'o': [2, 10, 41, 51, 66, 75, 83],
    'p': [13, 18],
    'q': [36],
    'r': [21, 25, 65, 68, 92, 95],
    's': [00, 28, 52, 63, 74, 78],
    't': [7, 19, 23, 35, 38, 54, 70, 84, 89],
    'u': [9, 32],
    'v': [44],
    'w': [56, 80],
    'x': [86],
    'y': [62, 76],
    'z': [27],
}

# propability for each letter in the English alphabet
LETTER_PROBABILITIES = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782,
                        'd': 0.04253, 'e': 0.12702, 'f': 0.02228,
                        'g': 0.02015, 'h': 0.06094, 'i': 0.06966,
                        'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
                        'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
                        'p': 0.01929, 'q': 0.00095, 'r': 0.05987,
                        's': 0.06327, 't': 0.09056, 'u': 0.02758,
                        'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
                        'y': 0.01974, 'z': 0.00074}


def display_frequency_tables(frequencies: list[dict[str, int]]):
    """
    Build a display of frequency tables for i-graphs.
    """
    latex_table = _get_frequency_display(frequencies)
    display(Math(latex_table))


_TITLES = [
    "Letter",
    "Digraph",
    "Trigraph",
    "Quadgraph",
    "Pentagraph",
    "Hexagraph",
    "Septagraph"
]


def _get_frequency_display(frequencies: list[dict[str, int]]) -> str:
    """
    Create a LaTeX display of frequency tables for i-graphs, The input is a list of dictionaries,
    the first dictionary is for the letter-number table, the second is for the digraph table, etc.
    There can be up to 7 dictionaries in the list.  Arrays are arranged in a single row.

    Only include the frequency tables for i-graphs with frequency > 1.

    Returns:
        LaTeX formatted string containing the frequency tables
    """
    tables = []
    for i, f in enumerate(frequencies):
        # Create the frequency array
        ngraph_array = "\\begin{array}{c|c}\n"
        ngraph_array += f"\\text{{{_TITLES[i]}}} & \\text{{Frequency}} \\\\\n\\hline\n"
        for inst, count in f.items():
            if count > 1:
                ngraph_array += f"{inst.upper()} & {count} \\\\\n"
        ngraph_array += "\\end{array}"
        tables.append(ngraph_array)

    # Combine the arrays
    fmt = "c" * len(tables)
    answer = f"\\begin{{array}}[t]{{{fmt}}}\n"
    answer += " \\quad \\quad & ".join(tables) + "\n"
    answer += "\\end{array}"
    return answer
