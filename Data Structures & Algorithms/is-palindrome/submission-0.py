class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.lower()
        print(s)
        l, r = 0, len(s)-1

        while l<r and r>l:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                print(l)
                print(r)
                return False

        return True

