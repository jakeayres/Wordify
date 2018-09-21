from wordify.primitives import Integer


def test_clean_whitespace():
    assert Integer._clean_whitespace('  hello  world  ') == 'hello world'


def test_insert_and():
    assert Integer._insert_and(['a', '', ''])   == ['a', '', '']
    assert Integer._insert_and(['a', 'b', ''])  == ['a and', 'b', '']
    assert Integer._insert_and(['a', '', 'c'])  == ['a and', '', 'c']
    assert Integer._insert_and(['a', 'b', 'c']) == ['a and', 'b', 'c']
    assert Integer._insert_and(['b', 'c'])      == ['b', 'c']


def test_split_into_triples():
    assert Integer._split_into_triples(123456)   == [123, 456]
    assert Integer._split_into_triples(12345678) == [12, 345, 678]
    assert Integer._split_into_triples(12345)    == [12, 345]


def test_wordify_triple():
    assert Integer._wordify_triple(0)   == 'zero'
    assert Integer._wordify_triple(4)   == 'four'
    assert Integer._wordify_triple(10)  == 'ten'
    assert Integer._wordify_triple(12)  == 'twelve'
    assert Integer._wordify_triple(321) == 'three hundred and twenty one'
    assert Integer._wordify_triple(100) == 'one hundred'
    assert Integer._wordify_triple(118) == 'one hundred and eighteen'
    assert Integer._wordify_triple(201) == 'two hundred and one'
    assert Integer._wordify_triple(123) == 'one hundred and twenty three'
    assert Integer._wordify_triple(850) == 'eight hundred and fifty'
    assert Integer._wordify_triple(23)  == 'twenty three'


def test_wordify():
    assert Integer.wordify(0)           == 'zero'
    assert Integer.wordify(4)           == 'four'
    assert Integer.wordify(10)          == 'ten'
    assert Integer.wordify(321)         == 'three hundred and twenty one'
    assert Integer.wordify(123000645)   == 'one hundred and twenty three million six hundred and forty five'
    assert Integer.wordify(1234)        == 'one thousand two hundred and thirty four'
    assert Integer.wordify(1001)        == 'one thousand and one'