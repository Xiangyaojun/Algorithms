# coding:utf-8

'''
leetcode 64
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
解析：
1.动态规划：设dp[i][j]表示从左上角走到i,j位置最小路径和，则
          dp[i][j] = min(dp[i][j-1],dp[i-1][j])+a[i][j]
          时间复杂度:O(m*n)
'''


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:return 0

        m = len(grid)
        n = len(grid[0])

        dp = m*[[0]*n]

        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[m-1][n-1]

slou= Solution()
print(slou.minPathSum([[1,2],[1,1]]))