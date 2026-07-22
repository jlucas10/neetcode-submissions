class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort s and sort t and see if they are equal 
        #if so then return true otherwise return false
        if sorted(s) == sorted(t):
            return True
        return False
        