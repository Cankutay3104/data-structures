# LeetCode '83. Remove Duplicates from Sorted List' Solution

class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head