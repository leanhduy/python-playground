import os
import sys

# os.system("clear") if os.name == "posix" else os.system("cls")
sys.path.insert(0, os.path.abspath(""))

import pytest
from data_structures.queue import *


@pytest.mark.q
class TestQueue:
    def test_constructor(self):
        s = Queue(1)
        assert type(s) is Queue
        assert s.front.value == 1
        assert s.rear.value == 1
        assert s.length == 1

    def test_clear(self):
        pass

    def test_str(self):
        s = Queue(1)
        assert str(s) == "1"
        s.clear()
        assert str(s) == ""

    def test_enqueue(self):
        s = Queue(1)
        s.enqueue(2)
        assert s.length == 2
        assert str(s) == "1 2"

        s = Queue(0)
        s.clear()
        s.enqueue(1)
        assert s.length == 1
        assert str(s) == "1"

    def test_dequeue(self):
        s = Queue(1)
        s.enqueue(2)
        assert s.dequeue().value == 1
        assert s.length == 1
        assert s.dequeue().value == 2
        assert s.length == 0
        assert s.dequeue() is None
