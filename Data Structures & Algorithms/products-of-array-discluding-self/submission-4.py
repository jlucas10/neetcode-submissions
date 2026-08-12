class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        U: 
            input - array of nums 
            output - product of all elements of num except nums[i]
            assumption - loop through twice and just dont multiply 
            the one your on. 
        P: 
            for 
                for 
                if i = j continue 
                else product = i * j 
            return product
        """
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix*= nums[i]
        
        suffix = 1
        for i in range(n -1 ,-1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

