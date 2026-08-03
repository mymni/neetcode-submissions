class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        D = {}
        for i in nums:
            if i not in D:
                D[i] = True
            else:
                return True
        return False
        