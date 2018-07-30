# coding:utf-8

class Solution:
    def __init__(self):
        self.result = []

    def permutation(self, nums, begin, end):
        # 递归算法 当数组中有重复元素时，会重复输出排列，需要在加一步去重的工作
        # 假设总共有n个元素，其核心是：将每个元素放到余下n-1个元素组成的队列最前方，然后对剩余元素进行全排列，依次递归下去
        if begin == end:
            # self.result.append(''.join(nums))
        else:
            for i in range(begin, end+1):
                self.swap(nums, begin, i)
                self.permutation(nums, begin+1, end)
                self.swap(nums, begin, i)

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


solu = Solution()
nums = [1, 2, 3, 4]
solu.permutation(nums, 0, len(nums)-1)
print(solu.result)