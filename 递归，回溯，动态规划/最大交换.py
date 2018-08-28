# coding:utf-8
'''
leetcode 670

题目：给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :
输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :
输入: 9973
输出: 9973
解释: 不需要交换。

解析：
1.记录每个数字的实际index
1.记录最大数字（maxdigit）及其对应的实际索引（maxidx）
2.如果当前数字小于最大数字，则此数字和最大数字是目前为止最大交换的最佳数字。在这种情况下，记录该数字对（leftidx和rightidx）。

'''
class Solution:

    def maximumSwap(self, num):
        nums = []
        while num > 0:
            temp = num % 10
            num = num//10
            nums.append(temp)
        nums = nums[::-1]

        hashmap = {}  # 用hashmap记录每个数字的实际位置
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]
        a = None
        b = None
        list_nums_sort = sorted(nums, reverse=True)
        for i in range(len(list_nums_sort)):
            cur_n = list_nums_sort[i]
            if i not in hashmap[cur_n]:
                max_index = -1
                for h in hashmap[cur_n]:
                    if h > max_index:
                        max_index = h
                a = max_index
                b = i
                break
        if a != None:
            nums[a], nums[b] = nums[b], nums[a]

        result = 0
        for n in nums:
            result = result * 10 + n
        return result



solu = Solution()
nums = [1, 2, 3, 4]
print(solu.maximumSwap(9912))
