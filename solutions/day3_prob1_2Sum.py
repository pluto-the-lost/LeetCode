'''
link: https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#solution: (note that 2Sum requires return of indices, while 3Sum requires return of numbers)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        res = sorted(zip(nums,range(len(nums))),key = lambda x:x[0])
        nums = [pair[0] for pair in res]
        indices = [pair[1] for pair in res]
        smallerHalf = [n for n in nums if n <= target/2]
        for idx,num in enumerate(smallerHalf):
            if idx > 0:
                if num == smallerHalf[idx-1]: continue
            largerPart = nums[idx+1:]
            if len(largerPart) > 0:
                theOtherIdx = bisect.bisect(largerPart,target-num)-1
                if largerPart[theOtherIdx] == target-num: 
                    return([indices[idx],indices[theOtherIdx+idx+1]])