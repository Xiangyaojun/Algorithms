# coding:utf-8

'''
剑指offer 2
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
解析：
1.暴力求解：每一个空格，然后开始移动空格后所有的字符，算法时间复杂度O(n^2)
2.先计算出空格的个数，则可以计算出非空格字符移动后的位置，算法时间复杂度O(n)
'''
class Solution:
    def replaceSpace(self, s):
        space_count = 0
        #计算空格个数
        for i in range(len(s)):
            if s[i]==" ":
                space_count += 1
        if space_count==0: return "".join(s)
        raw_last_index = len(s)-1 #记录原始字符串的最后一个字符位置
        new_last_index = len(s)-1 + space_count*2
        #根据空格个数，提前扩展数组空间，扩展空格数*2个空间
        s += "**" *space_count
        s = list(s)
        for i in range(raw_last_index, -1, -1):
            if s[i] == ' ':
                s[new_last_index] = '0'
                s[new_last_index-1] = '2'
                s[new_last_index-2] = '%'
                new_last_index -= 3
            else:
                s[new_last_index] = s[i]
                new_last_index -= 1
                
        return "".join(s)

solu = Solution()
print(solu.replaceSpace("hello world xiang !"))
