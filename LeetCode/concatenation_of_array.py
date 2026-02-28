# Leetcode '1929. Concatenation of Array' Solution

class Solution:
    def getConcatenation(self, nums):
        ans = []
        n = len(nums)
        for i in range(n * 2):
            if i >= n:
                ans.append(nums[i-n])
            else:
                ans.append(nums[i])
        return ans