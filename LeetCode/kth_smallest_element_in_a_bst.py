# LeetCode '230. Kth Smallest Element in a BST' Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        if root is None:
            return -1

        stack = []
        counter = 0

        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left 
                
            current = stack.pop()
            counter += 1
            if counter == k:
                return current.val
            current = current.right
