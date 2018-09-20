
def units(i):
    """
    Return the word in the units position.
    :param i: Integer in the units position
    :return: The word representation
    """
    units = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five', 
        'six',
        'seven',
        'eight',
        'nine'
        ]
    return units[i]


def tens(i):
    """
    Return the word in the tens position.
    :param i: Integer in the tens position
    :return: The word representation
    """
    tens = [
        '',
        'ten',
        'twenty',
        'thirty',
        'forty',
        'fifty', 
        'sixty',
        'seventy',
        'eighty',
        'ninety'
        ]
    return tens[i]


def hundreds(i):
    """
    Return the words in the hundreds position.
    :param i: Integer in the hundreds position
    :return: The word representation
    """
    return units(i) + ' hundred and'


def thousands(x):
    """
    Return the words in the thousands position.
    """
    return hundreds(str(x)[0]) + tens(str(x)[1]) + units(str(x)[2])
