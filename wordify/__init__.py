from .primitives import Integer


def integer(x):
    """
    Return the word represetation of the integer x.
    :param x: An integer to be wordified
    :return: The word representation of x
    """
    return Integer.wordify(int(x))