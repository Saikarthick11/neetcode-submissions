# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        total=0
        while current:
            total+=1
            current=current.next
        dummy=ListNode(0,head)
        current=dummy
        for i in range(total-n):
            current=current.next
        current.next=current.next.next
        return dummy.next
        