class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        mini = nums[0]

        D = {}
        for num in nums:
            if num not in D:
                D[num] = num

        S = {}
        for d in D:
            if d-1 not in D:
                S[d] = 1

        for s in S:
            while(True):
                if s+S[s] not in D:
                    break
                S[s] += 1
                
        maxi = 1
        for s in S:
            if maxi < S[s]:
                maxi = S[s]
                
        return maxi


            