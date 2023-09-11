import re


def vowel_int_palindrome(data: list):
    VOWELS = {'a', 'e', 'i', 'y', 'o', 'u', 'A', 'E', 'I', 'Y', 'O', 'U'}

    palindrome = list(filter(lambda x: x == x[::-1], data))
    any_int = list(filter(lambda x: re.sub("\D", "", x) != '', data))
    any_vowel = list(filter(lambda x: any(i in VOWELS for i in x), data))

    return any_vowel, any_int, palindrome


assert vowel_int_palindrome(['123321', 'asdaxc1zxc', 'zxczxc', 'aaaaa']) == (
    ['asdaxc1zxc', 'aaaaa'], ['123321', 'asdaxc1zxc'], ['123321', 'aaaaa'])
