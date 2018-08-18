'''
题目:给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
样例:
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
解析：
1.暴力解法：依次遍历数组中每一个数，第一次找到的target的位置就是目标，时间复杂度：O(n)
2.二分查找法：本身二分查找可以定位数组中某一个target的位置，由于我们是要找第一次出现target的位置，比如在[1, 2, 3, 3, 4, 5, 10]找3这个数，
通过第一次查找mid，判断nums[mid]是否等于target，如果等于则第一次出现target坐标一定在[left,mid]之中，同理如果想找最后一次出现target的坐标，则target坐标一定在[mid,right]之中
这里需要设置终止条件left + 1 < right，为两个指针相隔为1时候接结束。

'''
class Solution:
    def binarySearch(self,nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left + 1 < right:  # 终止条件为两个指针相隔为1时候接结束，普通二分查找终止条件Wie两个指针相等时终止。
            mid = left + right//2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid + 1
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1

solu = Solution()
print(solu.binarySearch([1, 2], 3))