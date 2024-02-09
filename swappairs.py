class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode(0, head)
        while node.next and node.next.next:  
            node.next.next.next, node.next.next, node.next, node =\
              node.next, node.next.next.next, node.next.next, node.next
        return head.next
