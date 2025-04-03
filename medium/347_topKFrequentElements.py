from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        temp = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        result = [x for x in list(temp.keys())[:k]]

        return result

solution = Solution()
print(solution.topKFrequent([1,1,2,2,3,4,5,6,6,6], 3))

