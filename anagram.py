
"""
Given two strings, this functions determines if they are an anagram of one another.
"""


def is_anagram(first_string: str, second_string: str) -> bool:
    if len(first_string) != len(second_string):
        return False

    list_a = list(first_string)
    list_b = list(second_string)

    for letter in first_string:
        if letter in list_a and letter in list_b:
            list_a.remove(letter)
            list_b.remove(letter)
            return True
        else:
            return False





