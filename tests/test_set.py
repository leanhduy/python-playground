import sys
import os
import pytest
from data_structures.set import *

sys.path.insert(0, os.path.abspath(""))


@pytest.mark.set
class TestSet:
    def test_remove_duplicates_with_set(self):
        assert remove_duplicates_with_set(
            [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
        ) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_has_unique_chars(self):
        assert has_unique_chars("abcdefg") == True  # should return True
        assert has_unique_chars("hello") == False  # should return False
        assert has_unique_chars("") == True  # should return True
        assert has_unique_chars("0123456789") == True  # should return True
        assert has_unique_chars("abacadaeaf") == False  # should return False

        # Test cases for unique characters in a string

        # Empty string
        test_string = ""
        assert has_unique_chars(test_string) == True

        # String with one character
        test_string = "a"
        assert has_unique_chars(test_string) == True

        # String with two unique characters
        test_string = "ab"
        assert has_unique_chars(test_string) == True

        # String with two repeated characters
        test_string = "aa"
        assert has_unique_chars(test_string) == False

        # String with all unique characters
        test_string = "abcdefghijklmnopqrstuvwxyz"
        assert has_unique_chars(test_string) == True

        # String with all repeated characters
        test_string = "aaaaaaaaaa"
        assert has_unique_chars(test_string) == False

        # String with a mix of unique and repeated characters
        test_string = "abcabcabc"
        assert has_unique_chars(test_string) == False

    def test_find_pairs(self):
        # Test cases for finding pairs of numbers that add up to a target

        # Empty lists
        arr1 = []
        arr2 = []
        target = 10
        assert find_pairs(arr1, arr2, target) == []

        # List with one element
        arr1 = [1]
        arr2 = []
        target = 10
        assert find_pairs(arr1, arr2, target) == []

        # List with two elements
        arr1 = [1, 2]
        arr2 = []
        target = 3
        assert find_pairs(arr1, arr2, target) == []

        # List with two elements, one of which is the target
        arr1 = [1, 2]
        arr2 = [3]
        target = 3
        assert find_pairs(arr1, arr2, target) == []

        # List with two elements, neither of which is the target
        arr1 = [1, 2]
        arr2 = [4]
        target = 3
        assert find_pairs(arr1, arr2, target) == []

        # List with three elements
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        target = 7
        assert find_pairs(arr1, arr2, target) == [(3, 4), (2, 5), (1, 6)]

        # List with three elements, one of which is the target
        arr1 = [1, 2, 3]
        arr2 = [3, 4, 5]
        target = 3
        assert find_pairs(arr1, arr2, target) == []

        # List with three elements, none of which is the target
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        target = 10
        assert find_pairs(arr1, arr2, target) == []

        arr1 = [1, 2, 3, 4, 5]
        arr2 = [2, 4, 6, 8, 10]
        target = 7
        assert find_pairs(arr1, arr2, target) == [(5, 2), (3, 4), (1, 6)]

    def test_longest_consecutive_sequence(self):
        assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4