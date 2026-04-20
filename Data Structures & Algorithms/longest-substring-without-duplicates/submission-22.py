class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l, r = 0, 1

        longest_substring = 1

        found = set(s[l])

        while r in range(len(s)):

            if s[r] not in found:
                found.add(s[r])
                r+=1
                if len(found) > longest_substring:
                    longest_substring = len(found)

            else: 
                found.remove(s[l])
                l+=1

        return longest_substring
