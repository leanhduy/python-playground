import sys
import os

# ROOT DIRECTORY
BASE_DIR = os.path.abspath("")
# Add the ROOT DIRECTORY into sys.path
sys.path.insert(0, BASE_DIR)

from data_structures.linkedlist import LinkedList, Node

import pytest


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
