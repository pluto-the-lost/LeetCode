'''
link: https://leetcode.com/problems/plus-one/description/

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

#solution:
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carryCursor = -1
        while(-carryCursor<=len(digits)):
            if digits[carryCursor] != 9:
                digits[carryCursor] += 1
                return(digits)
            else:
                digits[carryCursor] = 0
                carryCursor -= 1
        return([1]+digits)