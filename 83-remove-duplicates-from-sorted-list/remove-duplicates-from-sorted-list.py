# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head #No need to create a new llinked list
        while current: #to tranverse the entire length
            while current.next and current.next.val==current.val:#deletion if both are equal
                current.next=current.next.next
            current=current.next
        return head