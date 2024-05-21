import pytest
from rc import reverse

def test_empty_string():
   assert reverse('') == ''

def test_single_character_string():
   assert reverse('a') == 'a'

def test_palindrome_string():
   assert reverse('level') == 'level'

def test_non_palindrome_string():
   assert reverse('hello') == 'olleh'

def test_non_string_input():
   with pytest.raises(TypeError):
       reverse(123)

def test_iterable_non_string_input():
   with pytest.raises(TypeError):
       reverse([1, 2, 3])