'''
link: https://leetcode.com/problems/n-queens/description/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

#solution:
class Solution:
    def putAQueen(self, feasible, n):
        lastRawFeasible = [i for i,n in enumerate(feasible[-1]) if n]
        leftRaw = len(feasible)
        if leftRaw == 1:
            return([['.'*i+'Q'+'.'*(n-i-1)] for i in lastRawFeasible])
        resList = []
        for idx in lastRawFeasible:
            tempFeasible = copy.deepcopy(feasible[:-1])
            for i in range(leftRaw-1):
                for j in range(len(feasible[0])):
                    if abs(i - leftRaw + 1) == abs(j - idx) or j == idx:
                        tempFeasible[i][j] = False
            tempRes = self.putAQueen(tempFeasible,n)
            for res in tempRes:
                res.append('.'*idx+'Q'+'.'*(n-idx-1))
                resList.append(res)
        return(resList)
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        import copy
        feasible = []
        for i in range(n):
            feasible.append([True]*n)
        return(self.putAQueen(feasible,n))

'''
better solution:
*use nested definition
def fun1(arg1,...):
    def fun2(arg2,...):

class Solution():
    def solveNQueens(self,n):
        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append([queens])
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    //avoid redundant calculation by recording exclusive condition and search if the site for now matches
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
                    //in queens: below, in xy_dif: right below, in xy_sum: left below
        result = []
        dfs([],[],[])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]
'''