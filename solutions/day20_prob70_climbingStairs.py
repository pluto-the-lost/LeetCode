'''
link: https://leetcode.com/problems/climbing-stairs/description/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
#solution:
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def comb(n,m):
            if m > n/2:
                return comb(n,n-m)
            mul = div = 1
            for i in range(1,m+1):
                mul *= (n-i+1)
                div *= i
            return int(mul/div)
        res=0
        maxStep,minStep = n, n//2+int(n%2!=0)
        for i in range(minStep,maxStep+1):
            res += comb(i,maxStep-i)
        return res
'''
better solutions: (dp can do this but with good refinement)
class Solution:
    dictionary = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = 0
        if n == 0 or n == 1:
            return 1
        if n in self.dictionary:
            return self.dictionary[n]
        else:
            number += self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.dictionary[n] = number
        return number

(and this is also a Fibonacci-like sequence)
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [0, 1, 2]
        if n < 3:
            return steps[n]
        for i in range(3,n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n]
'''