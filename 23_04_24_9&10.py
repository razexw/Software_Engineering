import pytest

def count_chars(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def test_count_chars_valid_input():
    assert count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_chars("world") == {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}
    assert count_chars("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}

def test_count_chars_invalid_input():
    with pytest.raises(TypeError):
        count_chars(123)

def test_count_chars_special_cases():
    assert count_chars("") == {}
    assert count_chars("aaaaaaaaa") == {'a': 9}