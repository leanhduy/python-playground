import os
import sys
import pytest
from data_structures.graph import *

# add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(""))


@pytest.fixture
def setup_graph():
    graph = Graph()
    v1 = "A"
    v2 = "B"
    v3 = "C"
    v4 = "D"
    graph.add_vertex(v1)
    graph.add_vertex(v2)
    graph.add_vertex(v3)
    graph.add_edge(v1, v2)
    graph.add_edge(v1, v3)
    return graph


# Test Class
@pytest.mark.graph
class TestGraph:
    def test_constructor(self):
        graph = Graph()
        assert type(graph) is Graph
        assert type(graph.E) is dict

    def test_add_vertex(self):
        v = "A"
        graph = Graph()
        assert graph.add_vertex(v) == True
        assert len(graph.E) == 1
        assert len(graph.E[v]) == 0
        assert graph.add_vertex(v) == False

    def test_add_edge(self):
        graph = Graph()
        v1 = "A"
        v2 = "B"
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_edge(v1, v2)
        assert graph.E[v1] == ["B"]
        assert graph.E[v2] == ["A"]

        v3 = "C"
        assert graph.add_edge(v1, v3) == False
        assert graph.add_edge(v1, v2) == False

    def test_remove_edge(self, setup_graph):
        graph = setup_graph
        v1 = "A"
        v2 = "B"
        v3 = "C"
        graph.remove_edge(v1, v2) == True
        assert graph.E[v1] == [v3]
        assert graph.E[v2] == []
        graph.remove_edge(v2, v3) == False

    def test_remove_vertext(self, setup_graph):
        graph = setup_graph
        v1 = "A"
        v2 = "B"
        v3 = "C"
        graph.remove_vertex(v1)
        assert v1 not in graph.E
        assert graph.E[v2] == []
        assert graph.E[v3] == []
