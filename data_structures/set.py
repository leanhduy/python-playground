def remove_duplicates_with_set(nums):
    """
    ! INTERVIEW QUESTIONS !
    You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then return the updated list.

    You need to implement a function remove_duplicates(my_list) that takes in the input list `my_list` as a parameter and returns a new list with no duplicates.

    Your function should not modify the original list, instead, it should create a new list with unique values and return it.

    Example:
    Input:
    my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]

    Output:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]


    Note:

    The order of the elements in the updated list may be different from the original list, as sets are unordered.
    """
    return list(set(nums))


def has_unique_chars(string):
    """
    ! INTERVIEW QUESTIONS !
    Given a string.
    Return True if all the character in the string are unique
    """
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True


def find_pairs(arr1, arr2, target):
    """
    ! INTERVIEW QUESTION !
    Given 2 list of numbers, `arr1` and `arr2`, and a number `target`.
    Return the list contains all (num1, num2) pairs
    num1 is a number in arr1
    num2 ins a number in arr2
    num1 + num2 == target

    ? BIG-0 ?
    Your solution should have time complexity of O(N)
    """
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs


def longest_consecutive_sequence(nums):
    seq = set()
    for n in nums:
        if n + 1 in nums or n - 1 in nums:
            seq.add(n)
    return len(seq)
