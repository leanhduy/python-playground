from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = self.tail = None

    def __str__(self) -> str:
        temp = self.head
        node_values = []
        while temp:
            node_values += str(temp.value)
            temp = temp.next
        return "-".join(node_values)

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def find_middle_node(self) -> Optional[Node]:
        """
        ### !!! INTERVIEW QUESTION !!! ###
        FIND THE MIDDLE NODE OF THE LINKED LIST

        ### ? NOTE ? ###
        In the linked list with even number of nodes, return the first node of the second half of the linked list
        e.g. Linkedlist 1-2-3-4 's middle node would be 2

        Returns:
            bool: returns True if the loop contains a loop. False otherwise
        """
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self) -> bool:
        """
        ### !!! INTERVIEW QUESTION !!! ###
        CHECK IF THE LINKED LIST CONTAINS A LOOP

        Returns:
            bool: returns True if the loop contains a loop. False otherwise
        """
        slow = self.head
        fast = self.tail
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    def find_kth_from_end(self, k):
        """
        ### !!! INTERVIEW QUESTION !!! ###
        FIND THE K-TH NODE FROM THE END OF A LINKED LIST

        Returns:
            Optional[Node]: returns None the linked list is shorter than k. Otherwise return the k-th node (from the end)
        """
        slow = self.head
        fast = self.head
        # Set `fast` pointer to be k nodes a head of `slow` pointer
        for _ in range(k):
            if fast is None:
                return slow
            fast = fast.next
        while fast is not None:
            # Move slow and fast forward until fast is None
            slow = slow.next
            fast = fast.next
        return slow
