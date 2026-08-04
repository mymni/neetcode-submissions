class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in D:
                return [D[x], i]
            if nums[i] not in D:
                D[nums[i]] = i
        
