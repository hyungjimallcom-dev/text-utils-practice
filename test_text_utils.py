from text_utils import reverse_string, count_words, is_palindrome


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_count_words():
    assert count_words("the quick brown fox") == 4


def test_is_palindrome_true():
    assert is_palindrome("level") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False
