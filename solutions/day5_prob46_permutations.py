'''
link: https://leetcode.com/problems/permutations/description/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
#solution:
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteOne(InNums):
            if len(InNums) == 0:
                return [[]]
            res = []
            for idx,num in enumerate(InNums):
                permuteRes = [[num]+i for i in permuteOne(InNums[:idx]+InNums[idx+1:])]
                for item in permuteRes:
                    res.append(item)
            return res
        return permuteOne(nums)

'''
better solutions:
1. short but not faster (actually slower)
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def permuteOne(InNums,OutNums):
            if len(InNums) == 0:
                res.append(OutNums)
                pass
            for idx,num in enumerate(InNums):
                permuteOne(InNums[:idx]+InNums[idx+1:],OutNums+[num])
        permuteOne(nums,[])
        return res

2. faster for a little bit, but seems like saving memory (cannot understand this yet)
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        res = [nums[:]]
        n = len(nums)
        i = n-1
        while i > 0:
            if nums[i-1] < nums[i]:
                j = n-1
                while nums[j] < nums[i-1]:
                    j -= 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = sorted(nums[i:])
                res.append(nums[:])
                i = n-1
            else:
                i -= 1

        return res
'''