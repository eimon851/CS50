from fuel import gauge
from fuel import convert
import pytest


def main():
    test_correct_int()
    test_value_error()
    test_zero_division()


# return correct int
def test_correct_int():
    assert convert("50/100") == 50 and gauge(50) == '50%'
    assert convert("1/100") == 1 and gauge(1) == 'E'
    assert convert("99/100") == 99 and gauge(99) == 'F'

# raises ValueError
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

# raises ZeroDivisionError
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")









if __name__ == "__main__":
    main()
