# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=None
        result=None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                if curr==None:
                    curr=list1
                    result=curr
                else:
                    curr.next=list1
                    curr=curr.next
                list1=list1.next
            else:
                if curr==None:
                    curr=list2
                    result=curr
                else:
                    curr.next=list2
                    curr=curr.next
                list2=list2.next
        while list1 is not None:
            curr.next=list1
            curr=curr.next
            list1=list1.next
        while list2 is not None:
            curr.next=list2
            curr=curr.next
            list2=list2.next
        return result
        