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
        values = []
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return "-".join(values)

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
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
        ##### !!! INTERVIEW QUESTION !!! #####
        FIND THE MIDDLE NODE OF THE LINKED LIST

        ##### ? NOTE ? #####
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
        ##### !!! INTERVIEW QUESTION !!! #####
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
        ##### !!! INTERVIEW QUESTION !!! #####
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
        ##### !!! INTERVIEW QUESTION !!! #####
        Reverse the node of the linked list from node m-th to n-th

        ##### ? CONSTRAINTS ? #####
        m & n are valid
        m < n

        ##### * INPUTS * #####
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

    def partition_list(self, x: int) -> None:
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Partition the linked list based on a value X
        Nodes that have value less than X will come before Nodes that have value equal or greater than X

        ##### ? CONSTRAINTS ? #####
        Preserve the origin relative order of the nodes in each of the two partitions

        ##### * INPUTS * #####
        x: the value that will partition on

        Returns:
            Optional[Node]: returns None if the list is empty. Otherwise, partition the list
        """
        if self.head is None:
            return None

        # Create dummy node
        small = Node(0)
        big = Node(0)
        s_tmp = small
        b_tmp = big

        # Set current to linked list head
        current = self.head
        while current:
            if current.value < x:
                s_tmp.next = current
                s_tmp = current
            else:
                b_tmp.next = current
                b_tmp = current
            current = current.next

        # Terminate the big list
        b_tmp.next = None

        s_tmp.next = big.next
        self.head = small.next

    def remove_duplicates_with_set(self):
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Remove all duplicates in the linked list
        This approach contains 2 pointers and a set
        Time Complexity: O(n) with n is the number of nodes in the list

        ##### ? CONSTRAINTS ? #####
        Preserve the origin relative order of the nodes

        """
        # Initialize an empty set
        myset = set()

        # Init 2 pointers: prev and cur
        prev = None
        current = self.head

        # Iterate through the list
        while current:
            # If value in the set, remove the duplicate
            if current.value in myset:
                prev.next = current.next
                self.length -= 1
            # Otherwise add the value to the set, jumpt to next node
            else:
                myset.add(current.value)
                prev = current
            current = current.next

    def remove_duplicates_without_set(self):
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Remove all duplicates in the linked list
        This approach doesn't use the built-in Set data type


        ##### ? CONSTRAINTS ? #####
        Preserve the origin relative order of the nodes

        ##### * APPROACH EXPLANATION * #####
        We will use 3 pointers: prev, temp, curr
        Time complexity: O(n^2)

        This is the "naive" approach. And will not be preferred in interview
        """
        if self.length <= 1:
            return
        curr = self.head
        while curr is not None:
            prev = curr
            temp = prev.next
            while temp is not None:
                # If duplicates is found. Remove the node and decrese the linked list length
                if temp.value == curr.value:
                    prev.next = temp.next
                    self.length -= 1
                else:
                    prev = prev.next
                temp = temp.next
            curr = curr.next

    def reverse(self):
        """
        ##### !!! INTERVIEW QUESTION !!! #####
        Reverse the whole linked list

        ##### * APPROACH EXPLANATION * #####
        We will use 3 pointers: before, temp, after
        Time complexity: O(n)
        """
        if self.length > 1:
            # Swap the head and tail pointer
            temp = self.head
            self.head = self.tail
            self.tail = temp
            # Swap the pointer next of all nodes
            before = None
            after = temp.next
            while after:
                temp.next = before
                before = temp
                temp = after
                after = after.next
            self.head.next = before

    def bubble_sort(self):
        """
        IMPLEMENT BUBBLE SORT ON LINKED LIST WITHOUT USING EXTRA DATA STRUCTURE
        """
        if self.length > 1:
            after = self.tail
            while after != self.head.next:
                temp = self.head
                while temp.next != after:
                    if temp.value > temp.next.value:
                        temp.value, temp.next.value = temp.next.value, temp.value
                    temp = temp.next
                if temp.value > after.value:
                    temp.value, after.value = after.value, temp.value
                after = temp

    def selection_sort(self):
        if self.length > 1:
            current = self.head
            # Iterate the current pointer until it.next is None
            while current.next is not None:
                temp = current
                min = current
                while temp is not None:
                    if temp.value < min.value:
                        min = temp
                    temp = temp.next
                # At the end of the inner loop, swap the value of min and current node
                current.value, min.value = min.value, current.value
                current = current.next


##### * OTHER LINKED LIST PROBLEMS * (LeetCode) ####
##### ! NOTE: Leetcode define the linked list as the head of the list, which is a node with `val` and `next` pointer ! #####
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    buffer = 0
    l3 = ListNode()
    temp = l3
    # Iterate until one number is exhausted
    while l1 and l2:
        if l1.val + l2.val + buffer < 10:
            temp.next = ListNode(l1.val + l2.val + buffer)
            buffer = 0
        else:
            temp.next = ListNode(l1.val + l2.val + buffer - 10)
            buffer = 1
        l1 = l1.next
        l2 = l2.next
        temp = temp.next
    while l1:
        if l1.val + buffer == 10:
            temp.next = ListNode(0)
            buffer = 1
        else:
            temp.next = ListNode(l1.val + buffer)
            buffer = 0
        l1 = l1.next
        temp = temp.next
    while l2:
        if l2.val + buffer == 10:
            temp.next = ListNode(0)
            buffer = 1
        else:
            temp.next = ListNode(l2.val + buffer)
            buffer = 0
        l2 = l2.next
        temp = temp.next
    if buffer == 1:
        temp.next = ListNode(1)
    return l3.next
