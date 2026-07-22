class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they are not same length return false
        if len(s) != len(t):
            return False
        # if they are the same return true 
        return sorted(s) == sorted(t)

            

