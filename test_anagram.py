import unittest
import anagram


class TestAnagram(unittest.TestCase):

    def test_is_anagram(self):
        test_cases = [
            ("pat", "tap", True),
            ("angered", "enraged", True),
            ("evil", "vile", True),
            ("debit card", "bad credit", True),
            ("cat", "dog", False),
            ("Man", "man", False)
        ]
        for a, b, expected in test_cases:
            with self.subTest(f"{a}, {b} -> {expected}"):
                self.assertEqual(expected, anagram.is_anagram(a, b))


if __name__ == '__main__':
    unittest.main()
def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    if  (first_string) == (second_string)[::-1]:
        return True
    else:
        return False# remove pass statement and implement me
