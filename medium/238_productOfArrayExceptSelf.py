from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        pre, pos = 1, 1

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        for i in range(len(nums), -1, -1):
            res[i] *= pos
            pos *= nums[i]

        return res

solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
print(solution.productExceptSelf([4, 3, 2, 1, 2]))

