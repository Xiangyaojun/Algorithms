# coding:utf-8
import copy
class Solution:
    def getCombineFeature(self,all_feature,target_name):
        result = []
        pre_name = "comb"
        for s in target_name:
            pre_name += "_" + s
        name_stack = []
        value_stack = []
        row = []
        for i in range(len(target_name)):
            cur_n = target_name[i]
            name_stack.append(cur_n)
            for s in all_feature[cur_n]:
                value_stack.append(s)
            row.append(value_stack.pop())

        return result
all_feature = {"gender":[0,1],"age":[2,3,4],"city":[5,6,7],"education":[8,9]}
target_name = ["gender","age","city"]
slou = Solution()
print(slou.getCombineFeature(all_feature,target_name))
