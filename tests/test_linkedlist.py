import sys
import os

# ROOT DIRECTORY
BASE_DIR = os.path.abspath("")
# Add the ROOT DIRECTORY into sys.path
sys.path.insert(0, BASE_DIR)

from data_structures.linkedlist import LinkedList, Node

import pytest


@pytest.fixture
def sample_ll():
    ll = LinkedList()
    ll.append(10)
    ll.append(2)
    ll.append(4)
    ll.append(7)
    ll.append(1)
    ll.append(0)
    ll.append(5)
    return ll


@pytest.mark.ll
class TestLinkedList:
    def test_constructor(self):
        ll = LinkedList()
        assert type(ll) is LinkedList

    def test_find_middle_node(self):
        ll0 = LinkedList()
        assert ll0.find_middle_node() is None

        ll1 = LinkedList()
        ll1.append(1)
        ll1.append(2)
        ll1.append(3)
        ll1.append(4)
        ll1.append(5)
        assert ll1.find_middle_node().value == 3

        ll2 = LinkedList()
        ll2.append(1)
        ll2.append(2)
        ll2.append(3)
        ll2.append(4)
        assert ll2.find_middle_node().value == 3

    def test_has_loop(self):
        ll0 = LinkedList()
        assert ll0.has_loop() == False

        ll1 = LinkedList()
        ll1.append(1)
        ll1.append(2)
        ll1.append(3)
        assert ll1.has_loop() == False

        ll2 = LinkedList()
        ll2.append(1)
        ll2.append(2)
        ll2.append(3)
        ll2.tail.next = ll2.head
        assert ll2.has_loop() == True

    def test_find_kth_from_end(self):
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)

        k = 2
        result = my_linked_list.find_kth_from_end(k)

        assert result.value == 4

    def test_reverse_between(self):
        ll0 = LinkedList()
        ll0.append(1)
        ll0.append(2)
        ll0.append(3)
        ll0.append(4)
        ll0.append(5)

        # Reverse a sublist within the linked list
        ll0.reverse_between(2, 4)
        assert str(ll0) == "1-2-5-4-3"

        ll1 = LinkedList()
        ll1.append(1)
        ll1.append(2)
        ll1.append(3)
        ll1.append(4)
        ll1.append(5)
        ll1.reverse_between(0, 3) == "4-3-2-1-5"

    def test_partition_list(self, sample_ll):
        ll0 = sample_ll
        ll0.partition_list(5)
        assert str(ll0) == "2-4-1-0-10-7-5"

    def test_remove_duplicates_with_set(self):
        ll0 = LinkedList()
        ll0.append(1)
        ll0.append(2)
        ll0.append(3)
        ll0.append(1)
        ll0.append(4)
        ll0.append(2)
        ll0.append(5)
        ll0.remove_duplicates()
        assert str(ll0) == "1-2-3-4-5"

    def test_remove_duplicates_with_set(self):
        ll0 = LinkedList()
        ll0.append(1)
        ll0.append(2)
        ll0.append(3)
        ll0.append(1)
        ll0.append(4)
        ll0.append(2)
        ll0.append(5)
        ll0.remove_duplicates_with_set()
        assert str(ll0) == "1-2-3-4-5"

    def test_remove_duplicates_without_set(self):
        ll0 = LinkedList()
        ll0.append(1)
        ll0.append(2)
        ll0.append(3)
        ll0.append(1)
        ll0.append(4)
        ll0.append(2)
        ll0.append(5)
        ll0.remove_duplicates_without_set()
        assert str(ll0) == "1-2-3-4-5"
