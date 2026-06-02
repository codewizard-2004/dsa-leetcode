class Solution:
    def isValid(self, s: str) -> bool:
        closeChar = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in closeChar:
                if stack and stack[-1] == closeChar[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
            