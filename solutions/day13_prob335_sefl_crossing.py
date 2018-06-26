'''
link: https://leetcode.com/problems/self-crossing/description/

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:
Given x = [2, 1, 1, 2],
?????
?   ?
???????>
    ?

Return true (self crossing)
Example 2:
Given x = [1, 2, 3, 4],
????????
?      ?
?
?
?????????????>

Return false (not self crossing)
Example 3:
Given x = [1, 1, 1, 1],
?????
?   ?
?????>

Return true (self crossing)
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''
#solution: (a Finite-state machine)
class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        last4 = [0]*4
        status = 'out'
        for n in x:
            if status == 'in' and n>=last4[2]:
                return True
            if status == 'judge':
                if n>=last4[2] - last4[0]:
                    return True
                else: status = 'in'
            if status == 'out' and n<last4[2] - last4[0]:
                status = 'in'
            elif status == 'out' and n>=last4[2] - last4[0] and n<=last4[2]:
                status = 'judge'
            last4.append(n)
            del last4[0]
        return False
'''
better solution: (beautiful)
class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False
'''