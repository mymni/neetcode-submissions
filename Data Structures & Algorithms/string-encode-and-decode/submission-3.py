class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += ">"
            result += s
    
        return result
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        ptr = 0
        while (ptr < len(s)):
            jump = ""
            tmp = ptr
            while(s[tmp] != ">"):
                jump += s[tmp]
                tmp += 1

            print(jump)
            end = ptr + int(jump)
            decoded.append(s[ptr+len(jump)+1:end+len(jump)+1])
            ptr += int(jump) + len(jump) + 1
        return decoded
