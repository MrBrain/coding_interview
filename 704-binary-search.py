#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

    [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

    13
