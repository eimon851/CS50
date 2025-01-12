import pytest
from seasons import duration_in_words

def main():
    test_correct_phrase()
    test_exit()

def test_correct_phrase():
    assert duration_in_words("2022-12-19") == "Five hundred twenty-five thousand, six hundred minutes"

def test_exit():
     with pytest.raises(SystemExit):
        duration_in_words("cat")






