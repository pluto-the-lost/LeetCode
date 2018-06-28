'''
link: https://leetcode.com/problems/edit-distance/description/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''
#solution: (Smitsh-Waterman algorithm-like)
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dpMatrix = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(word1)):
            dpMatrix[i+1][0] = i+1
        for j in range(len(word2)):
            dpMatrix[0][j+1] = j+1
        for i in range(len(word1)):
            for j in range(len(word2)):
                dpMatrix[i+1][j+1] = min([dpMatrix[i][j+1]+1,dpMatrix[i+1][j]+1,dpMatrix[i][j]+int(word1[i]!=word2[j])])
        return dpMatrix[-1][-1]
'''
better solution: (recursive algorithm, about 2 times faster, but why)
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = {}
        def edit(i, j):
            if (i, j) not in dp:
                if not (i and j):
                    dp[i, j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i, j] = edit(i - 1, j - 1)
                else:
                    dp[i, j] = min(edit(i - 1, j) + 1, edit(i, j - 1) + 1,
                                   edit(i - 1, j - 1) + 1)
            return dp[i, j]

        return edit(len(word1), len(word2))
'''