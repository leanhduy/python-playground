from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.front = new_node
        self.rear = new_node
        self.length = 1

    def __str__(self) -> str:
        values = []
        temp = self.front
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return " ".join(values)

    def clear(self):
        self.length = 0
        self.front = None

    def enqueue(self, value) -> bool:
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
        return True

    def dequeue(self) -> Optional[Node]:
        if self.front is None:
            return None
        temp = self.front
        if self.length == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            temp.next = None
        self.length -= 1
        return temp
