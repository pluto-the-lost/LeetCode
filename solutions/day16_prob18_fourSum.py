'''
link: https://leetcode.com/problems/4sum/description/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
#solution:
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(0,len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            threeSum=target-nums[i]
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left,right = j+1,len(nums)-1
                twoSum = threeSum-nums[j]
                while(left<right):
                    #print(left,right,nums[left],nums[right],twoSum)
                    if nums[left]+nums[right]<twoSum:
                        left += 1
                    elif nums[left]+nums[right]>twoSum:
                        right -= 1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while(nums[left]==nums[left-1] and left<right): left+=1
                        while(nums[right]==nums[right+1] and left<right): right-=1
        return res
'''
better solution: (some judgement to avoid some useless calculation)
if sum(nums[i: i + 4]) > target: break
if nums[i] + sum(nums[-3:]) < target: continue
'''