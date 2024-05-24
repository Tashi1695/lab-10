
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = movingtail = ListNode()
        
        while l1 and l2:
            if l1.val <= l2.val:
                movingtail.next = l1
                l1 = l1.next
            else:
                movingtail.next = l2
                l2 = l2.next
            movingtail = movingtail.next
            
        movingtail.next = l1 or l2
        return head.next