


def test_units():
    import wordify

    assert wordify.integer(0) == 'zero'
    assert wordify.integer(1) == 'one'
    assert wordify.integer(2) == 'two'
    assert wordify.integer(3) == 'three'
    assert wordify.integer(4) == 'four'
    assert wordify.integer(5) == 'five'
    assert wordify.integer(6) == 'six'
    assert wordify.integer(7) == 'seven'
    assert wordify.integer(8) == 'eight'
    assert wordify.integer(9) == 'nine'


def test_teens():
    import wordify

    assert wordify.integer(10) == 'ten'
    assert wordify.integer(11) == 'eleven'
    assert wordify.integer(12) == 'twelve'
    assert wordify.integer(13) == 'thirteen'
    assert wordify.integer(14) == 'fourteen'
    assert wordify.integer(15) == 'fifteen'
    assert wordify.integer(16) == 'sixteen'
    assert wordify.integer(17) == 'seventeen'
    assert wordify.integer(18) == 'eighteen'
    assert wordify.integer(19) == 'nineteen'


def test_tens():
    import wordify

    assert wordify.integer(21) == 'twenty one'
    assert wordify.integer(32) == 'thirty two'
    assert wordify.integer(49) == 'forty nine'
    assert wordify.integer(57) == 'fifty seven'
    assert wordify.integer(68) == 'sixty eight'
    assert wordify.integer(70) == 'seventy'


def test_hundreds():
    import wordify

    assert wordify.integer(123) == 'one hundred and twenty three'
    assert wordify.integer(280) == 'two hundred and eighty'
    assert wordify.integer(501) == 'five hundred and one'
    assert wordify.integer(300) == 'three hundred'
    assert wordify.integer(200) == 'two hundred'
    assert wordify.integer(715) == 'seven hundred and fifteen'