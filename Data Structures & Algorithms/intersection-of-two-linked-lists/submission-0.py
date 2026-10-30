# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current=headA
        lenA=0
        while current:
            lenA+=1
            current=current.next
        current=headB
        lenB=0
        while current:
            lenB+=1
            current=current.next
        ptrA=headA
        ptrB=headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                ptrA=ptrA.next
        else:
            for i in range(lenB-lenA):
                ptrB=ptrB.next
        while ptrA!=ptrB:
            ptrA=ptrA.next
            ptrB=ptrB.next
        return ptrA

        