class Solution:
    def isPalindrome(self, s: str) -> List:
        l = 0
        r = len(s)-1
        s = s.lower()
        while(l<r):
            while not s[l].isalnum():
                if l == r:
                    return True
                l += 1

            while not s[r].isalnum():
                if r == l:
                    return True
                r -= 1

            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True