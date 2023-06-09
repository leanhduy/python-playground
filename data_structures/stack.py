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
        """Check whether the stack is empty

        Returns:
            bool: _description_
        """
        return len(self.stack_list) == 0

    def peek(self):
        """Return the bottom element of the stack

        Returns:
            int: the value at the bottom of the stack
        """
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        """Return the size of the stack"""
        return len(self.stack_list)

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


def reverse_string(s: str) -> str:
    """
    ##### ! INTERVIEW QUESTION ! ####
    Given a string, return the reversed string
    * NOTE *
    Using list type to implement the stack
    """
    if len(s) == 0:
        return s
    my_stack = StackList()
    # Push every single characters into the stack
    for c in s:
        my_stack.push(c)
    # To get the result, simply pop all character out of the stack
    reversed_str = []
    while not my_stack.is_empty():
        reversed_str.append(my_stack.pop())

    return "".join(reversed_str)


def sort_stack_list(input_stack: StackList) -> StackList:
    """
    ##### ! INTERVIEW QUESTION ! ####
    Sort a stack implemented using list type
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # create a new instance stack
    sorted_stack = StackList()
    # while the input stack is not empty
    while input_stack.size() > 0:
        temp = input_stack.pop()
        while sorted_stack.size() > 0:
            if sorted_stack.peek() > temp:
                input_stack.push(sorted_stack.pop())
            else:
                break
        sorted_stack.push(temp)
    while sorted_stack.size() > 0:
        input_stack.push(sorted_stack.pop())


s = StackList()
s.push(3)
s.push(1)
s.push(5)
s.push(4)
s.push(2)
sort_stack_list(s)
