class EN(object):

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
        'ninety',
        ]

    hundred = 'hundred'

    powers_of_1000 = [
        None,
        'thousand',
        'million',
        'billion',
        'trillion',
        'quadrillion',
        'quintillion',
        'sextillion',
        'septillion',
        'octillion',
        'decillion',
        'undecillion',
        'duodecillion',
        'tredecillion',
        'quattuordecillion',
        'quindecillion',
    ]

    concatenator = 'and'

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

    modifiers = [
        lambda word: word.rstrip(' zero') if word.endswith('zero') and word!='zero' else word,
        lambda word: word.rsplit(' and')[0] if word.endswith('and') else word 
    ]