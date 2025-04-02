from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for item in strs:

            sorted_word = ''.join(sorted(item))

            if sorted_word in d:
                d[sorted_word].append(item)
            else:
                d[sorted_word] = [item]

        return list(d.values())
        
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(["", ""]))
        
