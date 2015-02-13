class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        result = {}
        for index, item in enumerate(num, 1):
            if target - item not in result:
                result[item] = index
            else:
                return result[target-item], index
                
        return ()