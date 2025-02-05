from numb3rs import validate

def main():
    # test case for ValueError
    test_format()
    test_range()

def test_format():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False

def test_range():
    assert validate("1.1.1.1") == True
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False






if __name__ == "__main__":
    main()
