# coding:utf-8

'''
leetcode 3
题目: 给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 无重复字符的最长子串是 "abc"，其长度为 3。

示例 2:
输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。

解法分析：     
1.暴力解法：时间复杂度分析：首先最外层循环需要遍历不同长度的滑动窗口值，然后一层循环是对每一个滑动窗口大小进行滑动，最后一层循环是对每一个子串判断是否有重复元素，
           所以时间：O(n^3),空间O(n,m)，其中m为字符串不同字符的个数。
2.滑动窗口法：利用一个hashmap存储访问过的字符串，可以看到[i,j-1]的子串一定是没有重复元素的，只需要判断S[j]是否在S[i:j-1]中，
             利用hashmap我们判断判断S[j]是否在S[i:j-1]中只需要O(1), 
             所以时间复杂度：O(2n)=O(n),最坏情况，每个字符被i和j访问2次。
                 空间复杂度：O(n,m)，其中m为字符串不同字符的个数。
3.优化滑动窗口法：如果S[j]在[i:j-1]中的k位置有重复的字符，不需要设置下一个滑动窗口为[i+1，j-1]，可以直接将窗口变为[k+1,j-1],其他与hashmap方法一样，
                所以时间复杂度：O(n)，空间复杂度：O(n,m)，其中m为字符串不同字符的个数。
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        i = 0
        j = 0
        maxlength = 0
        while i < len(s) and j < len(s):
            if s[j] not in hashmap:
                hashmap[s[j]] = j
                j+=1
                maxlength = max(maxlength, j-i)
            else:
                hashmap.pop(s[i])
                i+=1
        return maxlength


solu = Solution()
print(solu.lengthOfLongestSubstring("pwwkew"))
