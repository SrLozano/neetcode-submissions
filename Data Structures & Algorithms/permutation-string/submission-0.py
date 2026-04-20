class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_set = set(s1)
        
        for i in range(0, len(s2) - len(s1)):
            substring = s2[i:i+len(s1)]
            if set(substring) == s1_set:
                return True

        return False


        
        '''s1
        for slicing window on s2:
            if set(s2) == set(s1)
                return true


        questions: lower case?
                    repetition?'''