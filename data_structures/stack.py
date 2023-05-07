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
