import os
import sys

sys.path.insert(0, os.path.abspath(""))

import pytest
from data_structures.doubly_linkedlist import *


@pytest.fixture
def test_dll():
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    return dll


@pytest.mark.dll
class TestDoublyLinkedList:
    def test_constructor(self):
        dll = DoublyLinkedList(1)
        assert dll.head.value == 1
        assert dll.head.prev is None
        assert dll.head.next is None
        assert dll.tail.prev is None
        assert dll.tail.next is None
        assert dll.length == 1

    def test_str(self):
        dll = DoublyLinkedList(1)
        dll.head.next = Node(2)
        assert str(dll) == "1 2"

    def test_clear(self):
        dll = DoublyLinkedList(1)
        dll.clear()
        assert dll.length == 0
        assert dll.head is None
        assert dll.tail is None

    def test_append(self):
        dll = DoublyLinkedList(1)
        dll.append(2)
        assert dll.length == 2
        assert dll.tail.value == 2
        assert dll.head.value == 1
        assert str(dll) == "1 2"

    def test_pop(self):
        dll = DoublyLinkedList(1)
        dll.append(2)
        assert dll.pop().value == 2
        assert dll.length == 1
        assert str(dll) == "1"
        assert dll.pop().value == 1
        assert dll.length == 0
        assert str(dll) == ""
        assert dll.pop() is None

    def test_prepend(self):
        dll = DoublyLinkedList(1)
        dll.prepend(2)
        assert str(dll) == "2 1"
        assert dll.length == 2
        assert dll.head.value == 2
        assert dll.tail.value == 1

        dll1 = DoublyLinkedList(1)
        dll1.clear()
        dll1.prepend(2)
        assert str(dll1) == "2"
        assert dll1.length == 1
        assert dll1.head.value == 2
        assert dll1.tail.value == 2

    def test_pop_first(self):
        dll = DoublyLinkedList(1)
        dll.append(2)
        assert dll.pop_first().value == 1
        assert dll.length == 1
        assert str(dll) == "2"

        assert dll.pop_first().value == 2
        assert dll.length == 0

        assert dll.pop() is None
        assert dll.head is None
        assert dll.tail is None

    def test_get(self, test_dll):
        dll = test_dll
        assert dll.get(-1) is None
        assert dll.get(dll.length) is None

        assert dll.get(0).value == 1
        assert dll.get(1).value == 2
        assert dll.get(2).value == 3
        assert dll.get(3).value == 4
        assert dll.get(4).value == 5
        assert dll.get(5).value == 6

    def test_set_value(self, test_dll):
        dll = test_dll
        assert dll.set_value(-1, 10) == False
        assert dll.set_value(0, 100) == True
        assert dll.get(0).value == 100
        assert dll.set_value(dll.length - 1, 1000) == True
        assert dll.get(dll.length - 1).value == 1000
        assert str(dll) == "100 2 3 4 5 1000"

    def test_insert(self, test_dll):
        dll = test_dll
        assert dll.insert(-1, 100) == False
        assert dll.insert(dll.length + 1, 1000) == False

        assert dll.insert(0, 100) == True
        assert dll.length == 7
        assert str(dll) == "100 1 2 3 4 5 6"

    def test_swap_first_last(self, test_dll):
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Swap the values of the first and last node

        ##### ? CONSTRAINTS ? #####
        The pointers to the nodes themselves are not swapped - only the values are exchanged
        """
        dll = test_dll
        dll.swap_first_last()
        assert dll.head.value == 6
        assert dll.tail.value == 1
        assert str(dll) == "6 2 3 4 5 1"

    def test_reverse(self, test_dll):
        dll = test_dll
        dll.reverse()
        assert str(dll) == "6 5 4 3 2 1"
        assert dll.head.value == 6
        assert dll.tail.value == 1

    def test_check_palindrome(self, test_dll):
        dll0 = DoublyLinkedList(1)
        dll0.clear()
        assert dll0.check_palindrome() == False

        dll1 = DoublyLinkedList(1)
        assert dll1.check_palindrome() == True

        dll2 = test_dll
        assert dll2.check_palindrome() == False

        dll3 = DoublyLinkedList(1)
        dll3.append(2)
        dll3.append(3)
        dll3.append(2)
        dll3.append(1)
        assert dll3.check_palindrome() == True

        dll4 = DoublyLinkedList(1)
        dll4.append(2)
        dll4.append(3)
        assert dll4.check_palindrome() == False

    def test_swap_pairs(self, test_dll):
        dll0 = DoublyLinkedList(1)
        dll0.swap_pairs()
        assert str(dll0) == "1"

        dll0.clear()
        dll0.swap_pairs()
        assert str(dll0) == ""

        dll1 = test_dll
        dll1.swap_pairs()
        assert str(dll1) == "2 1 4 3 6 5"
