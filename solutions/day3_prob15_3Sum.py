'''
link: https://leetcode.com/problems/3sum/description/


Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

#python solution, NOT AC(TLE at test case 312)
class Solution:
    def twoSum(self, nums, goal):
        #nums = sorted(nums)
        resList = []
        smallerHalf = [n for n in nums if n <= goal/2]
        for idx,num in enumerate(smallerHalf):
            if idx > 0:
                if num == smallerHalf[idx-1]: continue
            largerPart = nums[idx+1:]
            if largerPart != []:
                if largerPart[bisect.bisect(largerPart,goal-num)-1] == goal-num: 
                    resList.append([num,goal-num])
        return(resList)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import bisect
        nums = sorted(nums)
        resList = []
        smallestOne = [n for n in nums if n <= 0]
        for idx,num in enumerate(smallestOne):
            if idx > 0:
                if num == smallestOne[idx-1]: continue
            leftTwo = self.twoSum(nums[idx+1:],-num)
            if leftTwo != []:
                for pair in leftTwo:
                    resList.append([num]+pair)
        return(resList)