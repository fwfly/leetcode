# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
        def mergeTwoLists(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """

            if not l1 and not l2:
                return []
            elif not l1:
                return l2
            elif not l2:
                return l1
            else:

                head = ListNode(-1)
                cur = head
                while (l1 is not None) and (l2 is not None):

                    if l1.val > l2.val:
                        cur.next = l2
                        l2 = l2.next
                    else:
                        cur.next = l1
                        l1 = l1.next
                    cur = cur.next

                if l1 is None:
                    cur.next = l2
                else:
                    cur.next = l1

                return head.next
