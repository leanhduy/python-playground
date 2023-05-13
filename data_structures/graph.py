"""
This file implements the Graph data structure
The graph class will be implemented using Adjacency List
"""


class Graph:
    def __init__(self):
        """E stands for Edges"""
        self.E = {}

    def add_vertex(self, v_label) -> bool:
        if v_label not in self.E:
            self.E[v_label] = []
            return True
        return False

    def add_edge(self, v1, v2) -> bool:
        # v1 or v2 is not in the list of vertices or Edge between v1 and v2 already exists
        if v1 not in self.E or v2 not in self.E or v1 in self.E[v2] or v2 in self.E[v1]:
            return False
        self.E[v1].append(v2)
        self.E[v2].append(v1)
        return True

    def remove_edge(self, v1, v2) -> bool:
        if v1 in self.E and v2 in self.E:
            try:
                self.E[v1].remove(v2)
                self.E[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, v1) -> bool:
        if v1 in self.E:
            del self.E[v1]
            for v in self.E:
                self.E[v].remove(v1)
            return True
        return False
