def reverse_string(text):
    """Return the reversed version of text."""
    return text[::-1]


def count_words(text):
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards."""
    return text == text[::-1]
