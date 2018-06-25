'''
link: https://leetcode.com/problems/subsets/description/


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
#solution
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def addOneIn(now,i):
            if len(now) == len(nums):
                return
            for idx in range(i,len(nums)):
                temp = now+[nums[idx]]
                res.append(temp)
                addOneIn(temp,idx+1)
        res = [[]]
        addOneIn([],0)
        return res
'''
better solution: using a depth variable to indicate the length of now and judge whether to return
'''