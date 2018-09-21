class Integer(object):
    """
    
    """

    # concatenator = 'and'

    # units = [
    #     'zero',
    #     'one',
    #     'two',
    #     'three',
    #     'four',
    #     'five', 
    #     'six',
    #     'seven',
    #     'eight',
    #     'nine'
    #     ]

    # tens = [
    #     '',
    #     'ten',
    #     'twenty',
    #     'thirty',
    #     'forty',
    #     'fifty', 
    #     'sixty',
    #     'seventy',
    #     'eighty',
    #     'ninety'
    #     ]

    # hundred = 'hundred'

    # powers_of_1000 = [
    #     None,
    #     'thousand',
    #     'million',
    #     'billion',
    #     'trillion',
    #     'quadrillion',
    #     'quintillion',
    #     'sextillion',
    #     'septillion',
    #     'octillion',
    #     'decillion',
    #     'undecillion',
    #     'duodecillion',
    #     'tredecillion',
    #     'quattuordecillion',
    #     'quindecillion',
    # ]

    # replacements = {
    #     'ten zero':  'ten',
    #     'ten one':   'eleven',
    #     'ten two':   'twelve',
    #     'ten three': 'thirteen',
    #     'ten four':  'fourteen',
    #     'ten five':  'fifteen',
    #     'ten six':   'sixteen',
    #     'ten seven': 'seventeen',
    #     'ten eight': 'eighteen',
    #     'ten nine':  'nineteen',
    # }

    # modifiers = [
    #     lambda word: word.rstrip(' zero') if word.endswith('zero') and word!='zero' else word,
    #     lambda word: word.rsplit(' and')[0] if word.endswith('and') else word 
    # ]


    @classmethod
    def _power_of_1000(cls):
        i = 0
        while True:
            yield cls.powers_of_1000[i]
            i += 1


    @classmethod
    def _units(cls, i):
        """
        Return the word in the units position.
        :param i: Integer in the units position
        :return: The word representation
        """
        return cls.units[i]


    @classmethod
    def _tens(cls, i):
        """
        Return the word in the tens position.
        :param i: Integer in the tens position
        :return: The word representation
        """
        return cls.tens[i]


    @classmethod
    def _hundreds(cls, i):
        """
        Return the words in the hundreds position.
        :param i: Integer in the hundreds position
        :return: The word representation
        """
        return cls._units(i) + f' {cls.hundred}'


    @classmethod
    def _position(cls):
        while True:
            yield cls._units
            yield cls._tens
            yield cls._hundreds


    @classmethod
    def _insert_and(cls, words):
        """
        Inserts the 'and' if required after the 'hundred'
        eg. one hundred fifty seven -> one hundred and fifty seven
        :param words: <list> List of three strings, one for each position
        :return:      <list> List of three strings with 'and' added
        """
        if len(words)==3 and (words[1]!='' or words[2]!=''):
            words[0] += f' {cls.concatenator}'
        return words


    @staticmethod
    def _clean_whitespace(word):
        """
        Clean the leading, trailing and double whitespace
        :param word: <str> A wordified number
        :return:     <str> Cleaned string
        """
        return word.lstrip(' ').rstrip(' ').replace('  ', ' ')


    @staticmethod
    def _split_into_triples(x):
        """
        A Triple is three consecutive digits of a number.
        eg. 456   is composed of one triple:   456
            23800 is composed of two triples:  23, 800
        It is a useful primitive as large numbers are just concatenated
        triples with the textual representation of a power-of-1000 
        separating them.
        eg.   123,045,008  ->             123 million  45 thousand and   8
              4,010,200,167  ->   4 billion  10 million 200 thousand     167 
        """
        return [int(i) for i in '{:,}'.format(x).split(',')]


    @classmethod
    def _wordify_triple(cls, x, append=None, and_less=False):
        """
        Turn a three digit integer into its textual representation.
        :param x:                   <int>  The integer to be wordified
        :param to_app
        :param and_less (optional): <bool> Whether to stip all 'and's
        :return:                    <str>  The textual representation of x
        """
        position = cls._position()
        words = [next(position)(int(i)) for i in str(x)[::-1]][::-1]
        
        if not and_less: words = cls._insert_and(words)

        word = ' '.join(words)
        word = cls._clean_whitespace(word)

        for m in cls.modifiers:
            word = m(word)

        for k, v in cls.replacements.items():
            word = word.replace(k, v)

        if append:
            word = f'{word} {append}'

        return word


    @classmethod
    def wordify(cls, x, and_less=False):
        p1000 = cls._power_of_1000()
        triples = cls._split_into_triples(x)
        words = [cls._wordify_triple(triple, next(p1000)) for triple in triples[::-1]][::-1]
        words = [word for word in words if not word.startswith('zero') or len(words)==1]
        
        if len(words) > 1 and cls.concatenator not in words[-1]:
            words[-1] = f'{cls.concatenator} {words[-1]}'

        word = ' '.join(words)
        return word
