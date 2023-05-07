import os
import sys

os.system("cls")
sys.path.insert(0, os.path.abspath(""))

import pytest
from data_structures.stack import *


@pytest.mark.s
class TestStack:
    def test_constructor(self):
        s = Stack(1)
        assert type(s) is Stack
        assert s.top.value == 1
        assert s.length == 1

    def test_clear(self):
        s = Stack(1)
        s.clear()
        assert s.length == 0
        assert s.top is None

    def test_str(self):
        s = Stack(1)
        assert str(s) == "1"
        s.clear()
        assert str(s) == ""

    def test_push(self):
        s = Stack(1)
        s.push(2)
        assert s.length == 2
        assert str(s) == "2 1"

        s = Stack(0)
        s.clear()
        s.push(1)
        assert s.length == 1
        assert str(s) == "1"

    def test_pop(self):
        s = Stack(1)
        s.push(2)
        assert s.pop().value == 2
        assert s.length == 1
        assert s.pop().value == 1
        assert s.length == 0
        assert s.pop() is None


@pytest.mark.s_others
class TestStackList:
    def test_constructor(self):
        s = StackList()
        assert type(s.stack_list) is list
        assert len(s.stack_list) == 0

    def test_push(self):
        s = StackList()
        s.push(1)
        s.push(2)
        assert len(s.stack_list) == 2

    def test_pop(self):
        s = StackList()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1
        assert s.pop() is None


@pytest.mark.s_others
def test_is_balanced_parentheses():
    balanced_parentheses = "((()))"
    unbalanced_parentheses = "((())))"
    assert is_balanced_parentheses(balanced_parentheses) == True
    assert is_balanced_parentheses(unbalanced_parentheses) == False
