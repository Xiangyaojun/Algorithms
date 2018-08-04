# coding:utf-8

'''
剑指offer 1
二维数组中的查找
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
解析：
1.暴力求解：遍历每一个数，O(n^2)
2.左下向右上遍历：O(n)
'''
class Solution:
    def Find(self, target, array):
        row_length = len(array)
        column_length = len(array[0])
        i = row_length - 1
        j = 0
        while(i>=0 and j < column_length):
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                j += 1
            else:
                i -= 1
        return False

