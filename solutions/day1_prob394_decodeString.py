'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
#solution:
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        leftBracketList = []
        correspondingNumStart = []
        idx = 0
        while(idx != len(s)):
            #print(idx,len(s))
            if s[idx] == '[':
                leftBracketList.append(idx)  #a stack saving the idx of left brackets
                for backIdx in range(1,idx+1):
                    if (not s[idx-backIdx].isdigit()):
                        correspondingNumStart.append(idx-backIdx+1)
                        break
                    if backIdx == idx:
                        correspondingNumStart.append(0)
            elif s[idx] == ']':   #seen a right bracket, pop the last left bracket, decode the string inside this bracket pair, recursively
                lastLeftBracketIdx = leftBracketList[-1]
                lastNumStart = correspondingNumStart[-1]
                #print(correspondingNumStart[-1],lastLeftBracketIdx)
                replicateTimes = int(s[lastNumStart:lastLeftBracketIdx])
                tempStr = self.decodeString(s[lastLeftBracketIdx+1:idx])
                s = s[:lastNumStart] + replicateTimes*tempStr + s[idx+1:]
                idx = lastNumStart + replicateTimes*len(tempStr) - 1    #change idx to the end of temp str
                leftBracketList.pop()
                correspondingNumStart.pop()
            idx+=1
        return(s)