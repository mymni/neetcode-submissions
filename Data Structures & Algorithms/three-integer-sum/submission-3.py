class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p1 = i+1
            p2 = n-1
            while(p1<p2):
                if nums[i] + nums[p1] + nums[p2] == 0:
                    ans.append([nums[i],nums[p1],nums[p2]])
                    tempP1 = p1
                    tempP2 = p2
                    p1 += 1
                    p2 -= 1
                    while(p1<p2 and nums[tempP1] == nums[p1]):
                        p1 += 1

                    while(p1<p2 and nums[tempP2] == nums[p2]):
                        p2 -= 1

                elif nums[i] + nums[p1] + nums[p2] > 0:
                    tempP = p2
                    p2 -= 1
                    while(p1<p2 and nums[tempP] == nums[p2]):
                        p2 -= 1
                elif nums[i] + nums[p1] + nums[p2] < 0:
                    tempP = p1
                    p1 += 1
                    while(p1<p2 and nums[tempP] == nums[p1]):
                        p1 += 1

        return ans
            


            
