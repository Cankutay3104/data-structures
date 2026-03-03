# LeetCode '1. Two Sum' Hashmap Solution

class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in numbers:
                return [numbers[complement], i]
            else:
                numbers[num] = i
        