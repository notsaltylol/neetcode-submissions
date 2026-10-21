class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif not stack:
                return False
            else:
                bracket = stack.pop()
                if (bracket+c) not in ['()', '{}', '[]']:
                    return False
        return not stack
        