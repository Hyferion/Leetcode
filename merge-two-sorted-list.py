class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        while l1.next:
            print(l1.val)
            if l1.val <= l2.val:
                l3.val = l1.val
                l1 = l1.next


