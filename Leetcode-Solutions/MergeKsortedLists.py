class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        start = 0
        end = len(lists) - 1
        while start != end or end != 0:
            if start >= end:
                start = 0
            else:
                lists[start] = self.mergeTwoLists(lists[start], lists[end])
                start += 1
                end -= 1
        return lists[0]
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        current = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return head.next