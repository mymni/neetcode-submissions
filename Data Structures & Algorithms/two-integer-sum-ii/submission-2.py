class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = len(numbers)
        r = n - 1

        s = numbers[l] + numbers[r]
        while(s != target):
            if s < target:
                l += 1
            if s > target:
                r -= 1
            
            s = numbers[l] + numbers[r]


        return [l+1, r+1]
