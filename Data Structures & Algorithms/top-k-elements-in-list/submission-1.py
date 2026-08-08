class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        for num in nums:
            if num not in D:
                D[num] = 1
            else:
                D[num] += 1

        n = len(nums)
        frequencies = [0]*(n+1)
        for d in D:
            if frequencies[D[d]] == 0:
                frequencies[D[d]] = [d]
            else:
                frequencies[D[d]].append(d)
        
        ptr = n
        ctr = 0
        sol = []
        while(ctr < k):
            if frequencies[ptr] != 0:
                sol += frequencies[ptr]
                ctr += len(frequencies[ptr])
            ptr -= 1
            
        return sol
