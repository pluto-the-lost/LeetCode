'''
link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
#solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = cursor = head
        for i in range(n):
            tail = tail.next
        if tail == None:
            return cursor.next
        while(tail.next != None):
            cursor = cursor.next
            tail = tail.next
        cursor.next = cursor.next.next
        return head
'''
better solution: (actually the same algorithm, differ in how to deal with n=len(List))
tail = cursor = pretendHead = ListNode(None)
pretendHead.next = head
#and then the judgement of whether tail is None can be escaped
'''