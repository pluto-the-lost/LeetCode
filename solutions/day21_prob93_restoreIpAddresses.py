'''
link: https://leetcode.com/problems/restore-ip-addresses/description/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''
#solution: (so ugly)
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def getOneSite(leftS,leftN):
            if len(leftS)<leftN or len(leftS)>3*leftN or leftN==1 and int(leftS)>=256:
                return []
            if leftN==1 and (leftS[0]!='0' or leftS=='0') and int(leftS)<256:
                return [leftS]
            res = []
            for i in range(1,min(4,len(leftS))):
                thisSite = leftS[:i]
                if (thisSite[0]!='0' or thisSite=='0') and int(thisSite)<256:
                    leftChoice = getOneSite(leftS[i:],leftN-1)
                    if leftChoice:
                        for r in leftChoice:
                            res.append(thisSite+'.'+r)
            return res
        return getOneSite(s,4)
'''
better solution: (same speed but much more beautiful)
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res=[]
        self.dfs(s,4,[])
        return ['.'.join(x) for x in self.res]
    
    def dfs(self,s,k,path):
        if len(s)>k*3:
            return
        if k==0:
            self.res.append(path)
        else:
            for i in range(min(3,len(s)-k+1)):
                if i==2 and int(s[:3])>255 or i>0 and s[0]=='0':
                    continue
                self.dfs(s[i+1:],k-1,path+[s[:i+1]])
'''