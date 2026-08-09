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
            if i == 0:
                sol.append(Dr[1])
            elif i == n-1:
                sol.append(Dl[i-1])
            else:
                sol.append(Dl[i-1] * Dr[i+1])

        return sol



