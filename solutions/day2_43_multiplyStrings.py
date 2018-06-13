'''
link: https://leetcode.com/problems/multiply-strings/description/


Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''
'''
#version1 (TLE):
class Solution:
    def getNum(self,num,idx):
        if idx in range(-len(num),len(num)):
            return(int(num[idx]))
        else:
            return(0)
    def add_strings(self,num1,num2):
        #if not num1.isdigit() or not num2.isdigit():
        #    return('not digit')
        carry = 0
        sum_str = ''
        for idx in range(max(len(num1),len(num2))):
            tempSum = int(carry + self.getNum(num1,-(idx+1)) + self.getNum(num2,-(idx+1)))
            sum_str = str(tempSum % 10) + sum_str
            carry = int(tempSum / 10)
            #print(carry)
        return(bool(carry)*str(carry) + sum_str)
    def string_times_single_number(self,num_str,num):
        product_str = '0'
        for idx in range(int(num)):
            product_str = self.add_strings(product_str,num_str)
        return(product_str)
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) != len(num2):
            num1,num2 = [num for num in [num1,num2] if len(num)==max(len(num1),len(num2))][0],[num for num in [num1,num2] if len(num)==min(len(num1),len(num2))][0]
        product_str = '0'
        for idx in range(len(num2)):
            product_str = self.add_strings(product_str,self.string_times_single_number(num1,num2[-(idx+1)])+idx*'0')
        return(product_str)
'''

#submit version:
class Solution:
    def plus_one(self,digits):
        carryCursor = len(digits)-1
        while(carryCursor>=0):
            if digits[carryCursor] != '9':
                return(digits[:carryCursor]+str(int(digits[carryCursor])+1)+digits[carryCursor+1:])
            else:
                digits = digits[:carryCursor]+'0'+digits[carryCursor+1:]
                carryCursor -= 1
        return('1'+digits)
    def add_strings(self,num1,num2):
        num1Len,num2Len = len(num1),len(num2)
        if num1Len != num2Len:
            num1Len,num2Len = max(num1Len,num2Len),min(num1Len,num2Len)
            num1,num2 = [num for num in [num1,num2] if len(num)==num1Len][0],[num for num in [num1,num2] if len(num)==num2Len][0]
        carry = 0
        sum_str = ''
        for idx in range(num2Len):
            tempSum = int(carry + int(num1[-idx-1]) + int(num2[-idx-1]))
            sum_str = str(tempSum % 10) + sum_str
            carry = int(tempSum / 10)
        if not carry:
            sum_str = num1[:num1Len-num2Len] + sum_str
        else:
            sum_str = self.plus_one(num1[:num1Len-num2Len]) + sum_str
        return(sum_str)
    def string_times_single_number(self,num_str,num):
        product_str = '0'
        for idx in range(int(num)):
            product_str = self.add_strings(product_str,num_str)
        return(product_str)
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1Len,num2Len = len(num1),len(num2)
        if num1Len != num2Len:
            num1,num2 = [num for num in [num1,num2] if len(num)==max(num1Len,num2Len)][0],[num for num in [num1,num2] if len(num)==min(num1Len,num2Len)][0]
        product_str = '0'
        for idx in range(len(num2)):
            product_str = self.add_strings(product_str,self.string_times_single_number(num1,num2[-(idx+1)])+idx*'0')
        return(product_str)
'''
better solution:
num1 = list(num1)[::-1]
num2 = list(num2)[::-1]
num3 = [0 for _ in range(len(num1)+len(num2))]

for i in range(len(num1)):
    for j in range(len(num2)):
        num3[i+j] += int(num1[i]) + int(num2[j])

for i in range(len(num3)):
    num3[i+1] += num3[i] // 10
    num3[i] = num3[i] % 10

res = ''.join(str(n) for n in num3[::-1])
return(res)
'''