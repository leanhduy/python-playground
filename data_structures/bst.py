"""This is the implementation of Binary Search Tree (BST)
    # * OVERVIEW
    Binary Search Tree (BST) is a undirected graph.
    Each node has maximum 2 child nodes
    There is a root node of the tree
    Leaf node is the node that has 0 children
"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.value) if self else "None"


class BST:
    def __init__(self) -> None:
        self.root = None

    def __str__(self) -> str:
        if self.root is None:
            return str(self.root)
        left_branch = BST()
        left_branch.root = self.root.left
        right_branch = BST()
        right_branch.root = self.root.right
        return f"""
        ----
        Node: {self.root}
        Left: {str(left_branch)}
        Right:{str(right_branch)}
        ----
        """

    def insert(self, value) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == value:
                return False
            if temp.value < value:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = new_node
                    return True
            if temp.value > value:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = new_node
                    return False

    def contains(self, value) -> bool:
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if temp.value < value:  # Go to the right
                temp = temp.right
            if temp.value > value:  # Go to the left
                temp = temp.left
        return False
