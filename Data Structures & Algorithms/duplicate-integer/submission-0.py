class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 3 major ways to do it 
        # bruteforce which looks at each index and compares to every index after
        # sorting which sorts array and compares every index after 
        # creating hash set which puts numbers in and checks as we loop through (fastest)

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
