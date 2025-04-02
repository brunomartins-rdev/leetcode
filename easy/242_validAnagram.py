class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}

        for letter in s:
            if letter in d_s:
                d_s[letter] += 1
            else:
                d_s[letter] = 1

        for letter in t:
            if letter in d_t:
                d_t[letter] += 1
            else:
                d_t[letter] = 1

        return d_s == d_t

solution = Solution()
print(solution.isAnagram('anagram', 'anagarm'))
print(solution.isAnagram('anaggram', 'anagarm'))
