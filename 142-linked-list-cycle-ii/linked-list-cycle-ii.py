# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow=fast=head
        
        while fast and fast.next:
            slow=slow.next
            
            
            fast=fast.next.next
            if slow==fast:
                new=head
                while slow != new:
                    new=new.next
                    slow=slow.next
                return new
                
                
        return None


        