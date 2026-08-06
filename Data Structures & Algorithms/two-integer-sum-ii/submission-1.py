def binarySearch(L, x, start, end):
    mid = start
    low = start
    high = end
    while(low <= high):
        mid = (high + low) // 2
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            low = mid + 1
        elif L[mid] > x:
            high = mid - 1
        
    return -1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n-1):
            x = binarySearch(numbers, target - numbers[i], i+1, n-1)
            if x > -1:
                return [i+1, x+1]
