class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        swaps = 0
        
        for bracket in s:
            if bracket == '[':
                stack.append(bracket)
            else:
                if not stack:
                    swaps += 1
                    stack.append('[')
                else:
                    stack.pop()
                    
        return swaps
