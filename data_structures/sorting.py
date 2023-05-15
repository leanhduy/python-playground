class Sorting:
    def bubble_sort(self, nums):
        """
        ! KEY IDEA !
        Sorting by swapping the ADJACENT pairs that out of order
        """
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def selection_sort(self, nums):
        """
        ! KEY IDEA !
        For each iteration:
            SELECT the MINIMUM value
            Bring it to the TOP of the array/sub-array
        """
        for i in range(len(nums) - 1):
            min_idx = i
            # Find the index of the minimum value
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            # Bring the minimum value to the top of the nums[i:] subarray
            if i != min_idx:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]

    def insertion_sort(self, nums):
        """
        ! KEY IDEA !
        For each iteration
        INSERT the current value at index to the appropriate place
        in the sub-array before it.
        """
        if len(nums) > 1:
            for i in range(1, len(nums)):
                temp = nums[i]
                j = i - 1
                while temp < nums[j] and j > -1:
                    nums[j + 1] = nums[j]
                    nums[j] = temp
                    j -= 1
