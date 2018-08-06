# coding:utf-8

'''
所有常见排序算法的实现
         最优          最坏      平均        空间      稳定
冒泡排序：O(n)        O(n^2)    O(n^2)       O(1)      是           交换排序
快速排序：O(nlogn)    O(n^2)    O(nlogn)     O(logn)   否

选择排序：O(n^2)      O(n^2)    O(n^2)       O(1)      否           选择排序
堆排序：O(nlogn)     O(nlogn)   O(nlogn)     O(1)      否
'''
class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp 

    '''
    交换排序：冒泡排序 和 快速排序
    '''
    def bubbleSort(self, nums):
        flag = False
        for i in range(0,len(nums)-1):  # n-1趟
            for j in range(len(nums)-1,i,-1):
                if nums[j]<nums[j-1]:
                    self.swap(nums,j,j-1)
                    flag = True
            if flag == False:  # 若一次冒泡后，没有交换元素，证明此时已经有序
                return nums
        return nums

    def quickSort(self, nums, left, right):
        if left < right:
            q = self.partition(nums, left, right)
            self.quickSort(nums, left, q-1)
            self.quickSort(nums, q+1, right)
        return nums

    def partition(self, nums, left, right):
        pivot = nums[left] 
        while left < right:
            while left < right and nums[right] >= pivot: right -= 1
            nums[left] = nums[right] 
            while left < right and nums[left] <= pivot: left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    '''
        选择排序：简单选择排序 和 堆排序
    '''
    def selectSort(self,nums):
        for i in range(len(nums)-1):  # n-1趟
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            self.swap(nums, min, i)
        return nums              
    '''
    堆排序:将数组看成一棵完全二叉树的顺序存储结构，利用完全二叉树的基本性质，节点i的左孩子为2i，右孩子为2i+1
    大根堆：父节点>=子节点
    小根堆：父节点<=子节点
    构造大根堆的过程，是对所有分支节点反复筛选的过程，所谓分支节点指的是[|_n/2_|~1],即，最后一个分支节点为|_n/2_|
    将一个无序数组看成一棵顺序存储结构的完全二叉树，对其建[|_n/2_|~1]每一个分支节点，向下调整建堆，而总体来说，从[|_n/2_|~1],从下往上的遍历过程。
    并没有使用递归和多余的空间，空间复杂度为O(1)
    '''
    
    def heapSort(self,nums):
        self.bulidMaxHeap(nums)
        for i in range(len(nums)-1, 0, -1):
            self.swap(nums,i,1)
            self.adjustDown(nums, 1, i-1)
        return nums

    def bulidMaxHeap(self,nums):
        size = len(nums)-1
        for i in range(size//2, 0, -1):
            self.adjustDown(nums, i, size)

    # 自上向下调整
    def adjustDown(self, nums, k, size):
        # size 表示最大堆长度
        temp = nums[k] #存储需要调整的分支节点值
        i = 2*k  # 此时i节点表示右孩子
        while i <= size:
            # 选择出当前节点左右孩子中较大的一个
            if i < size and nums[i+1] > nums[i]:
                i = i+1

            if nums[i] > temp:
                nums[k] = nums[i]
                k = i
                i = 2*i
            else:
                break
        nums[k] = temp

solu = Solution()
nums =[5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]
print(solu.heapSort(["", 5, 3, 2, 5, 1, 5, 7, 3, 9, 8, 7]))
