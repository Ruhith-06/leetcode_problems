# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return None

        fast = head
        temp = head
        c = 0
        while(fast):
            fast = fast.next
            c += 1
        mid = c // 2
        i = 0
        slow = head
        while(slow):
            if i == mid - 1:
                slow.next = slow.next.next
                break
            i += 1
            slow = slow.next
                
        return head
            
        
