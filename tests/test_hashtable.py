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
