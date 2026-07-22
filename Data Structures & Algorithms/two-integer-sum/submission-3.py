class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #loop through nums 
        #loop through nums again but index + 1 
        #check if two nums equal target if do return index 
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []