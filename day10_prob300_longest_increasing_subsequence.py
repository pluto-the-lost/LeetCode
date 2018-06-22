'''
link: https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''
#solution:
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpList = [0]*(len(nums)+1) #len(nums)+1 to avoid error in max(dpList) when nums=[]
        for idx,num in enumerate(nums):
            dpList[idx] = max([dpList[i] for i,n in enumerate(nums[:idx]) if n<num]+[0]) + 1
        return max(dpList)

'''
better solution: (ten times faster, nlogn)
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = [nums[0]]
        def binarySearch(l,target):
            left , right = 0 , len(l)-1
            while left < right:
                mid = (left + right)//2
                if l[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        for i in range(1,len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                res[binarySearch(res,nums[i])] = nums[i]
        return len(res)
'''