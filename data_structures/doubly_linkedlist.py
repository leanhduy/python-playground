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
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index)
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev = new_node
            new_node.prev.next = new_node
            self.length += 1

    def swap_first_last(self):
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Swap the values of the first and last node

        ##### ? CONSTRAINTS ? #####
        The pointers to the nodes themselves are not swapped - only the values are exchanged
        """
        if self.length <= 1:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def reverse(self):
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Reverse the doubly linked list

        ##### ? CONSTRAINTS ? #####
        Do not change the value of any of the nodes
        Only change the pointer `prev` and `next` of each node
        """
        if self.length <= 1:
            return
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        # Update the head and tail pointer
        self.head, self.tail = self.tail, self.head

    def check_palindrome(self) -> bool:
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Check if a doubly linked list is Palindromic

        ##### ? CONSTRAINTS ? #####
        The linked list with length <= 1 is always a palindrome
        """
        if self.length < 1:
            return False
        if self.length == 1:
            return True
        t1 = self.head
        t2 = self.tail
        while t1 != t2:
            if t1.value != t2.value:
                return False
            # Check incase list contains even number of nodes
            if t1.next == t2:
                break
            t1 = t1.next
            t2 = t2.prev
        return True
