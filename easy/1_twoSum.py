from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):

            complementary = target - nums[i]

            if complementary in d:
                return [i, d[complementary]]
            else:
                d[nums[i]] = i

            print(f'This is the number: {nums[i]}')
            print(f'This is the complementary: {complementary}')
            print(d)


solution = Solution()
# print(solution.twoSum([1, 2, 3], 5))
# print(solution.twoSum([2, 7, 11, 15], 9))
# print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
