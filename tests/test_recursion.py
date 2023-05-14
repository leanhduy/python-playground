import os
import sys
import pytest
from data_structures.recursion import *

sys.path.insert(0, os.path.abspath(""))


@pytest.mark.recur
class TestRecursion:
    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
