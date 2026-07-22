class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 3 major ways to do it 
        # bruteforce which looks at each index and compares to every index after
        # sorting which sorts array and compares every index after 
        # creating hash set which puts numbers in and checks as we loop through (fastest)
        
        #create hashset
        hashset = set()
        #for loop to loop through nums
        for n in nums:
            #if n is in hashset return true 
            if n in hashset:
                return True
            #add n to hashset and continue looping till end of array
            hashset.add(n)
        # return false if no duplicates
        return False
