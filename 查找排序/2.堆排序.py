# coding:utf-8

'''
         最优          最坏      平均        空间      稳定
堆排序：O(nlogn)     O(nlogn)   O(nlogn)     O(1)      否
'''


class Solution:
    def __init__(self):
        pass
    '''
        堆排序:将数组看成一棵完全二叉树的顺序存储结构，利用完全二叉树的基本性质，节点i的左孩子为2i，右孩子为2i+1
        大根堆：父节点>=子节点
        小根堆：父节点<=子节点
        构造大根堆的过程，是对所有分支节点反复筛选的过程，所谓分支节点指的是[|_n/2_|~1],即，最后一个分支节点为|_n/2_|
        将一个无序数组看成一棵顺序存储结构的完全二叉树，对其建[|_n/2_|~1]每一个分支节点，向下调整建堆，而总体来说，从[|_n/2_|~1],从下往上的遍历过程。
        并没有使用递归和多余的空间，空间复杂度为O(1)
    '''

    def heapSort(self, nums):
        self.bulidMaxHeap(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.adjustDown(nums, 0, i - 1)
        return nums

    def bulidMaxHeap(self, nums):
        size = len(nums)
        for i in range(size // 2, 0, -1):  # 调整 [|_n/2_|~1]
            self.adjustDown(nums, i - 1, size - 1)

    # 自上向下调整
    def adjustDown(self, nums, k, size):
        # size 表示最大堆长度
        temp = nums[k]  # 存储需要调整的分支节点值
        i = 2*k + 1  # 此时2*k+1节点表示左孩子，2k+2为右孩子
        while i < size:
            # 选择出当前节点左右孩子中较大的一个
            if nums[i + 1] > nums[i]:
                i = i + 1

            if nums[i] > temp:
                nums[k] = nums[i]
                k = i
                i = 2*i
            else:
                break
        nums[k] = temp

solu = Solution()
nums = [5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]
print(solu.heapSort(nums))
