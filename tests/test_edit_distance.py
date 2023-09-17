import sys
import os

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root directory to the Python path
sys.path.insert(0, project_root)

import unittest
from spellcheck import edit_distance

class TestEditDistance(unittest.TestCase):
    def test_equal_strings(self):
        # Test when both strings are equal
        self.assertEqual(edit_distance("abc", "abc"), 0)

    def test_one_empty_string(self):
        # Test when one string is empty
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("abc", ""), 3)

    def test_insertion(self):
        # Test insertion of a character
        self.assertEqual(edit_distance("abc", "abdc"), 1)

    def test_deletion(self):
        # Test deletion of a character
        self.assertEqual(edit_distance("abcdef", "abdef"), 1)

    def test_substitution(self):
        # Test substitution of a character
        self.assertEqual(edit_distance("kitten", "sitting"), 3)

if __name__ == "__main__":
    unittest.main()
