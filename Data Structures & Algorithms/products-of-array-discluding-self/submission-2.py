class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1]
        mult = 1

        n = len(nums)
        for i in range(n-1):
            mult = mult * nums[i]
            sol.append(mult)

        mult = 1
        for i in range(n-1, 0, -1):
            sol[i] = sol[i] * mult
            mult = mult * nums[i]

        sol[0] = sol[0] * mult
        return sol




