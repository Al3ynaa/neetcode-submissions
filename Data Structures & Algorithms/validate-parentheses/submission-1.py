class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if stack and char == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack