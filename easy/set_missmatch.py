# https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = {}
        true_set = set(num for num in range(1, max(nums) + 2))
        for num in nums: 
            if res.get(num):
                dupl = num 
            else: 
                true_set.remove(num)
                res[num] = 1
        return [dupl, min(true_set)]