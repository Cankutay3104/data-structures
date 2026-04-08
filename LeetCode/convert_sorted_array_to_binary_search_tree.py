# LeetCode "108. Convert Sorted Array to Binary Search Tree" Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        return self._bst_helper(nums, 0, len(nums) - 1)
    
    def _bst_helper(self, nums, left, right):
        if left > right:
            return None
        
        middle = (left + right) // 2
        
        middleNode = TreeNode(nums[middle])
        middleNode.left = self._bst_helper(nums, left, middle - 1)
        middleNode.right = self._bst_helper(nums, middle + 1, right)
        
        return middleNode