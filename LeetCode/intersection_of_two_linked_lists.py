# LeetCode '160. Intersection of Two Linked Lists' Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hash_set = set()
        current = headA
        while current:
            hash_set.add(current)
            current = current.next
        
        current = headB
        while current:
            if current in hash_set:
                return current
            current = current.next
        return None