class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        aux_longest_substring = 0
        aux_set = set()
        for character_index in range(0, len(s)):
            if s[character_index] not in aux_set:
                aux_set.add(s[character_index])
                print(f"set: {aux_set} and character: {s[character_index]}")
                aux_longest_substring+=1
            else:
                if aux_longest_substring > longest_substring:
                    longest_substring = aux_longest_substring
                aux_longest_substring = 0
                aux_set.clear()

        if aux_longest_substring > longest_substring:
            longest_substring = aux_longest_substring

        return longest_substring