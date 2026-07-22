class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #given array of numbers 
        #return true if value appears more than once
        #create hashmap and add each num to hashmap 
        #if number from array is in hashmap return ture 
        #otherwise return false
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 1;
        return False