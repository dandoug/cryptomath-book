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


def display_prime_factors_table(inputs, outputs):
    """
    Generate the table latex and display it
    """
    latex_table = _get_prime_factors_table(inputs, outputs)
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
