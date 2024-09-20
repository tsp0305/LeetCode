# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        temp = ListNode()
        temp = head
        cnt = 0
        while temp != None:
            cnt += 1
            temp = temp.next
        mid = cnt // 2
        for i in range(mid):
            head = head.next
        return head
       
        

        