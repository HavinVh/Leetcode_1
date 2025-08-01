# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        answer=ListNode()
        current=answer

        bal=0

        while l1 or l2 or bal:
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            ans=a+b+bal
            bal=ans//10
            ans=ans%10
            current.next=ListNode(ans)
            current=current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        return answer.next



            
        
        

            
