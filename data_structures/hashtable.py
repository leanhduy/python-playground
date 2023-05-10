from typing import Optional


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % (len(self.data_map))
        return my_hash

    def print_table(self):
        for i, item in enumerate(self.data_map):
            print(i, ": ", item)

    def set_item(self, key, value):
        idx = self.__hash(key)
        if self.data_map[idx] is None:
            self.data_map[idx] = []
        self.data_map[idx].append([key, value])

    def get_item(self, key):
        idx = self.__hash(key)
        for item in self.data_map[idx]:
            if key in item:
                return item
        return None

    def keys(self):
        """
        Return all the keys in the hashtable
        """
        keys = []
        for row in self.data_map:
            if row:
                for key, value in row:
                    keys.append(key)
        return keys


def has_common_item(s1, s2) -> bool:
    """
    ! INTERVIEW QUESTION !
    Check if two list has common item
    * BIG-O *
    Naive approach: Nested Loop = O(n^2)
    This approach: Use Python dict (which is a hashtable) = O(n)
    """
    d1 = dict()
    for item in s1:
        d1[item] = True
    for item in s2:
        if d1.get(item):
            return True
    return False


def find_duplicates(nums):
    """
    ! INTERVIEW QUESTION !
    Return the list of all duplicates number
    * BIG-O *
    This approach: Use Python dict (which is a hashtable) = O(n)
    """
    d = dict()  # d for duplicates
    for num in nums:
        if d.get(num) is None:
            d[num] = True
        else:
            d[num] = False
    result = [k for _, k in enumerate(d) if d[k] == False]
    return result


def first_non_repeating_char(s: str) -> Optional[str]:
    """
    ! INTERVIEW QUESTION !
    Find the first non duplicate letter in a string
    * BIG-O *
    This approach: Use Python dict (which is a hashtable) = O(n)
    """
    d = dict()
    for c in s:
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1
    for k in d.keys():
        if d[k] == 1:
            return k
    return None
