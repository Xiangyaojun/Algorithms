'''
leetcode 51
题目: n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
8皇后问题: 将八个皇后摆在一张8*8的国际象棋棋盘上，使每个皇后都无法吃掉别的皇后，一共有多少种摆法？
注意: 每一个皇后摆放后，位置与其在同一行、列和斜线的敌方棋子都可以被吃掉。
1.暴力解法:单单基于从n*n中选择n个位置的组合数来看，有C(n^2,n)种可能，但从行来看，每一行只允许放置一个皇后，故基于这个性质总共有n!种不同的摆法。
2.回溯法:
'''

import copy

class Solution:
    def __init__(self):
        self.result = []
        self.str_result = []

    def solveNQueens(self, n):
        x = [0 for i in range(n)]
        self.queen(x, 0, n)

    def queen(self, x, row, n):
        if row == n:
            self.result.append(copy.deepcopy(x))
            one_result = []
            for i in range(len(x)):
                temp_str = "."*n
                temp_str = list(temp_str)
                temp_str[x[i]] = 'Q'
                one_result.append("".join(temp_str))
            self.str_result.append(one_result)
        else:
            for i in range(n):
                x[row] = i
                if self.is_ok(x, row):
                    self.queen(x, row+1, n)

    def is_ok(self, x, row):
        for j in range(row):
            # 首先肯定是不同行的，主要判断在col列上是否相等，故x[row] == x[j]表示row行放皇后的位置和j行放皇后的列相同
            # 左由斜线是否相等，即可以判断两个放皇后的位置，行号差是否等于列号差
            if x[row] == x[j] or abs(x[row]-x[j]) == row-j:
                return False
        return True

solu = Solution()
solu.solveNQueens(4)
print(solu.result)