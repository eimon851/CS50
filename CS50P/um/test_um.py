from um import count

def main():
    test_catching_um()
    test_catching_case_insensitive()
    test_words_with_um()


def test_catching_um():
    assert count("um") == 1
    assert count("um?") == 1

def test_catching_case_insensitive():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

def test_words_with_um():
    assert count("Drum") == 0
    assert count("yummy") == 0


if "__name__" == "__main__":
    main()
