class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        max_count = 0
        for key in counter.keys():
            if counter[key] > max_count:
                max_count = counter[key]
                dominant_c = key

        left = 0
        right = len(s) - 1

        while left < right:
            window_len = right + 1 - left
            max_count = counter[dominant_c]
            
            if (window_len - max_count) <= k or counter[dominant_c] == window_len:
                return window_len
            if s[right] != dominant_c:
                counter[s[right]] -= 1
                right-=1
            elif s[left] != dominant_c:
                counter[s[left]] -= 1
                left+=1
            else:
                counter[s[left]] -= 1
                # todo: encapsulate in a function
                max_count = 0
                for key in counter.keys():
                    if counter[key] > max_count:
                        max_count = counter[key]
                        dominant_c = key
                left+=1

        return -1

