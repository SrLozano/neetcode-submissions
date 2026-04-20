class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        aux_longest_substring = 0
        aux_set = set()
        for first_character_index in range(0, len(s)):
            aux_set.add(s[first_character_index])
            aux_longest_substring+=1
            for end_character_index in range(first_character_index + 1, len(s)):
                if s[end_character_index] not in aux_set:
                    aux_set.add(s[end_character_index])
                    aux_longest_substring+=1
                else:
                    if aux_longest_substring > longest_substring:
                        longest_substring = aux_longest_substring
                    aux_longest_substring = 1
                    aux_set.clear()
                    break

        if aux_longest_substring > longest_substring:
            longest_substring = aux_longest_substring

        return longest_substring