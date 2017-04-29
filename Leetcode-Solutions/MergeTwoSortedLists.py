class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None and l2 is None:
            return []
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1
        if l1.val <= l2.val:
            result = l1
            result = ListNode(l1.val)
            result.next = self.mergeTwoLists(l1.next,l2)
        else:
            result = l2
            result = ListNode(l2.val)
            result.next = self.mergeTwoLists(l1,l2.next)
        return result