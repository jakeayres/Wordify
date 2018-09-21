


def make_replacements(word):
    """ 
    Applies the lists substring replacements
    :param word:  The starting word
    :return word: The word with replacements made
    """
    for r in _replacements:
        word = r(word)

    return word


def _teens(word):
    """
    The string replacements required to correct the naming
    of teens.
    :param word:  The starting word
    :return word: The word with replacements made
    """
    replacements = {
        'ten zero':  'ten',
        'ten one':   'eleven',
        'ten two':   'twelve',
        'ten three': 'thirteen',
        'ten four':  'fourteen',
        'ten five':  'fifteen',
        'ten six':   'sixteen',
        'ten seven': 'seventeen',
        'ten eight': 'eighteen',
        'ten nine':  'nineteen',
    }

    for k, v in replacements.items():
        word = word.replace(k, v)

    return word


_replacements = [_teens]