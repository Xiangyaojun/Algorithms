# coding:utf-8

'''
题目: 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明: 解集不能包含重复的子集。
解析: n个元素的集合它的子集有2^n个，可以看到算法时间复杂度至少为O(2^n)
1.回溯法: 利用递归树回溯每次元素放入或者不放入的情况。
2.位运算: 每一个子集都可以用二进制编码表示, 基于这个编码可以通过位运算判断某一元素是否被选中。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
import copy

class Solution(object):
    def __init__(self):
        pass
    def subsets_I(self, nums):
        result = [[]]
        item = []
        self.generateNext(0,nums,item,result)
        return result

    def generateNext(self,i,nums,item,result):
        if i>= len(nums):
            return
        else:
            item.append(nums[i])
            result.append(copy.deepcopy(item))
            self.generateNext(i+1, nums,item,result)
            item.pop(-1)
            self.generateNext(i+1,nums,item,result)

    def subsets_II(self, nums):
        # 基于位运算
        result = []
        for i in range(2**len(nums)):
            item = []  # 此时i就是每一个子集的编号，将其转换成二进制以后就可以标记每个元素的状态
            for j in range(len(nums)):
                if i & (2**j) > 0:  # 基于当前编码和2^j与运算，判断nums[j]元素是否被选中
                    item.append(nums[j])
            result.append(item)
        return result
solu = Solution()
print(solu.subsets_II([1, 2, 3]))