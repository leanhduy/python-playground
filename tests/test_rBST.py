import os
import sys
import pytest
from data_structures.rBST import *

# add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(""))


@pytest.fixture
def init_rbst():
    rbst = RBST()
    rbst.insert(21)
    rbst.insert(10)
    rbst.insert(47)
    rbst.insert(1)
    rbst.insert(16)
    rbst.insert(25)
    rbst.insert(50)

    return rbst


@pytest.mark.rbst
class TestRBST:
    def test_r_contains(self, init_rbst):
        tree = init_rbst
        assert tree.r_contains(25) == True
        assert tree.r_contains(100) == False
        assert tree.r_contains(21) == True
        assert tree.r_contains(47) == True
        assert tree.r_contains(50) == True

    def test_r_insert(self):
        tree = RBST()
        tree.r_insert(21)
        tree.r_insert(10)
        tree.r_insert(47)
        tree.r_insert(1)
        tree.r_insert(16)
        tree.r_insert(25)
        tree.r_insert(50)
        assert tree.r_contains(25) == True
        assert tree.r_contains(100) == False
        assert tree.r_contains(21) == True
        assert tree.r_contains(47) == True
        assert tree.r_contains(50) == True

    def test_r_delete(self, init_rbst):
        # Case 1: Delete Leaft Node
        t1 = RBST()
        t1.r_insert(21)
        t1.r_insert(10)
        t1.r_insert(47)
        t1.r_delete(100)
        assert t1.root.value == 21
        assert t1.root.left.value == 10
        assert t1.root.right.value == 47
        t1.r_delete(10)
        assert t1.root.value == 21
        assert t1.root.left is None
        assert t1.root.right.value == 47
        t1.r_delete(47)
        assert t1.root.value == 21
        assert t1.root.left is None
        assert t1.root.right is None
        t1.r_delete(21)
        assert t1.root is None
