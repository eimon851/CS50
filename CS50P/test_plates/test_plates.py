from plates import is_valid

def main():
    test_first_two_letter()
    test_min_and_max()
    test_punctuation()
    test_zero_placement()

def test_first_two_letter():
    assert is_valid("A22222") == False
    assert is_valid("AA2222") == True

def test_min_and_max():
    assert is_valid("Ab123456") == False
    assert is_valid("A") == False
    assert is_valid("AAAA") == True

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PY3!14") == False
    assert is_valid("PI 14") == False

def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_number_middle():
    assert is_valid("AA22") == True
    assert is_valid("AA22AA") == False

