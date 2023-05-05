from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self) -> str:
        temp = self.head
        values = []
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return " ".join(values)

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None
        if index <= int(self.length / 2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index: int, value: int) -> bool:
        node = self.get(index)
        if node is None:
            return False
        node.value = value
        return True

    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False
