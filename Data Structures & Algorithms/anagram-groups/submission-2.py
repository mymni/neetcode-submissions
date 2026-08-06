class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combinations = {}
        ans = []
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_index = {}
        for i, letter in enumerate(alphabet):
            alphabet_index[letter] = i

        
        for s in strs:
            counts = [0]*26

            for c in s:
                counts[alphabet_index[c]] += 1
            
            immutable_counts = tuple(counts)
            if immutable_counts not in combinations:
                combinations[immutable_counts] = [s]
            else:
                combinations[immutable_counts].append(s)

        for k in combinations:
            ans.append(combinations[k])
        return ans 
        