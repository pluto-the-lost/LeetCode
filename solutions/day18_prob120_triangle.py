'''
link: https://leetcode.com/problems/triangle/description/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
#solution:
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        pathSum = [triangle[0]]
        for depth in range(1,len(triangle)):
            layer = triangle[depth]
            layerSum = []
            for idx,num in enumerate(layer):
                if idx==0:
                    layerSum.append(pathSum[depth-1][0]+num)
                elif idx>0 and idx<depth:
                    layerSum.append(min(pathSum[depth-1][idx-1],pathSum[depth-1][idx])+num)
                else:
                    layerSum.append(pathSum[depth-1][idx-1]+num)
            pathSum.append(layerSum)
        return min(pathSum[-1])
'''
better solution:(down-top, faster and only O(1) extra space used)
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        for i in range(length - 1, 0, -1):
            for j in range(1, len(triangle[i])):
                if triangle[i][j] < triangle[i][j-1]:
                    triangle[i-1][j-1] += triangle[i][j]
                else:
                    triangle[i-1][j-1] += triangle[i][j - 1]
        return triangle[0][0]
'''