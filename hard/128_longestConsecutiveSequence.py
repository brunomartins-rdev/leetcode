from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)
        longest = 0

        for n in setNum:
            if (n - 1) not in setNum:
                length = 0
                while (n+length) in setNum:
                    length += 1
                longest = max(length, longest)

        return longest

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))

