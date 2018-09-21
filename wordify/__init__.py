from .core.integer import Integer
from .languages import get_language


def integer(x, language='EN'):
    """
    Return the word represetation of the integer x.
    :param x: An integer to be wordified
    :return: The word representation of x
    """
    language_cls = get_language(language)
    Integer_cls  = type('Integer_cls', (language_cls, object), Integer.__dict__.copy())
    return Integer_cls.wordify(int(x))