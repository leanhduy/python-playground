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

    def reverse_between(self, m, n):
        """
        #### !!! INTERVIEW QUESTION !!! ####
        Reverse the node of the linked list from node m-th to n-th

        #### ? CONSTRAINTS ? ####
        m & n are valid
        m < n

        #### * INPUTS * ####
        m - int: the 0-based index of the m-th node
        n - int: the 0-based index of the n-th node

        Returns:
            Optional[Node]: returns None if the list is empty. Otherwise, reverse the nodes from m-th to n-th
        """
        if self.head is None:
            return None

        # This node is for the case of m-th = 0 (Head node is also reversed)
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(m):
            prev = prev.next
        current = prev.next

        for _ in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        self.head = dummy.next
