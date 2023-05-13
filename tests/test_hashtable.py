import os
import sys

# os.system("clear") if os.name == "posix" else os.system("cls")
sys.path.insert(0, os.path.abspath(""))

import pytest
from data_structures.hashtable import *


@pytest.fixture
def init_ht():
    ht = HashTable()
    ht.set_item("Argentina", "Messi")
    ht.set_item("Portugal", "Ronaldo")
    ht.set_item("Brazil", "Pele")
    ht.set_item("Italy", "Buffon")
    ht.set_item("Finland", "Hallaand")
    ht.set_item("Sweden", "Ibrahimovic")
    ht.set_item("Norway", "Carrew")
    ht.set_item("Germany", "Muller")
    ht.set_item("Spain", "Casillas")
    return ht


@pytest.mark.ht
class TestHashTable:
    def test_get(self, init_ht):
        ht = init_ht
        key = "Germany"
        assert ht.get_item(key)[1] == "Muller"
        key = "VietNam"
        assert ht.get_item(key) is None

    def test_keys(self, init_ht):
        ht1 = HashTable()
        assert ht1.keys() == []
        ht2 = init_ht
        assert len(ht2.keys()) == 9


@pytest.mark.ht
def test_has_common_item():
    s1 = [1, 3, 5]
    s2 = [2, 4, 5]
    s3 = [0, 4, 6]
    assert has_common_item(s1, s2) == True
    assert has_common_item(s1, s3) == False


@pytest.mark.ht
def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 4, 5]) == []
    assert find_duplicates([1, 1, 2, 2, 3]) == [1, 2]
    assert find_duplicates([1, 1, 1, 1, 1]) == [1]
    assert find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) == [3, 4]
    assert find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) == [1, 2, 3]
    assert find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == [1, 2, 3]
    assert find_duplicates([]) == []


@pytest.mark.ht
def test_first_non_repeating_char():
    assert first_non_repeating_char("leetcode") == "l"
    assert first_non_repeating_char("hello") == "h"
    assert first_non_repeating_char("aabbcc") == None


@pytest.mark.ht
def test_group_anagrams():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
    assert group_anagrams(["abc", "cba", "bac", "foo", "bar"]) == [
        ["abc", "cba", "bac"],
        ["foo"],
        ["bar"],
    ]
    assert group_anagrams(
        ["listen", "silent", "triangle", "integral", "garden", "ranged"]
    ) == [["listen", "silent"], ["triangle", "integral"], ["garden", "ranged"]]


@pytest.mark.ht
def test_two_sum():
    assert two_sum([], 0) == []
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3, 4, 5], 10) == []
    assert two_sum([1, 2, 3, 4, 5], 7) == [2, 3]
    assert two_sum([1, 2, 3, 4, 5], 3) == [0, 1]


@pytest.mark.ht
def test_subarray_sum():
    assert subarray_sum([1, 2, 3, 4, 5], 9) == [1, 3]
    assert subarray_sum([-1, 2, 3, -4, 5], 0) == [0, 3]
    assert subarray_sum([2, 3, 4, 5, 6], 3) == [1, 1]
    assert subarray_sum([], 0) == []


@pytest.mark.ht
def test_count_good_pairs():
    input = [1, 2, 3, 1, 1, 3]
    assert count_good_pairs(input) == 4
    input = [1, 1, 1, 1]
    assert count_good_pairs(input) == 6
    input = [1, 2, 3]
    assert count_good_pairs(input) == 0


@pytest.mark.ht
def test_count_smaller_numbers_than_current():
    input = [8, 1, 2, 2, 3]
    assert count_smaller_numbers_than_current(input) == [4, 0, 1, 1, 3]
