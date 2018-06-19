'''
link: https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

#solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        newHead,cursor = None,None
        l = [l1,l2]
        while(l[0] != None and l[1] != None):
            minIdx = int(l[0].val>l[1].val)
            #print(l[minIdx].val)
            if newHead == None:
                newHead = l[minIdx]
                cursor = newHead
            else:
                cursor.next = l[minIdx]
                cursor = cursor.next
            l[minIdx] = l[minIdx].next
        #printList(newHead)
        if l[0] != None:
            cursor.next = l[0]
        elif l[1] != None:
            cursor.next = l[1]
        return newHead

'''
better solution: (faster and shorter)
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            return l1 or l2
        newHead = cursor = ListNode(0)
        l = [l1,l2]
        while(l[0] != None and l[1] != None):
            minIdx = int(l[0].val>l[1].val)
            cursor.next = l[minIdx]
            cursor = cursor.next
            l[minIdx] = l[minIdx].next
        if l[0] != None or l[1] != None:
            cursor.next = l[0] or l[1]
        return newHead.next
'''