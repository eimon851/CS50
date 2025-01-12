from bank import value

def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()


def test_return_zero():
    assert value("Hello") == 0
    assert value("hello, z") == 0
    assert value("HeLlo") == 0

def test_return_twenty():
    assert value("H") == 20
    assert value("hector") == 20
    assert value("hi,james") == 20

def test_return_hundred():
    assert value("yo") == 100
    assert value("1") == 100


