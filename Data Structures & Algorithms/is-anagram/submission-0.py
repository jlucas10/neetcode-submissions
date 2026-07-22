class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they are not same size return false
        if len(s) != len(t):
            return False
        # create hash map 
        countS, countT = {}, {}
        # loop through s and add to count S and T
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0) 
        # return count S and T as true if they are the same 
        return countS == countT
            

