# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        a = []
        temp = ListNode()
        temp = head
        while temp != None:
            a.append(temp.val)
            temp = temp.next
        for i in range(len(a)-1,-1,-1):
            if a[i] != head.val:
                return False
            head = head.next
        return True
            