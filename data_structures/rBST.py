"""This is the implementation of Binary Search Tree (RBST) but using recursion techniques
    # * OVERVIEW
    Binary Search Tree (RBST) is a undirected graph.
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


class RBST:
    def __init__(self) -> None:
        self.root = None

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

    def r_contains(self, value) -> bool:
        return self.__r_contains(self.root, value)

    def __r_contains(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        if current.value < value:
            return self.__r_contains(current.right, value)
        # We use another if instead of else for better readability
        if current.value > value:
            return self.__r_contains(current.left, value)

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.root = self.__r_insert(self.root, value)

    def __r_insert(self, current, value):
        # base case
        if current is None:
            return Node(value)
        if current.value < value:
            current.right = self.__r_insert(current.right, value)
        if current.value > value:
            current.left = self.__r_insert(current.left, value)
        return current

    def __minimum_of_subtree(self, node):
        """
        Return the minimum value of a subtree, given a root of that tree
        """
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp.value

    def __r_delete(self, current, value):
        if current is None:
            return None
        if value < current.value:
            current.left = self.__r_delete(current.left, value)
        elif value > current.value:
            current.right = self.__r_delete(current.right, value)
        else:
            if current.left is None and current.right is None:
                return None
            elif current.left is None:
                current = current.right
            elif current.right is None:
                current = current.left
            else:
                # Find the minimum value of the subtree on the right branch
                minimum = self.__minimum_of_subtree(current.right)
                # Update the value of current node
                current.value = minimum
                # Delete the node with minimum on the right branch
                current.right = self.__r_delete(current.right, minimum)
        return current

    def r_delete(self, value):
        if self.root is None or not self.r_contains(value):
            return
        else:
            self.root = self.__r_delete(self.root, value)


t2 = RBST()
t2.r_insert(21)
t2.r_insert(10)
t2.r_insert(47)
t2.r_insert(5)
t2.r_insert(3)
t2.r_insert(4)
t2.r_delete(10)
