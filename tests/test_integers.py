import wordify


def test_units():
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
    assert wordify.integer(21) == 'twenty one'
    assert wordify.integer(32) == 'thirty two'
    assert wordify.integer(49) == 'forty nine'
    assert wordify.integer(57) == 'fifty seven'
    assert wordify.integer(68) == 'sixty eight'
    assert wordify.integer(70) == 'seventy'


def test_hundreds():
    assert wordify.integer(123) == 'one hundred and twenty three'
    assert wordify.integer(280) == 'two hundred and eighty'
    assert wordify.integer(501) == 'five hundred and one'
    assert wordify.integer(300) == 'three hundred'
    assert wordify.integer(200) == 'two hundred'
    assert wordify.integer(715) == 'seven hundred and fifteen'


def test_thousands():
    assert wordify.integer(2054)    == 'two thousand and fifty four'
    assert wordify.integer(1234)    == 'one thousand two hundred and thirty four'
    assert wordify.integer(12000)   == 'twelve thousand'
    assert wordify.integer(100000)  == 'one hundred thousand'


def test_large_power_of_ten():
    assert wordify.integer(1e6)     == 'one million'
    assert wordify.integer(10e6)    == 'ten million'
    assert wordify.integer(100e6)   == 'one hundred million'
    assert wordify.integer(1e9)     == 'one billion'
    assert wordify.integer(10e9)    == 'ten billion'
    assert wordify.integer(100e9)   == 'one hundred billion'
    assert wordify.integer(1e12)    == 'one trillion'
    assert wordify.integer(10e12)   == 'ten trillion'
    assert wordify.integer(100e12)  == 'one hundred trillion'


def test_large_random():
    assert wordify.integer(1e12+13) == 'one trillion and thirteen'
    assert wordify.integer(14e6+12345) == 'fourteen million twelve thousand three hundred and forty five'
    assert wordify.integer(100000000000000003000000004) == 'one hundred septillion three billion and four'