class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        D = {}
        for i in range(len(s)):
            if s[i] not in D:
                D[s[i]] = 1
            else:
                D[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in D:
                return False
            else:
                if D[t[i]] == 0: 
                    return False
                D[t[i]] -= 1
        
        for j in D:
            if D[j] != 0:
                return False
        return True

        