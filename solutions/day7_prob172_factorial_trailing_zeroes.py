'''
link: https://leetcode.com/submissions/detail/159824389/

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''
#solution:
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        divisor = 5
        while(n//divisor > 0 ):
            res += n//divisor
            divisor *= 5
        return res
'''
better solution:
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while(n//5 > 0 ):
            n = n//5
            res += n
        return res
'''