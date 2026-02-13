# LeetCode '234. Palindrome Linked List' Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        # Finding the middle, splitting in half
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reversing the right side
        prev = None
        curr = slow

        while curr:
            next_el = curr.next
            curr.next = prev
            prev = curr
            curr = next_el

        # Checking whether palindrome
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            