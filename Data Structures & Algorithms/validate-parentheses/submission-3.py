class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])

            elif len(stack) == 0:
                return False

            if s[i] == ')':
                if stack[-1]!= '(':
                    return False
                else:
                    stack.pop()

            if s[i] == '}':
                if stack[-1]!= '{':
                    return False
                else:
                    stack.pop()

            if s[i] == ']':
                if stack[-1]!= '[':
                    return False
                else:
                    stack.pop()  
        
        if len(stack) > 0:
            return False
        return True

