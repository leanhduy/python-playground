from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def __str__(self) -> str:
        values = []
        temp = self.top
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return " ".join(values)

    def clear(self):
        self.length = 0
        self.top = None

    def push(self, value) -> bool:
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp


class StackList:
    """
    Create a stack using a list
    """

    def __init__(self) -> None:
        self.stack_list = []

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def push(self, value):
        self.stack_list.append(value)

    def pop(self) -> Optional[int]:
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def is_balanced_parentheses(str: str) -> bool:
    """
    ##### ! INTERVIEW QUESTION ! ####
    Check if parentheses in a string is balanced
    * NOTE *
    Using list type to implement the stack
    """
    s = StackList()
    for c in str:
        if c == "(":
            s.push(c)
        if c == ")":
            if s.is_empty() or s.pop() != "(":
                return False
    return len(s.stack_list) == 0
