from .primitives import units, tens, hundreds, thousands
from .replacements import make_replacements


def _power():
    while True:
        yield units
        yield tens
        yield hundreds


def _power_of_1000():
    while True:
        yield ''
        yield ' thousand'
        yield ' million'
        yield ' billion'
        yield ' trillion'
        yield ' quadrillion'
        yield ' quintillion'
        yield ' sextillion'
        yield ' septillion'
        yield ' octillion'
        yield ' decillion'
        yield ' undecillion'
        yield ' duodecillion'
        yield ' tredecillion'
        yield ' quattuordecillion'
        yield ' quindecillion'
        

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
    return word[:-4] if word[-4:] == ' and' else word


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


def _triple(x):
    """
    Returns the word representation of the number x<1000.
    :param x: integer x<1000
    :return:  Word representation of x
    """
    word = ''
    power_of_ten = _power()

    for i in str(x)[::-1]:
        p10   = next(power_of_ten)
        word = p10(int(i)) + ' ' + word

    word = make_replacements(word)
    word = _clean(word)

    return word


def integer(x):
    """
    Return the word represetation of the integer x.
    :param x: An integer to be wordified
    :return: The word representation of x
    """
    x = int(x)
    words = []
    power_of_1000 = _power_of_1000()

    # x=12,345,678 -> triples=[12, 345, 678]
    triples = [int(str(x)[::-1][i:i+3][::-1]) for i in range(0, len(str(x)), 3)]

    for triple in triples:
        word = _triple(triple)
        words.append(_triple(triple))

    words = [word+next(power_of_1000) for word in words]

    if len(words)>1 and 'and' not in words[0] and not words[0].endswith('hundred'):
        words[0] = 'and ' + words[0]

    if len(words)>1:
        words = [word for word in words if 'zero' not in word]

    word = ' '.join(words[::-1])

    word = _clean(word)
    word = make_replacements(word)

    return word