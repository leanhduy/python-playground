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


def group_anagrams(words):
    """
    ! INTERVIEW QUESTION !
    Given a list of words.
    Return a list of group of anagrams words
    * BIG-O *
    sorted() has time complexity of O(n log n)
    loop has time complexity of O(m)
    Time complexity = O(m * n log n)
    """
    result = {}
    if len(words) == 0:
        return []
    for word in words:
        canonical = "".join(sorted(word))  # O(n log n), n is the size of the word
        if result.get(canonical) is None:
            result[canonical] = [word]
        else:
            result[canonical].append(word)
    return [group for group in result.values()]


def two_sum(nums, sum):
    """
    ! INTERVIEW QUESTION !
    Problem: Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = sum - num
        if num_map.get(complement) is not None:
            return [num_map.get(complement), i]
        else:
            num_map[num] = i
    return []


def subarray_sum(nums, target):
    """
    ! INTERVIEW QUESTION !
    Given an array of integers nums and a target integer target, write a function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

    ? INPUTS ?
    nums: a list of integers representing the input array
    target: an integer representing the target sum

    ? OUTPUT ?
    Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.
    """
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []


def count_good_pairs(nums):
    """
    Given an array of number
    Return the number of good pairs in the array
    A pair (i, j) is a good pair if i < j and nums[i] == nums[j]
    """
    index_dict = {}
    count = 0
    for i, num in enumerate(nums):
        if index_dict.get(num) is None:
            index_dict[num] = [i]
        else:
            count += len(index_dict[num])
            index_dict[num].append(i)
    return count


def count_smaller_numbers_than_current(nums):
    """
    * PROBLEM *\n
    Given array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it.
    That is, for each `nums[i]` you have to count the number of valid `j`'s such that `j != i` and `nums[j] < nums[i]`.

    Return the answer in an array.

    ? INPUT ? \n
    An array of numbers `nums`

    ! CONSTRAINTS !\n
    2 <= `nums.length` <= 500 \n
    0 <= `nums[i]` <= 100
    """
    temp = sorted(nums)
    mapping = {}
    result = []
    for i in range(len(temp)):
        if temp[i] not in mapping:
            mapping[temp[i]] = i
    for i in range(len(nums)):
        result.append(mapping[nums[i]])
    return result
