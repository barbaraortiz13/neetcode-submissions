class Solution:
    def isValid(self, s: str) -> bool:
        closers = {')':'(','}':'{',']':'['}
        stack = []

        for c in s:
            if c in closers:
                if stack and stack[-1] == closers[c]:
                    stack.pop()
                else:
                    return False
            
            if c not in closers:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
            