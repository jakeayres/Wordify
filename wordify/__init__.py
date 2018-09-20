from .primitives import units, tens, hundreds, powers
from .replacements import make_replacements


def _power():
    while True:
        yield units
        yield tens
        yield hundreds


def _clean_whitespace(word):
    """
    Clean any trailing, leading and double whitespace
    :param word: The word to be cleaned
    :return: The cleaned word
    """
    word = word.lstrip(' ').rstrip(' ')
    word = word.replace('  ', ' ')
    return word


def _clean_trailing_zero(word):
    """
    Clean up trailing 'zero'. eg. twenty zero -> twenty
    :param word: The word to be cleaned
    :return: The cleaned word
    """
    if word == 'zero':
        return word
    else:
        return word[:-5] if word[-4:] == 'zero' else word


def _clean_trailing_and(word):
    """ 
    Clean trailing 'and' eg. twenty and -> twenty
    :param word: The word to be cleaned
    :return: The cleaned word
    """
    print('@'+word[-5:]+'@')
    return word[:-4] if word[-3:] == 'and' else word


def _clean(word):
    """
    Perform cleaning functions on word
    :param word: The word to be cleaned
    :return: The cleaned word
    """
    word = _clean_whitespace(word)
    word = _clean_trailing_zero(word)
    word = _clean_trailing_and(word)
    return word


def integer(x):
    """
    Return the word represetation of the integer x.
    :param x: An integer to be wordified
    :return: The word representation of x
    """
    word = ''
    power = _power()

    for i in str(x)[::-1]:
        p = next(power)
        word = p(int(i)) + ' ' + word

    word = make_replacements(word)

    return _clean(word)