"""
Utilities used for the project
"""
from IPython.display import display, Math


def format_factors(factors: list[int]) -> str:
    """
    Formats a list of integer factors into a mathematical expression string. The list
    of factors represents prime factors of a number, and the output builds an expression
    where repeated factors are represented with exponents. For example, a list of factors
    [2, 2, 3] would result in the expression "2^2 * 3".

    :param factors: A sorted list of integers representing the prime factors of a
        number. The list must be in ascending order to correctly interpret repetitions.
    :return: A string representation of the prime factorization in the form
        "factor^exponent * ...", where repeated factors are grouped and represented with exponents.
    """
    if not factors:
        raise ValueError("empty list of factors")

    last_factor = 0
    last_factor_exp = 0
    expression = ""
    for f in factors:
        if f < last_factor:
            raise ValueError("factors must be positive integers and sorted in ascending order")
        if f == last_factor:  # another instance of the same factor?
            last_factor_exp += 1  # keeping track of the exponent
        else:
            # new factor, so add the previous factor to the expression, as long as it wasn't 0
            if last_factor != 0:
                expression = _add_factor_to_rexpression(expression, last_factor, last_factor_exp)
            # remember the new factor so we can add it later
            last_factor = f
            last_factor_exp = 1
    # add the last one we saw
    expression = _add_factor_to_rexpression(expression, last_factor, last_factor_exp)
    return expression


def factors_as_tuples(factors: list[int]) -> list[tuple[int, int]]:
    """
    Converts a given list of integer factors into a list of tuples representing
    the factors and their corresponding exponents. Each factor is expressed as
    a tuple of its numerical value and its exponent. If a factor does not have
    an explicitly mentioned exponent, it is assumed to be 1.

    :param factors: A list of integers representing the factors to be processed.
    :type factors: list[int]
    :return: A list of tuples where each tuple represents a factor and its
        corresponding exponent.
    :rtype: list[tuple[int, int]]
    """
    factor_string = format_factors(factors)
    factor_strings = factor_string.split(" \\cdot ")
    result = []
    for fs in factor_strings:
        if "^" in fs:
            factor, exp = fs.split("^")
            result.append((int(factor), int(exp)))
        else:
            result.append((int(fs), 1))
    return result


def display_prime_factors_table(inputs, outputs):
    """
    Generate the table latex and display it
    """
    latex_table = _get_prime_factors_table(inputs, outputs)
    display(Math(latex_table))


def display_quotient_and_remainders_table(pairs, quotients_and_remainders):
    latex_table = _get_quotient_and_remainders_table(pairs, quotients_and_remainders)
    display(Math(latex_table))

def display_gcd_table(pairs, gcds):
    latex_table = _get_gcd_table(pairs, gcds)
    display(Math(latex_table))

def display_mod_inverse_table(a_and_n, inv_mod_n):
    latex_table = _get_mod_inverse_table(a_and_n, inv_mod_n)
    display(Math(latex_table))

def display_sum_prod_mod_table(a_b_n, sum_prod_mod_n):
    latex_table = _get_sum_prod_mod_table(a_b_n, sum_prod_mod_n)
    display(Math(latex_table))

def display_key_inv_table(keys, inv_keys):
    latex_table = _get_key_inv_table(keys, inv_keys)
    display(Math(latex_table))

def _get_prime_factors_table(inputs, outputs):
    """
    Create LaTeX content for a table displaying prime factorizations
    Returns just the LaTeX content that can be used in a notebook cell
    """
    latex_content = "\\begin{array}{c|l}\n"
    latex_content += "n & \\text{Prime Factorization of } n \\\\\n\\hline\n"

    for n, factors in zip(inputs, outputs):
        latex_content += f"{n} & {factors} \\\\\n"

    latex_content += "\\end{array}"
    return latex_content


def _add_factor_to_rexpression(expression, factor, exp):
    """
    Appends a factor to the given mathematical expression with proper formatting. The
    factor is added using a product separator if it is not the first factor
    in the expression. An exponent is included in the output if specified.
    """
    if len(expression) > 0:  # not the first factor, then add \product separator
        expression += " \\cdot "
    if exp > 1:  # exponent required?
        expression += f"{factor}^{exp}"
    else:
        expression += str(factor)
    return expression

def _get_quotient_and_remainders_table(pairs, quotients_and_remainders):
    latex_content = "\\begin{array}{c|c|c|c}\n"
    latex_content += ("\\text{dividend} & \\text{divisor} & " +
                      "\\text{quotient} & \\text{remainder} \\\\\n\\hline\n")

    for p, qr in zip(pairs, quotients_and_remainders):
        latex_content += f"{p[0]} & {p[1]} & {qr[0]} & {qr[1]} \\\\\n"

    latex_content += "\\end{array}"
    return latex_content

def _get_gcd_table(pairs, gcds):
    latex_content = "\\begin{array}{c|c|c}\n"
    latex_content += ("x & y & " +
                      "\\text{gcd(} x , y \\text{)} \\\\\n\\hline\n")

    for p, gcd in zip(pairs, gcds):
        latex_content += f"{p[0]} & {p[1]} & {gcd} \\\\\n"

    latex_content += "\\end{array}"
    return latex_content

def _get_mod_inverse_table(a_and_n, inv_mod_n):
    latex_content = "\\begin{array}{c|c|c}\n"
    latex_content += ("a & n & " +
                      "\\text{additive inverse of}\\ a \\pmod{n} \\\\\n\\hline\n")

    for p, inv in zip(a_and_n, inv_mod_n):
        latex_content += f"{p[0]} & {p[1]} & {inv} \\\\\n"

    latex_content += "\\end{array}"
    return latex_content


def _get_sum_prod_mod_table(a_b_n, sum_prod_mod_n):
    latex_content = "\\begin{array}{c|c|c|c|c}\n"
    latex_content += ("a & b & n & " +
                      "a +_n b & a \\times_n b \\\\\n\\hline\n")

    for p, ans in zip(a_b_n, sum_prod_mod_n):
        latex_content += f"{p[0]} & {p[1]} & {p[2]} & {ans[0]} & {ans[1]} \\\\\n"

    latex_content += "\\end{array}"
    return latex_content


def _get_key_inv_table(keys, inv_keys):
    latex_content = "\\begin{array}{c|c}\n"
    latex_content += ("k & k^{-1} \pmod{26} \\\\\n\\hline\n")

    for k, i in zip(keys, inv_keys):
        latex_content += f"{k} & {i} \\\\\n"

    latex_content += "\\end{array}"
    return latex_content
