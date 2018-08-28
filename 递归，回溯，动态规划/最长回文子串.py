# coding:utf-8

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
1.暴力求解法：时间复杂度O(n^3),
2.
'''


class Solution:
    def longestPalindrome(self, s):
        pass

    def judgeR_Str(self,s,left,right):
        while left<right:
            if s[left]!=s[right]:
                break
            else:
                left += 1
                right -= 1
        return left>=right

slou = Solution()
print(slou.judgeR_Str("abaaa",0,4))