"""
    This file contains all the tests for the Binary Search Tree
"""
import os
import sys

sys.path.insert(0, os.path.abspath(""))

import pytest
from data_structures.bst import *


@pytest.mark.bst
class TestBinarySearchTree:
    def test_constructor(self):
        bst = BST()
        assert bst.root is None

    def test_insert(self):
        bst = BST()
        assert bst.insert(47) == True

    def test_contains(self):
        bst = BST()
        bst.insert(47)
        bst.insert(21)
        bst.insert(76)
        bst.insert(18)
        bst.insert(27)
        bst.insert(52)
        bst.insert(82)

        assert bst.contains(52) == True
        assert bst.contains(10) == False
