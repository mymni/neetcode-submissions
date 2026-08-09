class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Dl = {}
        Dr = {}
        multL = 1
        multR = 1

        n = len(nums)
        for i in range(n):
            multL = multL * nums[i]
            multR = multR * nums[-i-1]

            Dl[i] = multL
            Dr[n-i-1] = multR
        
        sol = []
        for i in range(n):
            sol.append(Dl.get(i - 1, 1) * Dr.get(i + 1, 1))
            
        return sol
