# coding:utf-8

'''
字符串模式匹配算法
题目：求一个字符串(m长度)在主串(n长度)中第一次出现的位置
1.暴力求解：时间复杂度: O(n*m)
2.KMP算法：O(n+m)
'''

class Sloution:
    def findIndex(self,s,t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i = i-j+1
                j = 0
        if j == len(t):
            return i-len(t)
        else:
            return -1

solu = Sloution()
print(solu.findIndex("xiang","ian"))