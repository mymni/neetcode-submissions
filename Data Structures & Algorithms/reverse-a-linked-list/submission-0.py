# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head!=None:
            ptr1 = head
            if head.next!=None:
                ptr2 = ptr1.next
            else:
                return head
            ptr1.next = None

                
            while ptr2 != None and ptr2.next!=None:
                ptr3 = ptr2.next
                ptr2.next = ptr1
                ptr1 = ptr2
                ptr2 = ptr3

            ptr2.next = ptr1

            head = ptr2
            return head







        