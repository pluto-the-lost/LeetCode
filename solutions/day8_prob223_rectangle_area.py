'''
link: https://leetcode.com/problems/rectangle-area/description/

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
'''
#solution:
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        iLeft, iRight, iUp, iDown = max(A,E), min(C,G), min(D,H), max(B,F)
        area1, area2 = (D-B)*(C-A), (H-F)*(G-E)
        areaI = max(0,iUp-iDown)*max(0,iRight-iLeft)
        return area1+area2-areaI

'''
better solution: (faster but i don't know why)
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        sum_area = (C-A)*(D-B) + (G-E)*(H-F)
        
        l_x, l_y = max(A, E), max(B, F)
        u_x, u_y = min(C, G), min(D, H)
        if l_x <= u_x and l_y <= u_y:
            return sum_area - (u_x-l_x)*(u_y-l_y)
        return sum_area
'''