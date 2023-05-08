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


class MyQueue:
    """
    This Queue data structure is implemented by using 2 stacks, each stack is a list
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0

    def enqueue(self, value):
        """
        #### ! INTERVIEW QUETSION ! ####
        Implement the enqueue method for a Queue
        You must use list only, linked list is now allowed
        
        #### ? BIG-O ? ####
        Time complexity: O(n)
        Space complexity: O(1)
        """
        # Flush out the stack1 into the stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        # Add the new value to the top of stack1
        self.stack1.append(value)
        # Re-migrate the elements from stack2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
            
    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()