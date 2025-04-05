class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            print(f'This is the character {c}')
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    print(f'This is the stack before popping: {stack}')
                    stack.pop()
                    print(f'This is the tsack after popping: {stack}')
                else:
                    return False
            else:
                stack.append(c)
                print(f'This is the stack after appending: {stack}')

        return True if not stack else False

s = Solution()
print(s.isValid('()'))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
print(s.isValid('([])'))
