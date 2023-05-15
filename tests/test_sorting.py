import os
import sys
import pytest
from data_structures.sorting import *

# add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(""))


@pytest.mark.sort
class TestSorting:
    def test_bubble_sort(self):
        sorting = Sorting()
        nums = [4, 2, 6, 5, 1, 3]
        sorting.bubble_sort(nums)
        assert nums == [1, 2, 3, 4, 5, 6]

    def test_selection_sort(self):
        sorting = Sorting()
        nums = [4, 2, 6, 5, 1, 3]
        sorting.selection_sort(nums)
        assert nums == [1, 2, 3, 4, 5, 6]

    def test_insertion_sort(self):
        sorting = Sorting()
        nums = [4, 2, 6, 5, 1, 3]
        sorting.insertion_sort(nums)
        assert nums == [1, 2, 3, 4, 5, 6]
